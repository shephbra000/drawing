import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")


CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
display_surface.fill(YELLOW)
CENTER = (300, 300)
RADIUS = 100
START = (100, 100)
END = (500, 500)




TOP_LEFT_X = 130
TOP_LEFT_Y =150
WIDTH = 350
HEIGHT = 400
DATA = (TOP_LEFT_X, TOP_LEFT_Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, CYAN, DATA)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.draw.circle
pygame.quit()