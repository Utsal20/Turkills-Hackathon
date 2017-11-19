# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:38:14 2017

@author: Amon, Utsal, Anujin, Ene
"""

import pygame
import os
import random
import time
from pygame import mixer

#initialize screen
pygame.init()
screen = pygame.display.set_mode((1000, 800))

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
    
#background color
screen.fill((175,238,238))
bg = get_image('landscape.jpg')

#score text
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
score = int(0);
textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
def update_score(i):
        global textsurface
        global score
        score = score + i
        textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
update_score(0)

#turkey images
turkey = pygame.transform.scale(get_image('turkey.png'),(100,100))
turkey_list = (500,500)
def show_turkeys():
        screen.blit(turkey,turkey_list)
        #for i in turkey_list:
                #screen.blit(turkey, i)
                
#turkey sounds
mixer.init()
mixer.music.load('turkeysound2.wav')

def new_turkey():
        return int(random.randint(0,1000)/100)*100,int(random.randint(0,800)/100)*100

#check if turkey was brutally murdered and do something if it was...
def turkey_killed_or_not(mouse_pos):
        global turkey_list
        global time1
        global time_level
        pos=(0,0)
        pos = int((mouse_pos[0])/100)*100,int((mouse_pos[1])/100)*100
        print('pos: ',pos)
        if pos == turkey_list:
                update_score(200)
                if mixer.music.get_busy():
                        mixer.music.stop()
                        print('sound stoppped')
                mixer.music.play()
                time_level = time_level * 0.9;
                print('timelevel: ',time_level)
                print('turkey killed')
                print('sound played')
                turkey_list = new_turkey()
                time1 = time.time()
            
#save score to file
def save_score(score):
        with open('highscores.txt','a') as filehandler:
                filehandler.writelines('name '+str(score)+'\n')
        print('highscore saved: ','name ',score)
        
mouse_pos = (0,0)
time1 = time.time()
time_level = 2.0

timer = time.time()

def playgame():
        global time1, turkey_list
        #gameloop
        done = False
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                        mouse_pos = pygame.mouse.get_pos()
                                        print(mouse_pos)
                                        turkey_killed_or_not(mouse_pos)
                                        
                if time.time()-time1 > time_level:
                        turkey_list = new_turkey()
                        time1 = time.time()
                
                print("Time: ", 30-(time.time()-timer) )        
                if time.time()-timer>30:
                        done = True
                
                                
                screen.blit(bg, (0,0))
                update_score(0)
                show_turkeys()
                
                pygame.display.flip()
                #os.clock.tick(60)
                
        save_score(score)
        

if __name__=='__main__':
        playgame()

