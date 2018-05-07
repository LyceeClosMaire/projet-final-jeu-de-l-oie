import pygame

from pygame.locals import *



pygame.init()

clock = pygame.time.Clock()



# window est du type Surface(), on peut donc utiliser blit(), fill() sur window

# et donc "dessiner sur l'écran" (attention cela se fait en réalité en mémoire, il

# faut appeler flip() pour que cela devienne visible)

window = pygame.display.set_mode( (800,600) )


# vous pouvez chargez n'importe quel fichier image, les png sont recommandés comme

# format (car ils gèrent bien la transparence)

image = []

for i in range(52):
    image.append( pygame.image.load(str(i)+".png") )



running = True

while running:

   clock.tick(60)



   # ATTENTION à l'ordre dans lequel vous manipulez window, commencez par le fond

   # puis dessinez par dessus sinon vous recouvrirez vos images par votre fond

   window.fill( (200,50,50) )



   # blit() permet de recopier une Surface dans une autre Surface à n'importe quelles

   # coordonnées (attention l'axe des ordonnées est orienté vers le bas et l'origine

   # est dans le coin en haut à gauche)

   window.blit( image[0], (10,10) )
   window.blit( image[1], (50,10))










   # une autre opération très utile est la mise à l'échelle :

   # smoothscale permet de transformer les dimensions d'une image

   # commençons par récupérer les dimensions de notre image d'origine

   (width, height) = image[0].get_size()

   # attention les dimensions doivent être un nombre _entier_ de pixel donc // plutôt que /

   smaller = pygame.transform.smoothscale( image[0], (width // 3, height // 3) )












   # avec Surface vous avez également accès à la couleur de chaque pixel

   # on va modifier une copie de notre image d'origine

   grey_levels = image[0].copy()

   # on parcourt chaque pixel de la surface

   (xmax, ymax) = image[0].get_size()

   for x in range(xmax):

       for y in range(ymax):

           # on récupère les composantes rouge, verte, bleue et alpha (opacité) d'un

           # pixel comme des entiers entre 0 et 255

           (red, green, blue, alpha) = image[0].get_at( (x,y) )

           mean = (red + green + blue) / 3

           # si vous souhaitez réellement mettre une image en niveaux de gris,

           # il existe des formules plus sophistiquées

           grey_levels.set_at((x,y), (mean, mean, mean, alpha))

   # notez qu'opérer pixel par pixel est trop lent si l'on doit le faire à chaque tour

   # de boucle en temps réel

   window.blit(grey_levels, (10, 500) )





   pygame.display.flip()



   for event in pygame.event.get():



       if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):

           running = False



pygame.quit()