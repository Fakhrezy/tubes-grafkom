import pygame
from pygame.locals import *
from math import pi, cos, sin

def draw_tree(surface, scale=1.0):
    brown_color = (128, 82, 0)  # Warna coklat untuk batang pohon
    green_color = (0, 128, 0)  # Warna hijau untuk daun pohon

    # Create oval-shaped trunk
    pygame.draw.polygon(surface, brown_color, [(scale * cos(2.0 * pi * i / 100), -0.3 * scale + 0.1 * scale * sin(2.0 * pi * i / 100)) for i in range(101)])

    # Create circular-shaped leaves
    pygame.draw.circle(surface, green_color, (0, int(0.1 * scale)), int(0.1 * scale))

def main():
    pygame.init()

    width, height = 800, 600
    scale = 50.0  # You can adjust the scale factor here

    screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Oval-shaped Tree Trunk")

    glOrtho(-width / 200.0, width / 200.0, -height / 200.0, height / 200.0, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        draw_tree(screen, scale)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
