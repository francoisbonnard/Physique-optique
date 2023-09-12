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

def draw_arrow(screen, x, y, color, direction="up"):
    """Dessiner une flèche à la position (x, y) avec la couleur spécifiée."""
    if direction == "up":
        pygame.draw.polygon(screen, color, [(x, y), (x - 10, y + 10), (x + 10, y + 10)])
    else:
        pygame.draw.polygon(screen, color, [(x, y), (x - 10, y - 10), (x + 10, y - 10)])


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


        lenses = sorted(lenses, key=lambda l: l.x)

        for lens in lenses:
            lens.draw(screen)

        for obj in vertical_objects:
            obj.draw(screen)
            direction = "down" if obj.height < 0 else "up"
            draw_arrow(screen, obj.x, HEIGHT//2 - obj.height, (255, 255, 0), direction=direction)  # Flèche pour l'objet

            # Transformer l'objet à travers chaque lentille pour obtenir la position et la hauteur finales de l'image
            final_image_position = obj.x
            final_image_height = obj.height

            for lens in lenses:
                final_image_position, final_image_height = lens.transform_object(final_image_position, final_image_height)

            direction = "down" if final_image_height < 0 else "up"
            pygame.draw.line(screen, (0, 0, 255), (final_image_position, HEIGHT//2), (final_image_position, HEIGHT//2 - final_image_height), 2)  # Bleu pour l'image finale
            draw_arrow(screen, final_image_position, HEIGHT//2 - final_image_height, (0, 0, 255), direction=direction)  # Flèche pour l'image

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
