import pygame, sys, pygame.locals
pygame.init()
winsize = (600, 600)
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
rects['tree'].topleft=((winsize[1]-90)/2, 0)

# Parameters to tweak
a = 0.3
vreset = -5

v = 0
while True:
#    dy = 0
    v += a
    for event in pygame.event.get():
        if event.type==pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            v = vreset
#            dy = 20

    for rect in rects:
#        rects[rect].right += 2
        rects[rect].top += v
        if rects[rect].bottom > winsize[1]:
            rects[rect].topleft=((winsize[1]-90)/2, 0)
            v = 0

    window.fill(WHITE)
    window.blit(tree, rects['tree'])
    pygame.time.Clock().tick(60)
    pygame.display.update()
