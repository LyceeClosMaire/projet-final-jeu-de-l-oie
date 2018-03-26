
import pygame



from pygame.locals import *





pygame.init()




screenInfo = pygame.display.Info()

(width, height) =(screenInfo.current_w, screenInfo.current_h)

window = pygame.display.set_mode( (width, height), FULLSCREEN )





running = True


while running:



   window.fill( (100,20,70) )





   pygame.display.flip()



   for event in pygame.event.get():




       if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):



           running = False





pygame.quit()

