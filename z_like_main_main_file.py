from Turckeys import startscreen
from turkeykiller import playgame
from Scores import scorescreen
import pygame

x = 7

while x==7:
    startscreen(False)
    
    playgame(False)
    print('done')
    
    x = scorescreen()
    
    if x==2:
        print('EXITED')
        break

pygame.quit()