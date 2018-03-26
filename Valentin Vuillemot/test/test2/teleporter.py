import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )

coord_cases = [(0,0) , (400,0) , (700,0), (700,120), (700,300), (700,580)]


PionJ1 = pygame.image.load("pion/pion1.png")
PosJ1 = PionJ1.get_rect()
caseJ1 = 0


PionJ2 = pygame.image.load("pion/pion2.png")
PosJ2 = PionJ2.get_rect()
caseJ2 = 0


def afficher (pion, case):
    window.blit( pion, coord_cases[case])
# on lance les dé

running = True
while running:
   clock.tick(60)

   window.fill( (255,0,0) )

   afficher(PionJ1,0)
   afficher(PionJ2,4)

   pygame.display.flip()

   for event in pygame.event.get():
       if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
           running = False

pygame.quit()
