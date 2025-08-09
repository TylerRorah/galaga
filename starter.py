import pygame
import os

# Initialize Pygame
pygame.init()

# Create the display surface (the window)
screen = pygame.display.set_mode((800, 1000))
running = True

# Other variables needed
clock = pygame.time.Clock()
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# load spaceship png
ship_surface = pygame.image.load(os.path.join('assets', 'images', 'small_galaga_spaceship.png'))

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # how we get the spaceship on the screen
    screen.blit(ship_surface, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()