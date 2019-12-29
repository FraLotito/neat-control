# LunarLander-v2
Rocket trajectory optimization is a classic topic in Optimal Control. The goal of the agent is to land the space-ship inside the landing pad (the space between the two yellow flags). The space-ship is controlled by one main engine (bottom) and two side engines (left and right).

<img src="../images/lunar.jpg" width="500" height="270" />

## Observations

Type: Box(8)

## Actions

Type: Discrete(4)

| ID |	Action |
| ---- | ----- |
| 0 	| Do nothing |
| 1 	| Fire left engine |
| 2 	| Fire main engine |
| 3 	| Fire right engine |

## Reward and episode termination
Reward for moving from the top of the screen to landing pad and zero speed is about 100 to 140 points. If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Solved is 200 points. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt. 

## Starting state
Landing pad is always starting at coordinates (0,0).

## Solved requirements
The task is considered solved when the average reward is greater than or equal to 200.0 over 100 consecutive trials.

## Example of the solution
The tasks takes about 80 generations to be solved.

This is the evolved neural network which solved the environment

<img src="../images/lunar_net.svg" width="500" height="270" />

and this is an animation of the lander controlled by it.

<img src="../images/lunar.gif" width="500" height="270" />