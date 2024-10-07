import pygame, random, time
from icecream import ic

pygame.init()


def screen_maker():
    scr = pygame.display.set_mode((800, 800))
    return scr


def player(scr, pos_x, pos_y):
    pygame.draw.rect(scr, "red", (pos_x, pos_y, 20, 20))


def tresure(scr, x, y):
    pygame.draw.rect(scr, (0, 0, 255), (x, y, 20, 20))


def event_handler(event, scr):
    keys = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
        return "Q"

    if keys[pygame.K_a]:
        return "PLAYER_LEFT"
    if keys[pygame.K_d]:
        return "PLAYER_RIGHT"

    if keys[pygame.K_w]:
        return "PLAYER_UP"
    if keys[pygame.K_s]:
        return "PLAYER_DOWN"


def main_loop(scr):
    RUN = True
    play_x, play_y = 50, 20
    tresure_x, tresure_y = random.randint(50, 780), random.randint(50, 780)
    player(scr, play_x, play_y)
    while RUN:

        scr.fill((0, 255, 0))

        ev = pygame.event.wait()

        ev_r = event_handler(ev, scr)

        tresure(scr, tresure_x, tresure_y)

        if ev_r == "PLAYER_LEFT":
            play_x -= 1

        if ev_r == "PLAYER_RIGHT":
            play_x += 1

        if ev_r == "PLAYER_UP":
            play_y -= 1

        if ev_r == "PLAYER_DOWN":
            play_y += 1

        if ev_r == "Q":
            RUN = False

        player(scr, play_x, play_y)
        pygame.display.flip()


main_loop(screen_maker())
pygame.quit()
