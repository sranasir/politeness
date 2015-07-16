__author__ = 'raza'
import numpy as np


def softmax(_input):
    """
    Applies softmax function and computes the output
    """
    score = np.exp(_input)
    _sum = np.sum(score)

    return np.divide(score, _sum)


def tanh_derivative(_input):
    """
    Computes and returns derivative of a tangent hyperbolic function
    1 - (f'(x))^2
    """
    return 1. - np.square(_input)


def concat_with_bias(*vectors):
    """
    Stacks and returns the two given vectors vertically.
    Adds an always-on input for the bias units.
    """
    return np.vstack(vectors + (1., ))


def concat(*vectors):
    """
    Stacks and returns the two given vectors vertically
    """
    return np.vstack(vectors)

def init_random_purana(mean, var, shape):
    return np.random.normal(mean, var, size=shape)

def init_random(shape):
    dim = shape[0]
    range = 1 / (2*np.sqrt(dim))
    matrix = np.zeros(shape)
    matrix[:, :dim] = np.random.uniform(-range, range, (dim, dim)) + np.identity(dim)
    matrix[:, dim:2*dim] = np.random.uniform(-range, range, (dim, dim)) + np.identity(dim)
    return matrix
