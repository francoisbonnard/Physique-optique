# lens.py

import pygame

class Lens:
    def __init__(self, x, screen_height):
        self.x = x
        self.height = 240
        self.arrow_size = 10
        self.color = (255, 255, 255)  # Blanc pour la lentille
        self.screen_height = screen_height

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.screen_height // 2 - self.height // 2), 
                         (self.x, self.screen_height // 2 + self.height // 2))
        pygame.draw.polygon(screen, self.color, [(self.x, self.screen_height // 2 - self.height // 2),
                                                (self.x - self.arrow_size, self.screen_height // 2 - self.height // 2 + self.arrow_size),
                                                (self.x + self.arrow_size, self.screen_height // 2 - self.height // 2 + self.arrow_size)])
        pygame.draw.polygon(screen, self.color, [(self.x, self.screen_height // 2 + self.height // 2),
                                                (self.x - self.arrow_size, self.screen_height // 2 + self.height // 2 - self.arrow_size),
                                                (self.x + self.arrow_size, self.screen_height // 2 + self.height // 2 - self.arrow_size)])
