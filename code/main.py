import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load('../images/icon.png'))
my_font = pygame.font.Font('../font/Pixeled.ttf', 40)
score_font = pygame.font.Font('../font/Pixeled.ttf', 10)
game_over = my_font.render('GAME OVER', False, 'White', )
score = score_font.render('SCORE: ', False, 'White')
restart = my_font.render('RESTART', False, 'Green', )
restart_rect = restart.get_rect(topleft=(140, 350))
background = pygame.image.load('../images/background.png').convert()

score_point_font = pygame.font.Font('../font/Pixeled.ttf', 10)
point = 0
score_point = score_point_font.render(str(point), False, 'White')


player_up = [
    pygame.image.load('../images/playerup1.png').convert_alpha(),
    pygame.image.load('../images/playerup2.png').convert_alpha(),
    pygame.image.load('../images/playerup3.png').convert_alpha(),
]
player_up_animation = 0
player_speed = 6
player_x = 275
player_y = 650

meteor_timer = pygame.USEREVENT + 1
pygame.time.set_timer(meteor_timer, 1000)
meteor = pygame.image.load('../images/meteor.png').convert_alpha()
meteor_y = 0
meteor_list = []

bullet = pygame.image.load('../images/bullet.png').convert_alpha()
bullets = []

gg = True
running = True
while running:

    screen.blit(background, (0, 0))
    screen.blit(player_up[player_up_animation], (player_x, player_y))
    screen.blit(score, (10, 0))

    if gg:

        player_rect = player_up[0].get_rect(topleft=(player_x, player_y))
        meteor_rect = meteor.get_rect(topleft=(250, meteor_y))
        screen.blit(score_point, (70, 0))

        if meteor_list:
            for (i, el) in enumerate(meteor_list):
                screen.blit(meteor, el)
                el.y += 8

                if el.y > 675:
                    meteor_list.pop(i)

                if player_rect.colliderect(el):
                    gg = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 5:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 565:
            player_x += player_speed

        if keys[pygame.K_UP] and player_y > 5:
            player_y -= player_speed
        elif keys[pygame.K_DOWN] and player_y < 665:
            player_y += player_speed

        if player_up_animation == 2:
            player_up_animation = 0
        else:
            player_up_animation += 1

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.y -= 8

                if el.y < 10:
                    bullets.pop(i)

                if meteor_list:
                    for (index, meteor_element) in enumerate(meteor_list):
                        if el.colliderect(meteor_element):
                            meteor_list.pop(index)
                            bullets.pop(index)

    else:
        screen.fill((87, 88, 89))
        screen.blit(game_over, (140, 250))
        screen.blit(restart, (140, 350))

        mouse = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gg = True
            player_x = 275
            player_y = 650
            meteor_list.clear()
            bullets.clear()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == meteor_timer:
            meteor_list.append(meteor.get_rect(topleft=(250, meteor_y)))
        if gg and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bullets.append(bullet.get_rect(topleft=(player_x, player_y)))

    clock.tick(30)