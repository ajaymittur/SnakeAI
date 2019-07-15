import sys
import os
import pygame
from fruit import Fruit
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen_size = screen_width, screen_height = 820, 820
black = 0, 0, 0
white = 255, 255, 255
speed = [0, 0]
fruit = Fruit(screen_width, screen_height)
fruit_rect = fruit.get_rect()
print(fruit_rect)

screen = pygame.display.set_mode(screen_size)
rect = pygame.Rect(0, 0, 20, 20)
rect.center = screen_width/2, screen_height/2

def check_boundaries(rect):
    if rect.left < 0 or rect.right > screen_width or rect.top < 0 or rect.bottom > screen_height:
        pygame.event.clear()
        pygame.event.post(pygame.event.QUIT)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.clear()
                pygame.event.post(pygame.event.QUIT)

            if event.key == pygame.K_RIGHT:
                speed = [20, 0]
            if event.key == pygame.K_LEFT:
                speed = [-20, 0]
            if event.key == pygame.K_DOWN:
                speed = [0, 20]
            if event.key == pygame.K_UP:
                speed = [0, -20]

    if pygame.key.get_focused():
        screen.fill(black)
        check_boundaries(rect)
        pygame.draw.rect(screen, fruit.color, fruit_rect)
        pygame.draw.rect(screen, white, rect)
        rect.move_ip(speed)


        if rect.colliderect(fruit_rect):
            fruit.change_pos(screen_width, screen_height)
            fruit_rect = fruit.get_rect()

        pygame.display.flip()
        pygame.time.delay(100)
