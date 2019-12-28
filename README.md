# Self-solving control problems with NEAT
This is a brief tutorial to solve some classical control problems from the OpenAI Gym environment using the NEAT algorithm.

## Background

### NEAT
NEAT (Neuro-Evolution of Augmenting Topologies) is a popular neuroevolution algorithm. Usually, when you are dealing with neural networks you need to decide apriori the topology of the network (this is tipically done relying on experience and heuristics) and then you train the weights of the networks through gradient descent and backpropagation; the idea behind the NEAT algorithm is to use an evolutionary approach to make the topology and the weights of the neural network evolve to solve a certain task. 

You can find more information on the algorithms in this paper http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf

A python implementation of NEAT is available with the package python-neat.

### OpenAI Gym
The Gym library is a collection of test problems — environments — that you can use to work out your reinforcement learning algorithms, these environments have a shared interface, allowing you to write general algorithms. It supports teaching agents everything from walking to playing games like Pong or Pinball.

It makes no assumptions about the structure of your agent, and it's compatible with any numerical computation library.

## Environments
So far this repository contains the write-ups of the following environments:

* [CartPole-v1](https://github.com/FraLotito/neat-control/tree/master/cartpole)
* [LunarLander-v2](https://github.com/FraLotito/neat-control/tree/master/lunarlander)