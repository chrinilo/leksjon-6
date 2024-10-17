import pygame
import random
from icecream import ic

dumb_thing = 1
pygame.init()
ic(dumb_thing)
scre = pygame.display.set_mode((800, 800))


class entety:
    def __init__(self, scre) -> None:
        self.scr = scre
        self.x = 20
        self.y = 20  # størlse for ting når de er bokser

    def player(self, pos_x, pos_y):
        pygame.draw.rect(self.scr, "red", (pos_x, pos_y, self.x, self.y))

    def tresure(self, x, y):
        pygame.draw.rect(self.scr, (0, 0, 255), (x, y, self.x, self.y))


def event_handler(event, scr):
    if event.type == pygame.QUIT:
        return "Q"

def main_loop(scr):
    RUN = True
    # play_x, play_y = 50, 20
    ent = entety(scr)
    tresure_x, tresure_y = random.randint(50, 780), random.randint(50, 780)
    # ent.player(play_x, play_y)

    while RUN:
        keys = pygame.key.get_pressed()
        scr.fill((0, 255, 0))
        ev = pygame.event.wait()
        ev_r = event_handler(ev, scr)



        ent.tresure(tresure_x, tresure_y)



        if ev_r == "Q":
            RUN = False



        # ent.player(play_x, play_y)
        pygame.display.flip()


main_loop(scre)
pygame.quit()
