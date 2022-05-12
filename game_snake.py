import pygame
import time
pygame.init()

orange = pygame.Color(247, 114, 5)
game= pygame.display.set_mode((720,480))
game.fill((255,255,255))

x = [[120,50], [110,50], [100,50]]

for pos in x:   
    pygame.draw.rect(game, orange, pygame.Rect(pos[0],pos[1],10,10))

pygame.display.flip()
time.sleep(5)