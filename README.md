# Async-RL

This is a repository where I attempt to reproduce the results of [Asynchronous Methods for Deep Reinforcement Learning](http://arxiv.org/abs/1602.01783). It's still work-in-progress and not so successfull compared to the original results.

## Current Status

I trained A3C for ALE's Breakout with 8 processes for about 2 days and 5 hours. The scores of test runs along training are plotted below. One test run for every 100000 training steps (counted by the global shared counter).

![A3C scores on Breakout](https://raw.githubusercontent.com/muupan/async-rl/master/trained_model/breakout_scores.png)

### Some hyperparameters

- RMSprop
 - learning rate: initialize with 3.5e-4 (policy) and 7e-4 (value function) and linearly decrease to zero
 - epsilon: 0.1 (epsilon is inside sqrt)
 - alpha: 0.99

## Requirements

- chainer (>=1.8.1)
- cached-property (>=1.3.0)
- Arcade-Learning-Environment

## Train

```
python a3c_ale.py <number-of-processes> <path-to-atari-rom>
```

`a3c_ale.py` will save best-so-far models and test scores into the output directory.

## Evaluation

```
python demo_a3c_ale.py <path-to-atari-rom> <trained-model>
```

You can make the trained model to play Breakout by:

```
python demo_a3c_ale.py <path-to-breakout-rom> trained_model/breakout_48100000.h5
```
