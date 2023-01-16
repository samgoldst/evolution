import numpy as np
import pygame

from board import Board


b = Board(800, 800, 500, 50, 25)
b.simulate(1, 50, .1)
#define constants

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Pygame Template')

done = False

clock = pygame.time.Clock()

percentage = .5

while True:
    gen = b.simulate(1, 720, percentage)[0]
    cs = b.cells.copy()
    cs.sort(key=lambda x: x.fitness, reverse=True)
    top = cs[0]
    print(top.first_weights, "\n", top.second_weights)
    percentage *= .98
    for frame in gen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((255, 255, 255))

        for c in frame[0]:
            pygame.draw.circle(screen, c[1], c[0], 7)
        for f in frame[1]:
            pygame.draw.circle(screen, (0, 255, 0), f, 7)

        pygame.display.update()
        clock.tick(60)
pygame.quit()
