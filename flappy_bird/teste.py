import pygame
import flappy_bird

background_color = 0, 215, 225

screen = pygame.display.set_mode((400, 600))

pygame.display.set_caption('Testando')

screen.fill(background_color)

pygame.display.flip()

running = True

flappy_bird.main()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()