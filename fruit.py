import random
import pygame

class Fruit:
    def __init__(self, screen_width, screen_height):
        self.color = 255, 8, 0
        self.size = self.width, self.height = 20, 20
        self.position_x = random.randrange(0, screen_width, self.width) 
        self.position_y = random.randrange(0, screen_height, self.height)
        self.fruit_rect = pygame.Rect((0, 0), (self.size))

    def change_pos(self, screen_width, screen_height, snake_body_coords):
        self.position_x = random.randrange(0, screen_width, self.width)
        self.position_y = random.randrange(0, screen_height, self.height)

        # make sure fruit doesn't spawn in snake body
        if (self.position_x, self.position_y) in snake_body_coords:
            self.position_x = random.randrange(0, screen_width, self.width)
            self.position_y = random.randrange(0, screen_height, self.height)
        return self.get_rect()
    
    def get_rect(self):
        return self.fruit_rect.move([self.position_x, self.position_y])
