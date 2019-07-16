import sys
import os
import pygame
from fruit import Fruit
from snake import Snake
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen_size = screen_width, screen_height = 820, 820
black = 0, 0, 0
white = 255, 255, 255
speed = [0, 0]

screen = pygame.display.set_mode(screen_size)
fruit = Fruit(screen_width, screen_height)
fruit_rect = fruit.get_rect()
snake = Snake(screen_width, screen_height)
snake_body = snake.get_body()
fruit_eaten = False
eaten_fruit_position = 0, 0

def check_boundaries(head):
    if head.left < 0 or head.right > screen_width or head.top < 0 or head.bottom > screen_height:
        sys.exit()

def check_bodyhead_collision(body):
    if body[0].collidelist(body[1:]) != -1:
        sys.exit()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_RIGHT:
                snake.set_speed([20, 0])
            if event.key == pygame.K_LEFT:
                snake.set_speed([-20, 0])
            if event.key == pygame.K_DOWN:
                snake.set_speed([0, 20])
            if event.key == pygame.K_UP:
                snake.set_speed([0, -20])

    if pygame.key.get_focused():
        snake.move_head()
        check_bodyhead_collision(snake_body)
        snake.move_body()
        screen.fill(black)
        check_boundaries(snake_body[0])
        pygame.draw.rect(screen, fruit.color, fruit_rect)
        for i in range(snake.body_size):
            pygame.draw.rect(screen, snake.color, snake_body[i])

        if snake_body[0].colliderect(fruit_rect):
            fruit_eaten = True
            eaten_fruit_position = fruit_rect.x, fruit_rect.y
            fruit_rect = fruit.change_pos(screen_width, screen_height)

        if fruit_eaten and (snake_body[-1].x, snake_body[-1].y) == eaten_fruit_position:
            snake.add_body(eaten_fruit_position)
            snake_body = snake.get_body()
            fruit_eaten = False

        pygame.display.flip()
        pygame.time.delay(100)
