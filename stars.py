import pygame
import random
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT

# define colors here
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
TEAL=(0,255,255)
yellow=(254,254,0)
PURPLE=(166,0,255)

# make a list of colors called colors
colors = [BLACK, BLUE, RED, TEAL, yellow, PURPLE]

# initialize the game
pygame.init()

# Set up the game window dimensions
screen_width = 120*10
screen_height = 80*10
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window name
pygame.display.set_caption("cat")

# color the screen black
screen.fill(BLACK)


# load the image of the invader
FACTOR = 0.10
image = pygame.image.load("invader.png").convert_alpha()

# image = pygame.transform.scale(image, (180*FACTOR, 300*FACTOR))
image = pygame.transform.scale(image, (image.get_width()*FACTOR, image.get_height()*FACTOR))
image_rect = image.get_rect()
# put the invader in the center of the screen by dividing width and height by 2
rock_x, rock_y = (screen_width // 2, screen_height // 2) # Center the image
image_rect.center = rock_x, rock_y

screen.blit(image, image_rect)

stars = []

# define a star function to create stars
def init_stars(star_count):
    """
    Initialize stars
    """
    stars = []
    # for the numbers from 1 to star_count
    for ix in range(star_count):
        # set the x and y to a random number between 0 and screen width and 0 and screen height
        star = [random.randrange(0,screen.get_width()-1), random.randrange(0,screen.get_height()-1)]
        
        stars.append(star)
    return stars

# define add stars functions that puts the stars on the screen
def add_stars():
    screen.set_at([10,645], yellow)
    screen.set_at([11,641], yellow)
    screen.set_at([12,642], yellow)
    # print(len(stars))
    for ix in range(len(stars)):
        color_index = 5 # random.randrange(0, len(colors)-1)

        screen.set_at(stars[ix], colors[color_index])

# call the function and get 10,000 star positions    
stars = init_stars(10_000)

running = True

# Game loop - MOST important thing
while running:
    
    # handle all the keyboard presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            running = False
        elif (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                break
            # when UP key is pressed subtract 50 steps from the height value of the invader
            elif (event.key == K_UP):
                rock_y = rock_y - 50
            # when DOWN key is pressed add 50 steps from the height value of the invader
            elif (event.key == K_DOWN):
                rock_y = rock_y + 50
            
            # when LEFT key is pressed subtract 50 steps from the width value of the invader
            elif (event.key == K_LEFT):
                rock_x = rock_x - 50

            # when RIGHT key is pressed add 50 steps from the width value of the invader
            elif (event.key == K_RIGHT):
                rock_x = rock_x + 50

    

    # fill screen in black
    screen.fill(BLACK)

    # add stars to screen
    add_stars()
    
    # set the position of the invader
    image_rect.center = (rock_x, rock_y)
    screen.blit(image, image_rect)
    
    pygame.display.flip()

pygame.quit()
