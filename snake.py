import pygame

class Snake:
    def __init__(self, screen_width, screen_height):
        self.color = 255, 255, 255
        self.speed = [0, 0]
        self.size = 20, 20
        self.head_position = screen_width/2, screen_height/2
        self.body = [pygame.Rect((0, 0), self.size)]
        self.body[0].center = self.head_position
        self.body_size = 1

    def set_speed(self, new_speed):
        self.speed = new_speed

    def move_body(self):
        for i in range(self.body_size - 1, 1, -1):
            self.body[i].x, self.body[i].y = self.body[i-1].x, self.body[i-1].y
        if self.body_size > 1:
            self.body[1].x, self.body[1].y = self.head_position

    def move_head(self):
        self.head_position = self.body[0].x, self.body[0].y
        self.body[0].move_ip(self.speed)

    def add_body(self, position):
        self.body.append(pygame.Rect(position, self.size))
        self.body_size += 1

    def get_body(self):
        return self.body

    def get_body_coords(self):
        coords = []
        for body_rect in self.body:
            coords.append((body_rect.x, body_rect.y))
        return coords


    

