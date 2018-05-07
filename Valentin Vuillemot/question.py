import pygame
import random
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode( (800,600) )
winrect = window.get_rect()  # j'obtient un rectangle de la taille de l'écran créé
window.fill( (255,0,0) )

question = pygame.image.load("lancer_les_de/question.png") # je charge mon image : question
centerQuest = question.get_rect(center = winrect.center) # j'obtient un rectangle de la taile de "question"
window.blit(question,centerQuest)                        # ce rectagle sera au centre de l'écran créé

de1 = pygame.image.load("lancer_les_de/de1.png")
de2 = pygame.image.load("lancer_les_de/de2.png")
de3 = pygame.image.load("lancer_les_de/de3.png")
de4 = pygame.image.load("lancer_les_de/de4.png")
de5 = pygame.image.load("lancer_les_de/de5.png")
de6 = pygame.image.load("lancer_les_de/de6.png")
mes_des = [de1 , de2 , de3 , de4 , de5 , de6]

centerDe1 = de1.get_rect(center = winrect.center)
centerDe2 = de2.get_rect(center = winrect.center)
centerDe3 = de3.get_rect(center = winrect.center)
centerDe4 = de4.get_rect(center = winrect.center)
centerDe5 = de5.get_rect(center = winrect.center)
centerDe6 = de6.get_rect(center = winrect.center)
mes_centre = [centerDe1 , centerDe2 , centerDe3 , centerDe4 , centerDe5 , centerDe6]
pygame.display.flip()       #je fait passer sur mon écran tout ce que j'ai "blité"

running = True

while running:

   for event in pygame.event.get():

       if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):

           running = False
       if event.type == MOUSEBUTTONDOWN and event.button == 1: # si un evenement est du type clic souris
                                                               # et que c'est le clic gauche alors ....
           if centerQuest.collidepoint(event.pos): # si le tuple des coordonnées du clic est
                window.fill( (255,0,0) )         # est sur le rectangle question alors ...
                de = random.randint(0,5)
                window.blit(mes_des[de],mes_centre[de])
                pygame.display.flip()              # ne ré afficher que l'écran rouge (l'arrière plan)
pygame.quit()