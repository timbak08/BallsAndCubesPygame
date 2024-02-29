import pygame as pg
import random
import pygame.mixer

pg.init()
pg.font.init()


def game():
    WIDTH = 800
    HEIGHT = 480

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    FPS = 60

    temnaya_tema = True

    PLATFORM_WIDTH = 100
    PLATFORM_HEIGHT = 15
    PLATFORM_SPEED = 10
    platform_rect = pg.rect.Rect(WIDTH / 2 - PLATFORM_WIDTH / 2,
                                 HEIGHT - PLATFORM_HEIGHT * 2,
                                 PLATFORM_WIDTH,
                                 PLATFORM_HEIGHT)

    CIRCLE_RADIUS = 15
    CIRCLE_SPEED = 10
    circle_first_collide = False
    circle_x_speed = 0
    circle_y_speed = CIRCLE_SPEED
    circle_rect = pg.rect.Rect(WIDTH / 2 - CIRCLE_RADIUS,
                               HEIGHT / 2 - CIRCLE_RADIUS,
                               CIRCLE_RADIUS * 2,
                               CIRCLE_RADIUS * 2)

    score = 0

    font = pg.font.match_font('monserrat')
    font_48 = pg.font.Font(font, 48)
    font_36 = pg.font.Font(font, 36)

    sound_pong = pygame.mixer.Sound('sounds/pong.mp3')
    sound_fail = pygame.mixer.Sound('sounds/fail.mp3')

    size = (WIDTH, HEIGHT)

    screen = pg.display.set_mode(size)
    pg.display.set_caption('pong by timbak')

    clock = pg.time.Clock()

    running = True
    game_over = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                continue
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    continue
                elif event.key == pg.K_SPACE:
                    game_over = False

                    circle_rect.center = [WIDTH / 2, HEIGHT / 2]
                    circle_x_speed = 0
                    circle_y_speed = CIRCLE_SPEED
                    circle_first_collide = False

                    platform_rect.centerx = WIDTH / 2
                    platform_rect.bottom = HEIGHT - PLATFORM_HEIGHT

                    score = 0

        screen.fill(BLACK if temnaya_tema else WHITE)

        if not game_over:
            keys = pg.key.get_pressed()

            if keys[pg.K_a] or keys[pg.K_LEFT]:
                platform_rect.x -= PLATFORM_SPEED
            elif keys[pg.K_d] or keys[pg.K_RIGHT]:
                platform_rect.x += PLATFORM_SPEED

            if platform_rect.colliderect(circle_rect):
                sound_pong.play()
                if not circle_first_collide:
                    if random.randint(0, 1) == 0:
                        circle_x_speed = -CIRCLE_SPEED
                    else:
                        circle_x_speed = CIRCLE_SPEED

                    circle_first_collide = True

                circle_y_speed = -CIRCLE_SPEED

                score += 1

            pg.draw.rect(screen, WHITE if temnaya_tema else BLACK, platform_rect)

        circle_rect.x += circle_x_speed
        circle_rect.y += circle_y_speed

        if circle_rect.bottom >= HEIGHT:
            game_over = True
            sound_fail.play()
            circle_y_speed = -CIRCLE_SPEED
        elif circle_rect.top <= 0:
            circle_y_speed = CIRCLE_SPEED
        elif circle_rect.right >= WIDTH:
            circle_x_speed = -CIRCLE_SPEED
        elif circle_rect.left <= 0:
            circle_x_speed = CIRCLE_SPEED

        pg.draw.circle(screen, WHITE if temnaya_tema else BLACK, circle_rect.center, CIRCLE_RADIUS)

        score_surface = font_48.render(str(score), True, WHITE if temnaya_tema else BLACK)
        if not game_over:
            screen.blit(score_surface, [WIDTH / 2 - score_surface.get_width() / 2, 10])
        else:
            screen.blit(score_surface,
                        [WIDTH / 2 - score_surface.get_width() / 2, HEIGHT / 3])
            retry_surface = font_36.render('нажмите ПРОБЕЛ для рестарта', True, WHITE if temnaya_tema else BLACK)
            screen.blit(retry_surface,
                        [WIDTH / 2 - retry_surface.get_width() / 2,
                         HEIGHT / 3 + score_surface.get_height()])
        clock.tick(FPS)
        pg.display.flip()