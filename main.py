import pygame
from button import Button
from funtions import load_image
from game import game


pygame.init()
WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
background = load_image('images/МЕНЮШКА.jpg')


def main_menu():
    new_game_button = Button(WIDTH/2 - (252/2), 150, 252, 74, "НОВAЯ ИГРА", 'images/knopka.png', WIDTH, 'sounds/click.mp3')
    settings_button = Button(WIDTH/2 - (252/2), 250, 252, 74, "НАСТРОЙКИ", 'images/knopka.png', WIDTH, 'sounds/click.mp3')
    exit_button = Button(WIDTH/2 - (252/2), 350, 252, 74, "ВЫЙТИ", 'images/knopka.png', WIDTH, 'sounds/click.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT and event.button == new_game_button:
                game()

            elif event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
            for btn in [new_game_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [new_game_button, settings_button, exit_button]:
            btn.hovered_checker(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
    pygame.quit()




def settings_menu():
    pass


main_menu()