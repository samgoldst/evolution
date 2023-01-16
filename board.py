import copy
import math
import random
import numpy as np

from cell import Cell
from food import Food


class Board:
    def __init__(self, width, height, num_foods, num_cells, reach):
        self.width = width
        self.height = height
        self.reach = reach
        self.foods = []
        self.cells = []
        for i in range(num_foods):
            x = random.randint(0, width)
            y = random.randint(0, height)
            self.foods.append(Food(x, y))
        for i in range(num_cells):
            x = random.randint(0, width)
            y = random.randint(0, height)
            first_weights = np.random.uniform(-1, 1, (5, 4))
            second_weights = np.random.uniform(-1, 1, (2, 5))
            self.cells.append(Cell(x, y, first_weights, second_weights))

    def simulate(self, generations, timesteps, percentage):
        print()
        log = []
        for i in range(generations):
            total = 0
            generation_log = []
            for j in range(timesteps):
                # print(f"\r{i}: {j}   ", end="")
                timestep_log = [[],[]]
                for c in self.cells:
                    c.action(*self.closest_food(c))
                    eaten = self.eat(c)
                    c.eat(eaten)
                    total += eaten
                    timestep_log[0].append([(c.x, c.y), c.color])
                for f in self.foods:
                    timestep_log[1].append((f.x, f.y))
                generation_log.append(timestep_log)
            log.append(generation_log)
            print(total, max([c.fitness for c in self.cells]))
            self.purge(percentage)
        return log

    def closest_food(self, c: Cell):
        cx, cy = c.x, c.y
        angle = None
        min = -1
        for f in self.foods:
            distance = math.sqrt((cx - f.x) ** 2 + (cy - f.y) ** 2)
            if distance < min or min == -1:
                min = distance
                angle = math.degrees(math.atan2((cy - f.y), (cx - f.x)))
        return angle, min

    def eat(self, c: Cell):
        cx, cy = c.x, c.y
        eaten = 0
        for f in self.foods:
            if math.sqrt((cx - f.x) ** 2 + (cy - f.y) ** 2) < self.reach:
                f.x, f.y = random.randint(0, self.width), random.randint(0, self.height)
                eaten += 1
        return eaten

    def data(self):
        self.cells.sort(key=lambda x: x.fitness, reverse=True)
        print()
        for c in self.cells:
            print(f"{c.fitness}")

    def purge(self, percentage):
        self.cells.sort(key=lambda x: x.fitness, reverse=True)
        self.cells = self.cells[:len(self.cells)//2]
        self.cells += copy.deepcopy(self.cells)
        for c in self.cells:
            c.x = random.randint(100, 700)
            c.y = random.randint(100, 700)
            c.change(.1)
        for f in self.foods:
            f.x  = random.randint(0, 800)
            f.y = random.randint(0, 800)
