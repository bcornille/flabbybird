import pygame, sys, pygame.locals
pygame.init()
winsize = (800, 450)
window=pygame.display.set_mode(winsize, 0, 32)
pygame.display.set_caption("Flabbybird")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

tree = pygame.image.load('pyne_icon_small.png').convert()
tree = pygame.transform.scale(tree, (90, 77))
#tree = pygame.transform.threshold(tree, tree, BLACK, threshold = (0,0,0,0), diff_color = (0,0,0,0), change_return = 2)

rects={'tree': tree.get_rect()}

while True:
    dy = 0
    for event in pygame.event.get():
        if event.type==pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            dy = 10

    for rect in rects:
        rects[rect].right += 2
        rects[rect].top += 1 - dy
        if rects[rect].right > winsize[0]:
            rects[rect].topleft=(0, 0)

    window.fill(WHITE)
    window.blit(tree, rects['tree'])
    pygame.time.Clock().tick(60)
    pygame.display.update()
