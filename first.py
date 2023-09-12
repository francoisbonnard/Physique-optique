import pygame
import sys

from lens import Lens
from VerticalObject import VerticalObject
from grid_axes import draw_grid, draw_axes


# Initialisation de pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Repère orthonormé avec grille")

def main():

    lenses = []
    vertical_objects = []
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen, WIDTH, HEIGHT)
        draw_axes(screen, WIDTH, HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                # Vérifier si le clic est sur un objet vertical existant
                clicked_object = next((obj for obj in vertical_objects if abs(obj.x - x) <= 5), None)
                clicked_lens = next((l for l in lenses if abs(l.x - x) <= 5), None)
                
                if event.button == 1:  # Bouton gauche
                    if clicked_object:
                        clicked_object.adjust_height(increment=False)
                    elif clicked_lens:
                        clicked_lens.adjust_focal_length(increment=True)
                    else:
                        lenses.append(Lens(x, HEIGHT, lens_height=300))
                elif event.button == 3:  # Bouton droit
                    if clicked_object:
                        clicked_object.adjust_height(increment=True)
                    elif clicked_lens:
                        clicked_lens.adjust_focal_length(increment=False)
                    else:
                        vertical_objects.append(VerticalObject(x, HEIGHT))



        for lens in lenses:
            lens.draw(screen)

        for obj in vertical_objects:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
