import pygame

from pygame.locals import *



pygame.init()

clock = pygame.time.Clock()



window = pygame.display.set_mode( (800,600) )

image = pygame.image.load("image/img.jpg")

running = True

while running:
   clock.tick(60)

   # ATTENTION à l'ordre dans lequel vous manipulez window, commencez par le fond
# puis dessinez par dessus sinon vous recouvrirez vos images par votre fond
   window.fill( (255,0,0) )

   # blit() permet de recopier une Surface dans une autre Surface à n'importe quelles
   # coordonnées (attention l'axe des ordonnées est orienté vers le bas et l'origine
    # est dans le coin en haut à gauche)

   for i in range(0,1000):
       pos = image.get_rect()
       pos = pos.move(i, i)
       window.blit( image, pos)
       pygame.display.flip()

   for event in pygame.event.get():
       if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
           running = False

pygame.quit()

