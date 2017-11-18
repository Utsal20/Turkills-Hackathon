import pygame
import os

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

def button(msg,x,y,w,h,color,hc):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hc, (x, y, w, h))
        if click[0] == 1:
            print("Clicked")
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/ 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


# initialize screen
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Guru's Turkeys")
done = False

# gameloop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        screen.fill((222, 184, 135))
        #turkeys
        turkey = pygame.transform.scale(get_image('turkey.png'), (240, 200))
        screen.blit(turkey, (20, 20))
        screen.blit(turkey, (180, 600))
        screen.blit(turkey, (600, 600))
        screen.blit(turkey, (740, 20))

        #button
        button("Play", 410,350,205,100,white,gold)
    pygame.display.flip()
    # os.clock.tick(60)