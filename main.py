import pygame

#initialization
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))

#title
pygame.display.set_caption("game")

#game loop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

