# import the pygame module, so you can use it
import pygame
import random


def load_images():
    image_dict = {}
    image_dict['grassTop'] = pygame.image.load("assets/grass/GrassTop.png").convert()
    image_dict['grassTopRock'] = pygame.image.load("assets/grass/GrassTopRock.png").convert()
    image_dict['trainer'] = pygame.image.load("assets/trainer.png").convert()
    return image_dict

def draw_background(screen, image_dict):

    grass_top = image_dict['grass_top']
    grass_top_rock = image_dict['grass_top_rock']

    # draw grass blocks and update screen
    for i in range(0, 241, 16):
        if random.randint(0, 3) == 0:
            screen.blit(grass_top_rock, (i, 164))
        else:
            screen.blit(grass_top, (i, 164))
    pygame.display.update()

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("assets/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("test program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240, 180))

    # load images
    imageDict = load_images()

    # draw background
    draw_background(screen, imageDict)

    # draw trainer
    trainer_pos_x = 0
    trainer_pos_y = 0
    screen.blit(imageDict['trainer'], (trainer_pos_x, trainer_pos_y))
    pygame.display.flip()

    gravity = 20
    move_speed = 10

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

        # draw/update player position
        trainer_pos_y += gravity
        if trainer_pos_y > 132:
            trainer_pos_y = 132
        screen.blit(imageDict['trainer'], (trainer_pos_x, trainer_pos_y))

        pygame.display.flip()

    pygame.quit()



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()