# Riaan's game

import pygame
import random
import time
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN


NUM_STARS = 1000
WHITE = (255,255,255)
BLACK = (0,0,0)
LEFT = 0
direction = 0
LIGHTGRAY = (180,180,180)
KEY_FACTOR = 10
def init_stars(screen):
    "Create the starfield"

    # The starfield is represented as a dictionary of x and y values.
    stars = []

    # Create a list of (x,y) coordinates.
    for loop in range(0, NUM_STARS):
        star = [random.randrange(0, screen.get_width() - 1),
                random.randrange(0, screen.get_height() - 1)]
        stars.append(star);

    return stars

def move_stars(screen, stars, start, end, direction):
    "Correct for stars hitting the screen's borders"

    for loop in range(start, end):
        if (direction == LEFT):
            if (stars[loop][0] != 1):
                stars[loop][0] = stars[loop][0] - 1
            else:
                stars[loop][1] = random.randrange(0, screen.get_height() - 1)
                stars[loop][0] = screen.get_width() - 1
        elif (direction == RIGHT):
            if (stars[loop][0] != screen.get_width() - 1):
                stars[loop][0] = stars[loop][0] + 1
            else:
                stars[loop][1] = r
                andom.randrange(0, screen.get_height() - 1)
                stars[loop][0] = 1

    return stars
# Initialize Pygame
pygame.init()

# Set up the game window dimensions
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Starfield")

screen.fill(BLACK)

# Create the starfield.
stars = init_stars(screen)

# Place ten white stars
for loop in range(0, NUM_STARS):
    screen.set_at(stars[loop], WHITE)
# spaceship.png
FACTOR = 0.7
image = pygame.image.load("spaceship.png").convert_alpha()
image = pygame.transform.scale(image, (180*FACTOR, 300*FACTOR))
image = pygame.transform.rotate(image, 270)
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2) # Center the image

rock_x, rock_y = screen_width // 2, screen_height // 2

#image.transform.rotate()
screen.blit(image, image_rect)
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            running = False
        elif (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                break
            elif (event.key == K_UP):
                rock_y = max(rock_y - KEY_FACTOR, 0)
            elif (event.key == K_DOWN):
                rock_y = min(rock_y + KEY_FACTOR, screen_height)

    # Drawing (optional: add drawing code here)
    # For example, to fill the background with white:
    # screen.fill((255, 255, 255)) # RGB for white
    screen.fill((0,0,0))


    # time.sleep(10)
    # Erase the first star field.
    for loop in range(0, NUM_STARS):
        screen.set_at(stars[loop], BLACK)

    # Check if first field's stars hit the screen border.
    stars = move_stars(screen, stars, 0, NUM_STARS, direction)

    # Place ten light gray stars.
    for loop in range(0, NUM_STARS):
        screen.set_at(stars[loop], WHITE)
    image_rect.center = (rock_x, rock_y)
    screen.blit(image, image_rect)
    # Update the display
    pygame.display.flip()

# Quit Pygame

pygame.quit()
