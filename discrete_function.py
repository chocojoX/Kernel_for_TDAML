import numpy as np
from persistence_diagram import *


class discrete_function(object):
    def __init__(self, high=10, grid_step=0.1):
        x = np.arange(0, high, grid_step);
        y = np.arange(0, high, grid_step)
        [Y, X] = np.meshgrid(y, x)
        grid = np.maximum(np.abs(X), np.abs(Y))
        print(grid)


    def get_kernelized(self, diag, t):
        # TODO later on for visualization
        for p in diag.points:
            pass
