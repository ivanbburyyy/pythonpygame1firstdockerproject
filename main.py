import pygame
import sys
from pygame.constants import QUIT
pygame.init()
size_app = (500,400)
display = pygame.display.set_mode(size_app)
pygame.display.set_caption("куб")
background = (0,0,255)
FPS = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display.fill(background)
    pygame.display.flip()
    FPS.tick(60)
pygame.quit()
