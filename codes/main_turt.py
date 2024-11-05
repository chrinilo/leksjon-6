import turtle
import random

scr = turtle.Screen()
turtle.register_shape("assets/player.gif")

class entity:
    def __init__(self):
        pass
    class player:
        def __init__(self):
            self.t = turtle.Turtle("assets/player.gif")
        
        def forward(self):
            self.t.forward(1)
        def back(self):
            self.t.back(1)
        def right(self):
            self.t.right(1)
        def left(self):
            self.t.left(1)
        
    class enemy:
        def __init__(self):
            self.t = [turtle.Turtle(),turtle.Turtle(),turtle.Turtle]
        def enemy_1():
            pass

def mainloop():
    scr = turtle.Screen()
    player = entity.player()
    while True:
        scr.onkeypress(player.forward, 'w')
        scr.onkeypress(player.back, 's')
        scr.onkeypress(player.left, 'a')
        scr.onkeypress(player.right, 'd')
        scr.onkeypress(player.forward, 'Up')
        scr.onkeypress(player.back, 'Down')
        scr.onkeypress(player.left, 'Left')
        scr.onkeypress(player.right, 'Right')
        scr.listen()
        scr.update()

if __name__ == "__main__":
    mainloop()