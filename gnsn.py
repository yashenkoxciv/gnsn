import numpy as np


def gnsn(k, n):
    # todo: add option to set minimal value
    v = np.random.uniform(size=k)
    v = v / v.sum()
    v = (v * n).astype(np.int)
    # todo: choose random item to do addition
    v[-1] += n - v.sum()
    return v
