# vertical_object.py

import pygame

class VerticalObject:
    def __init__(self, x, screen_height):
        self.x = x
        self.height = 80
        self.arrow_size = 10
        self.color = (255, 255, 0)  # Jaune
        self.screen_height = screen_height

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.screen_height // 2 - self.height), 
                         (self.x, self.screen_height // 2))
        pygame.draw.polygon(screen, self.color, [(self.x, self.screen_height // 2 - self.height),
                                                (self.x - self.arrow_size, self.screen_height // 2 - self.height + self.arrow_size),
                                                (self.x + self.arrow_size, self.screen_height // 2 - self.height + self.arrow_size)])

    def adjust_height(self, increment=True):
        if increment:
            self.height += 20
        else:
            self.height = max(0, self.height - 20)  # Ensure height is non-negative
