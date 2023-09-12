import pygame

GRID_COLOR = (100, 100, 100)  # Couleur plus discrète pour la grille
AXIS_COLOR = (150, 150, 150)  # Gris pour les axes
GRID_SPACING = 40  # Espacement entre chaque ligne de la grille

def draw_grid(screen, width, height):
    num_x_lines = width // GRID_SPACING
    num_y_lines = height // GRID_SPACING

    for i in range(num_x_lines + 1):
        x = width // 2 + i * GRID_SPACING
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, height))
        x = width // 2 - i * GRID_SPACING
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, height))

    for i in range(num_y_lines + 1):
        y = height // 2 + i * GRID_SPACING
        pygame.draw.line(screen, GRID_COLOR, (0, y), (width, y))
        y = height // 2 - i * GRID_SPACING
        pygame.draw.line(screen, GRID_COLOR, (0, y), (width, y))

def draw_axes(screen, width, height):
    pygame.draw.line(screen, AXIS_COLOR, (width // 2, 0), (width // 2, height), 2)
    pygame.draw.line(screen, AXIS_COLOR, (0, height // 2), (width, height // 2), 2)
