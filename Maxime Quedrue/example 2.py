﻿import pygame

from pygame.locals import *

plateau=[0,1,2,3,4,5,6,7,8,5,9,10,11,12,5,13,14,15,5,16,17,18,19,5,20,21,22,5,23,24,25,26,5,27,28,29,5,30,31,32,5,33,34,35,5,36,37,38,39,5,40,41,42,5,43,44,45,46,5,47,48,49,50,51]


pygame.init()

clock = pygame.time.Clock()




screenInfo = pygame.display.Info()

(width, height) =(screenInfo.current_w, screenInfo.current_h)

window = pygame.display.set_mode( (width, height), FULLSCREEN )






image = plateau



running = True

while running:
    clock.tick(60)

    window.fill( (100,50,70) )

    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False



pygame.quit()