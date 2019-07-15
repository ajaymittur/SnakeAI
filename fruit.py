import random
import pygame

class Fruit:
    def __init__(self, screen_width, screen_height):
        self.color = 255, 8, 0
        self.size = self.width, self.height = 20, 20
        self.position = random.randrange(0, screen_width, self.width), random.randrange(0, screen_height, self.height)

    def get_pos(self):
        return self.position

    def change_pos(self, screen_width, screen_height):
        self.position = random.randrange(0, screen_width, self.width), random.randrange(0, screen_height, self.height)
    
    def get_rect(self):
        return pygame.Rect((self.position), (self.size))
