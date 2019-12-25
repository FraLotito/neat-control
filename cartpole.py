import os
import multiprocessing

import gym
import neat
import numpy as np
import graphviz


def eval_genome(genome, config):
    # Creates a FeedForward Network with the evolved genome and the requested config
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    fitnesses = []
    runs_per_net = 10

    for _ in range(runs_per_net):
        observation = env.reset()
        fitness = 0
        for _ in range(500):
            # The observation is used as the input of the NN
            action = net.activate(observation)

            # As the action we take the one with the highest probability
            action = int(np.argmax(action))

            # We take the action
            observation, reward, done, _ = env.step(action)

            # And get a reward

            fitness += reward
            if done:
                fitnesses.append(fitness)
                break
        fitnesses.append(fitness)

    # The genome's fitness is its worst performance across all runs.
    return min(fitnesses)


# Evaluation over 100 episodes
def eval_winner_net(winner, config):
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    fitnesses = []
    for _ in range(100):
        observation = env.reset()
        fitness = 0
        for _ in range(500):
            action = winner_net.activate(observation)
            action = int(np.argmax(action))
            observation, reward, done, _ = env.step(action)
            fitness += reward
            if done:
                fitnesses.append(fitness)
                break
        fitnesses.append(fitness)
    print("Average fitness across 100 episodes is: {}".format(np.mean(fitnesses)))
    if np.mean(fitnesses) > 475:
        print(" + The task is solved + ")
    else:
        print(" - The task is not solved - ")

# Final animation
def viz_winner_net(winner, config):
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    for _ in range(3):
        observation = env.reset()
        for _ in range(500):
            env.render()
            action = winner_net.activate(observation)
            action = int(np.argmax(action))
            observation, _, done, _ = env.step(action)
            if done:
                break

# Loads the CartPole environment
env = gym.make('CartPole-v1')

# Loads NEAT configuration file
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'cartpole.config')
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    config_path)
population = neat.Population(config)

# Adds statistics report
stats = neat.StatisticsReporter()
population.add_reporter(stats)
population.add_reporter(neat.StdOutReporter(True))

# Parallel execution over all the available processors
pe = neat.ParallelEvaluator(multiprocessing.cpu_count(), eval_genome)

# Runs the NEAT algorithm and returns the best network
winner = population.run(pe.evaluate)

# Evaluation of the evolved network on 100 episodes
eval_winner_net(winner, config)

# Visualization 
viz_winner_net(winner, config)

# Close the environment
env.close()
