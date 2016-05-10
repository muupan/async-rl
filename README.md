# Async-RL

![A3C playing Breakout](https://raw.githubusercontent.com/muupan/async-rl/master/trained_model/breakout/animation.gif)

This is a repository where I attempt to reproduce the results of [Asynchronous Methods for Deep Reinforcement Learning](http://arxiv.org/abs/1602.01783). Currently I have only reproduced the results of A3C FF on Atari Breakout.

Any feedback is welcome :)

## Current Status

I trained A3C for ALE's Breakout with 36 processes (AWS EC2 c4.8xlarge) for 80 million training steps, which took about 17 hours. The mean and median of scores of test runs along training are plotted below. Ten test runs for every 1 million training steps (counted by the global shared counter). The results seems slightly worse than theirs.

![A3C scores on Breakout](https://raw.githubusercontent.com/muupan/async-rl/master/trained_model/breakout/scores.txt.png)

The trained model is uploaded at `trained_model/breakout/80000000_finish.h5`, so you can make it to play Breakout by the following command:

```
python demo_a3c_ale.py <path-to-breakout-rom> trained_model/breakout/80000000_finish.h5
```

I received a confirmation about their implementation details and some hyperparameters by e-mail from Dr. Mnih. I summarized them in the wiki: https://github.com/muupan/async-rl/wiki

## Requirements

- Python 3.5.1
- chainer 1.8.1
- cached-property 1.3.0
- h5py 2.5.0
- Arcade-Learning-Environment

## Training

```
python a3c_ale.py <number-of-processes> <path-to-atari-rom>
```

`a3c_ale.py` will save best-so-far models and test scores into the output directory.

## Evaluation

```
python demo_a3c_ale.py <path-to-atari-rom> <trained-model>
```

## Similar Projects

- https://github.com/miyosuda/async_deep_reinforce
