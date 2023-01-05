import numpy as np

class Cell:
    def __init__(self, x, y, first_weights, second_weights):
        self.x = x
        self.y = y
        self.first_weights = first_weights
        self.seconds_weights = second_weights