import pygame
import os
from Turckeys import button
from Turckeys import text_objects
from Turckeys import get_image
from operator import itemgetter
import copy

x = []
y = 0

white = (245, 245, 220)
wheat = (245, 222, 179)
black = ((0, 0, 0))
gold = (218, 165, 32)

# initialize screen
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Guru's Turkeys")
done = False


def scorestitle(x, y, w, h):
    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects("Leaderboards:", smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

##scorestitle
#smallText = pygame.font.Font("freesansbold.ttf", 50)
#textSurf, textRect = text_objects("High Scores:", smallText)
#textRect.center = ((150 + (100 / 2)), (50 + (40/ 2)))
#screen.blit(textSurf, textRect)


def lines(num, x, y, w, h):
    for line in range(1, 10):
        smallText = pygame.font.Font("freesansbold.ttf", 30)
        textSurf, textRect = text_objects(str(num) + ". ", smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)


def getScores():
    global x
    x = []
    global y
    with open('highscores.txt', 'r') as fileee:
        d = fileee.readlines()
        for l in d:
            n = l.strip('\n').split(' ')
            # print(n)
            x.append(n)
        # x.remove([''])
        print(x)
    y = x[-1][1]
    print(x[-1][1])
    x = sorted(x, key=itemgetter(1), reverse=True)
    return x


def showScores(score, x, y, w, h):
    for line in range(1, 10):
        smallText = pygame.font.Font("freesansbold.ttf", 30)
        textSurf, textRect = text_objects(score, smallText)
        textRect = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)

def yourscore(xx, yy, w, h):
    global x
    global y
    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects("Your Score: "+str(y), smallText)
    textRect.center = ((xx + (w / 2)), (yy + (h / 2)))
    screen.blit(textSurf, textRect)



def scorescreen():
    done = False
    scores = getScores()
    # gameloop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    if 350 < mouse_pos[0] < 560 and 700 < mouse_pos[1] < 760:
                        print('menu button clicked')
                        done = True
                        return 7
                    elif 610 < mouse_pos[0] < 760 and 700 < mouse_pos[1] < 760:
                        print('exit button clicked')
                        done = True
                        return 2

        screen.fill((173, 216, 230))
        scorestitle(150, 50, 100, 40)
        yourscore(600, 400, 200, 40)

        # lines
#        screen.blit(textSurf, textRect)
    
        #lines
        h = 150
        for i in range(1, 11):
            lines(i, 30, h, 40, 40)
            h += 50
            # scores
            h2 = 135
        
        for i in range(10):
            score = scores[i][0] + " " + scores[i][1]
            showScores(score, 30, h2, 100, 40)
            h2 += 50

        turkey = pygame.transform.scale(get_image('cookedTurkey.png'), (350, 200))
#        for i in range(10):
#            score = scores[i][0] + " " + scores[i][1]
#            showScores(score,30,h2,100,40)
#            h2 += 50
    
        button("Menu", 350,700,210,60,white,gold,30)
        button("Exit", 610,700,150,60,white, gold,30)
    
    
        screen.blit(turkey, (630, 20))
        runningTurkey = pygame.transform.scale(get_image('runningTurkey.png'), (190, 130))
        screen.blit(runningTurkey, (100, 670))

        pygame.display.flip()
        # os.clock.tick(60)


if __name__ == '__main__':
    scorescreen()