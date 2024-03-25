import pygame
from time import sleep
from drawPiano import draw_piano
from drawPiano import get_notes

WIDTH = 1000
HEIGHT = 700
MARGINE_H = 50
MARGINE_V = 200
FPS = 30


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('ListenUp!')

running = True
notes = get_notes()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((125, 40, 170))

    keys = draw_piano(screen, notes, margines=(MARGINE_H, MARGINE_V))

    pygame.display.flip()

pygame.quit()
