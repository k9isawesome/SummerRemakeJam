# import the pygame module, so you can use it
import pygame
import random

# gravity value
gravity = 2

# move_speed value
move_speed = 5

def load_images():
    image_dict = {}
    image_dict['grass_top'] = pygame.image.load("assets/grass/GrassTop.png").convert_alpha()
    image_dict['grass_top_rock'] = pygame.image.load("assets/grass/GrassTopRock.png").convert_alpha()
    image_dict['trainer'] = pygame.image.load("assets/trainer.png").convert_alpha()
    image_dict['bg'] = pygame.image.load("assets/bg.png").convert_alpha()
    image_dict['short_grass_1'] = pygame.image.load("assets/shortGrass/shortGrass1.png").convert_alpha()
    image_dict['short_grass_2'] = pygame.image.load("assets/shortGrass/shortGrass2.png").convert_alpha()
    image_dict['short_grass_3'] = pygame.image.load("assets/shortGrass/shortGrass3.png").convert_alpha()
    image_dict['short_grass_4'] = pygame.image.load("assets/shortGrass/shortGrass4.png").convert_alpha()
    image_dict['short_grass_5'] = pygame.image.load("assets/shortGrass/shortGrass5.png").convert_alpha()
    return image_dict


def draw_foreground(screen, image_dict):

    grass_top = image_dict['grass_top']
    grass_top_rock = image_dict['grass_top_rock']
    short_grass_1 = image_dict['short_grass_1']
    short_grass_2 = image_dict['short_grass_2']
    short_grass_3 = image_dict['short_grass_3']
    short_grass_4 = image_dict['short_grass_4']
    short_grass_5 = image_dict['short_grass_5']

    # draw grass blocks and update screen
    for i in range(0, 241, 16):
        if random.randint(0, 3) == 0:
            screen.blit(grass_top_rock, (i, 164))
        else:
            screen.blit(grass_top, (i, 164))
        if random.randint(0,2) == 0:
            random_grass = random.randint(0,4)
            if random_grass == 0:
                screen.blit(short_grass_1, (i, 148))
            elif random_grass == 1:
                screen.blit(short_grass_2, (i, 148))
            elif random_grass == 2:
                screen.blit(short_grass_3, (i, 148))
            elif random_grass == 3:
                screen.blit(short_grass_4, (i, 148))
            elif random_grass == 4:
                screen.blit(short_grass_5, (i, 148))
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
    screen = pygame.display.set_mode((480, 360))

    # set up clock for stable framerate
    clock = pygame.time.Clock()

    # load images
    image_dict = load_images()

    # draw background
    screen.blit(image_dict['bg'], (0, 0))

    # draw foreground
    draw_foreground(screen, image_dict)

    # initialize trainer position
    trainer_pos_x = 0
    trainer_pos_y = 0

    # initialize trainer vertical velocity
    trainer_velocity_y = 0

    # initiazlie trainer in air status
    trainer_in_air = True

    # define a variable to control the main loop
    running = True

    # main loop
    while running:

        # erase trainer position
        trainer_rect = pygame.Rect(trainer_pos_x, trainer_pos_y, 32, 32)
        screen.blit(image_dict['bg'], trainer_rect, trainer_rect)

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keys = pygame.key.get_pressed()

        # update trainer position based on key press
        if keys[pygame.K_d]:
            trainer_pos_x += move_speed
        if keys[pygame.K_a]:
            trainer_pos_x -= move_speed
        if keys[pygame.K_w]:
            if not trainer_in_air:
                trainer_velocity_y = -10

        # apply gravity to trainer position
        trainer_pos_y += trainer_velocity_y

        if trainer_in_air:
            trainer_velocity_y += gravity

        if trainer_pos_y > 132:
            trainer_in_air = False
            trainer_pos_y = 132
        else:
            trainer_in_air = True

        # draw new trainer position
        screen.blit(image_dict['trainer'], (trainer_pos_x, trainer_pos_y))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()