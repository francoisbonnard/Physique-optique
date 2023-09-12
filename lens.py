import pygame
import random

class Lens:
    def __init__(self, x, screen_height, lens_height=80, focal_length=100):
        self.x = x
        self.screen_height = screen_height
        self.lens_height = lens_height
        self.focal_length = focal_length  # La distance focale initiale est de 100 pixels.
        self.color = self._random_color()  # Chaque lentille reçoit une couleur aléatoire.

    def _random_color(self):
        """Retourne une couleur RGB aléatoire."""
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def draw(self, screen):
        half_height = self.lens_height // 2
        pygame.draw.line(screen, self.color, (self.x, self.screen_height//2 - half_height), (self.x, self.screen_height//2 + half_height), 2)
        
        # Fleches avec la couleur de la lentille
        pygame.draw.polygon(screen, self.color, [(self.x, self.screen_height//2 - half_height), (self.x - 10, self.screen_height//2 - half_height + 10), (self.x + 10, self.screen_height//2 - half_height + 10)])
        pygame.draw.polygon(screen, self.color, [(self.x, self.screen_height//2 + half_height), (self.x - 10, self.screen_height//2 + half_height - 10), (self.x + 10, self.screen_height//2 + half_height - 10)])
        
        # Dessiner le point focal avec la couleur de la lentille
        pygame.draw.circle(screen, self.color, (self.x + self.focal_length, self.screen_height//2), 5)
        pygame.draw.circle(screen, self.color, (self.x - self.focal_length, self.screen_height//2), 5)

    def adjust_focal_length(self, increment=True):
        if increment:
            self.focal_length += 40
        else:
            self.focal_length -= 40

    def get_image_properties(self, object_position, object_height):
        """Calcule la position et la hauteur de l'image formée par l'objet à travers cette lentille."""
        u = self.x - object_position
        f = self.focal_length
        v_inv = (1/f) + (1/u)
        v = 1/v_inv
        image_position = self.x + v
        m = -v/u
        image_height = m * object_height
        return image_position, image_height

    def transform_object(self, object_position, object_height):
        """Mise à jour de la position et de la hauteur de l'objet en passant par cette lentille."""
        image_position, image_height = self.get_image_properties(object_position, object_height)
        return image_position, image_height
