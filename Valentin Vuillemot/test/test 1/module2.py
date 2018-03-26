import pygame

from pygame.locals import *



pygame.init()

clock = pygame.time.Clock()



window = pygame.display.set_mode( (800,600) )

image = pygame.image.load("image/img.jpg")
pos = image.get_rect()


running = True
while running:
   clock.tick(60)

   window.fill( (255,0,0) )

   pos = pos.move(2, 2)
   window.blit( image, pos)  #affiche limage en arrière plan

   pygame.display.flip()    # en premier plan

   for event in pygame.event.get():
       if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
           running = False

pygame.quit()

