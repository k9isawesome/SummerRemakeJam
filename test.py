# import the pygame module, so you can use it
import pygame
import random


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("assets/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240, 180))

    # load top grass blocks
    grassTop = pygame.image.load("assets/GrassTop.png").convert()
    grassTopRock = pygame.image.load("assets/GrassTopRock.png").convert()

    # draw grass blocks and update screen
    for i in range(0, 241, 16):
        if random.randint(0,3) == 0:
            screen.blit(grassTopRock, (i, 164))
        else:
            screen.blit(grassTop, (i, 164))
    pygame.display.update()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()