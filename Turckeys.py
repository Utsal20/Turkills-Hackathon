import pygame
import pygame_textinput
import os
import time

_image_library = {}

white = (245,245,220)
wheat = (245, 222,179)
black = ((0,0,0))
gold = (218,165,32)
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,color,hc,size):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hc, (x, y, w, h))
        if click[0] == 1:
            print("Clicked")
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/ 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
    pygame.draw.rect(screen, black, (x, y, w, h), 1)


def fb(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    cfb = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if cfb[0] == 1:
            print("directing to  fb")
    fb = pygame.transform.scale(get_image('fb.png'), (220, 90))
    screen.blit(fb, (x, y))

def  text(msg,x,y,w,h,size):
    smallText = pygame.font.Font("freesansbold.ttf", size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

textinput = pygame_textinput.TextInput()

# initialize screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Guru's Turkeys")
done = False

def startscreen(donee):
    global name
    done = donee
    # gameloop
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            name = textinput.get_text()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    if 410<mouse_pos[0]<615 and 450<mouse_pos[1]<550:
                        print('play button clicked')
                        done = True
    
        screen.fill((173, 216, 230))
        #turkeys
        turkey = pygame.transform.scale(get_image('turkey.png'), (240, 200))
        screen.blit(turkey, (20, 20))
        screen.blit(turkey, (180, 600))
        screen.blit(turkey, (600, 600))
        screen.blit(turkey, (740, 20))
    
        #buttons
        button("Play", 410,450,205,100,white,gold,50)
        fb(400,360,220,90)
    
        # name
        text("Enter your name: ", 400, 250, 240, 50, 15)
        text("or", 490, 330, 50, 50, 15)
        textinput.update(events)
        screen.blit(textinput.get_surface(), (450, 300))
        
        pygame.display.flip()
        #clock.tick(60)
        
        
if __name__ == '__main__':
    startscreen(False)
