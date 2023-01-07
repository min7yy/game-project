import pygame
import os
import sys


def main():
    # initialization
    pygame.init()

    # creating the screen
    screen_resolution = 800, 600
    screen = pygame.display.set_mode(screen_resolution, pygame.RESIZABLE)

    # title
    pygame.display.set_caption("Game Project")

    background_image = pygame.image.load(resource_path(os.path.join("assets", "background.png"))).convert()

    screen.blit(pygame.transform.scale(background_image, screen_resolution), background_image.get_rect())

    # game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                # Dynamically scale background image when resizing the window
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                screen.blit(pygame.transform.scale(background_image, event.dict['size']), (0, 0))
                pygame.display.flip()

        pygame.display.update()


# Helps load resources when project is compiled
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
