# Async-RL

This is a repository where I attempt to reproduce the results of [Asynchronous Methods for Deep Reinforcement Learning](http://arxiv.org/abs/1602.01783). It's still work-in-progress and not so successfull compared to the original results.

## Requirements

- chainer
- cached_property
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
