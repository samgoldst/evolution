import random

import numpy as np

from cell import Cell
from food import Food


class Board:
    def __init__(self, width, height, num_foods, num_cells):
        self.foods = []
        for i in range(num_foods):
            x = random.randint(0, width)
            y = random.randint(0, height)
            self.foods.append(Food(x, y))

        self.cells = []
        for i in range(num_cells):
            x = random.randint(0, width)
            y = random.randint(0, height)
            first_weights = np.random.uniform(0, 1, 10)
            second_weights = np.random.uniform(0, 1, (2, 10))
            self.cells.append(Cell(x, y, first_weights, second_weights))

    def simulate(self, generations):
        for i in range(generations):
