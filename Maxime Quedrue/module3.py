  # les transformations sont dans pygame.transform :

   # il est souvent utile de refléter une image horizontalement (autrement dit

   # autour de l'axe des ordonnées) :

   symetricH = pygame.transform.flip( image0, True, False)

   window.blit( symetricH, (210,10) )

   # ou verticalement (autrement dit autour de l'axe des abscisses) :

   symetricV = pygame.transform.flip( image0, False, True)

   window.blit( symetricV, (310,10) )

   # ou les deux :

   symetricVH = pygame.transform.flip( image0, True, True)

   window.blit( symetricVH, (410,10) )



   bigger = pygame.transform.smoothscale( image0, (width * 2, height * 2) )


 # on peut également utiliser des dimensions arbitraires

   squashed = pygame.transform.smoothscale( image0, (100, 50) )

   window.blit( smaller, (10, 200) )

   window.blit( bigger, (60, 200) )

   window.blit( squashed, (260, 200) )

   # il existe une fonction scale() mais le résultat est moins bon et smoothscale()

   # est généralement accélérée par le matériel donc n'utilisez que smoothscale()

   bigger2 = pygame.transform.scale( image0, (width * 2, height * 2) )

   window.blit( bigger2, (400, 200) )




 # il est également possible de faire tourner une image dans le sens direct

   # d'un certain angle (en degrés) ou de combiner mise à l'échelle et rotation

   # avec rotozoom()

   rotated = pygame.transform.rotate( image0, 45 )

   window.blit( rotated, (10, 400) )

   # le résultat de rotozoom() est de meilleure qualité (même si vous choisissez

   # une échelle de 1) donc n'utilisez rotate() que si la vitesse est primordiale

   rotated_and_zoomed = pygame.transform.rotozoom( image1, 45, 1 )

   window.blit( rotated_and_zoomed, (110, 400) )
