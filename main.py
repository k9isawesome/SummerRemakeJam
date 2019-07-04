import pygame
import random

def load_images():
    image_dict = {'grass_top': pygame.image.load('assets/grass/grass_top.png'),
                  'grass_top_rock': pygame.image.load('assets/grass/grass_top_rock.png'),
                  'short_grass_1': pygame.image.load('assets/short_grass/short_grass_1.png'),
                  'short_grass_2': pygame.image.load('assets/short_grass/short_grass_2.png'),
                  'short_grass_3': pygame.image.load('assets/short_grass/short_grass_3.png'),
                  'short_grass_4': pygame.image.load('assets/short_grass/short_grass_4.png'),
                  'short_grass_5': pygame.image.load('assets/short_grass/short_grass_5.png'),
                  'trainer_rotating_1': pygame.image.load('assets/trainer_rotating/')}

def get_background()


def main():

    pygame.init()

    logo = pygame.image.load('assets/logo32x32.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Game Test")

    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()