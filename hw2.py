import pygame, sys, pygame.locals#1
pygame.init()#2
window=pygame.display.set_mode((500, 400), 0, 32)#3
pygame.display.set_caption("Paint")#4
BLACK = (0, 0, 0)#5
WHITE = (255, 255, 255)#6
RED = (255, 0, 0)#7
GREEN = (0, 255, 0)#8
BLUE = (0, 0, 255)#9

triangle=pygame.Surface((150, 200))#14
triangle.fill((0, 0, 0))#15
pygame.draw.polygon(triangle, RED, ((70, 0), (150, 200), (0, 50)))#16
triangle.set_colorkey((0, 0, 0))#17

rects={'triangle': triangle.get_rect()}#24

while True:#29
    for event in pygame.event.get():#30
        if event.type==pygame.locals.QUIT:#31
            pygame.quit()#32
            sys.exit()#33
    for rect in rects:#34
        rects[rect].right+=1#35
        if rects[rect].right>500:#36
            rects[rect].topleft=(0, 0)#44
    window.fill(WHITE)#45
    window.blit(triangle, rects['triangle'])#47
    pygame.time.Clock().tick(40)#50
    pygame.display.update()#51
