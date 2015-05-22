import pygame, sys, pygame.locals
pygame.init()
window=pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Flabbybird")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

triangle=pygame.Surface((150, 200))
triangle.fill((0, 0, 0))
pygame.draw.polygon(triangle, RED, ((70, 0), (150, 200), (0, 50)))
triangle.set_colorkey((0, 0, 0))

rects={'triangle': triangle.get_rect()}

while True:
    dy = 0
    for event in pygame.event.get():
        if event.type==pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            dy = 10

    for rect in rects:
        rects[rect].right += 1
        rects[rect].top += dy
        if rects[rect].right > 500:
            rects[rect].topleft=(0, 0)

    window.fill(WHITE)
    window.blit(triangle, rects['triangle'])
    pygame.time.Clock().tick(20)
    pygame.display.update()
