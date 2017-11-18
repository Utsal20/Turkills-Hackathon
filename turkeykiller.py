# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:38:14 2017

@author: Amon
"""

import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

#initialize screen
pygame.init()
screen = pygame.display.set_mode((1400, 800))
done = False

#gameloop
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
                screen.fill((175,238,238))
        
                turkey = pygame.transform.scale(get_image('turkey.png'),(100,100))
                screen.blit(turkey, (20, 20))

        
        pygame.display.flip()
        #os.clock.tick(60)