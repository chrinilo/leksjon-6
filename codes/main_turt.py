import turtle
import random

scr = turtle.Screen()


class entity:
    def __init__(self):
        pass
    class player:
        def __init__(self):
            self.t = turtle.Turtle("assets/player.png")
        
        def forward():
            pass
        
    class enemy:
        def __init__(self):
            self.t = [turtle.Turtle(),turtle.Turtle(),turtle.Turtle]
        def enemy_1():
            pass
def thing():
    print("AAAAAaaaaaa~~~")
def mainloop():
    scr = turtle.Screen()
    t = turtle.Turtle()
    while True:
        scr.onkeypress(thing, 'a')
        scr.listen()

if __name__ == "__main__":
    mainloop()