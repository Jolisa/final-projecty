import pygame
#from PIL import Image
#im=Image.open("letter_e.jpg")

#surface=pygame.image.load("letter_e.jpg").convert()

from pygame.locals import*
#img= pygame.image.load("letter_e.jpg")
#image_surf = pygame.image.load("letter_e.jpg")
#display_surf.blit("letter_e.jpg",(100,300))


black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
turquoise=(40,200,120)
purple=(100, 40, 200)
pygame.init()
size=(700,500)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
eImg=pygame.image.load("letter_e.jpg")
done= False
x= 350
y=250
x_move=10
y_move=10
radius=10
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
    screen.fill(purple)
    screen.blit(eImg,(100,300))


    
    pygame.draw.circle(screen, turquoise, (x,y), radius)
    x+=x_move
    y+=y_move
    if y+ radius>=500:
        y_move*=-1
        y-=10
    if x+radius>=700:
        x_move*=-1
        x-=10
    if y-radius<=0:
        y_move*=-1
        y+=10
    if x-radius<=0:
        x_move*=-1
        x+=10



    pygame.display.flip()
    clock.tick(60)
pygame.quit()
exit()
        
