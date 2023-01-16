import random

import numpy as np
import math


class Cell:
    def __init__(self, x, y, first_weights, second_weights):
        self.fitness: int = 0
        self.angle_acceleration = 36
        self.acceleration = .1
        self.x: float = x
        self.y: float = y
        self.first_weights = first_weights
        self.second_weights = second_weights
        self.angle = random.randint(0, 360)
        self.velocity = 0
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 122)]

    def action(self, angle: float, distance: float):
        intermediate_values = np.tanh(np.dot(self.first_weights, np.array((self.angle - angle, distance, self.x, self.y))))
        output = np.tanh(np.dot(self.second_weights, intermediate_values) / 10)
        self.angle += self.angle_acceleration * output[0]
        self.angle %= 360
        if abs(self.angle_acceleration) > 12 or abs(self.angle_acceleration) < 3:
            self.velocity /= 1.3
        self.velocity += self.acceleration * output[1]
        self.x += self.velocity * math.cos(math.radians(self.angle))
        self.y += self.velocity * math.sin(math.radians(self.angle))
        if self.x > 800:
            self.x = 800.0
            self.angle = (self.angle + 180) % 360
        if self.x < 0:
            self.x = 0.0
            self.angle = (self.angle + 180) % 360
        if self.y > 800:
            self.y = 800.0
            self.angle = (self.angle + 180) % 360
        if self.y < 0:
            self.y = 0.0
            self.angle = (self.angle + 180) % 360

    def eat(self, eaten):
        self.fitness += eaten

    def change(self, percent):
        self.first_weights += np.random.uniform(-percent, percent, (5, 4))
        self.second_weights += np.random.uniform(-percent, percent, (2, 5))
        self.angle_acceleration += random.randint(-3, 3)
        self.angle = random.randint(0, 360)
        self.velocity = 0
        self.fitness = 0
        for i in range(3):
            self.color[i] += random.randint(-25, 25)
            if self.color[i] > 255:
                self.color[i] = 255
            if self.color[i] < 0:
                self.color[i] = 0
