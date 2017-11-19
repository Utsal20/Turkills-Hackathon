# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:38:14 2017

@author: Amon, Utsal, Anujin, Ene
"""

import pygame
import os

#image library function
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
screen = pygame.display.set_mode((1000, 800))
#background color
screen.fill((175,238,238))
bg = get_image('landscape.jpg')

#score text
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
score = int(1);
textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
def update_score(i):
        global textsurface
        global score
        score = score + i
        textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
update_score(0)

#turkey image
turkey_list = [(50,50),(500,500),(150,500)]
turkey = pygame.transform.scale(get_image('turkey.png'),(150,150))
def show_turkeys():
        for i in turkey_list:
                screen.blit(turkey, i)


#gameloop
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left click grows radius 
                                update_score(5)
                
        screen.blit(bg, (0,0))
        update_score(0)
        show_turkeys()
        
        pygame.display.flip()
        #os.clock.tick(60)
        