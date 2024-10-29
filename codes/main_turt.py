import turtle
import random

class entity:
    def __init__(self):
        self.t = turtle.Turtle()
    class player:
        pass
    class enemy:
        def __init__(self):
            t = [turtle.Turtle(),turtle.Turtle(),turtle.Turtle]
        def enemy_1():
            pass

class movement:
    def __init__(self,chris):
        self.t = chris
    def forward(self, n):
        print("forward")
        self.t.forward(n)
    def backward(self, n):
        print("back")
        self.t.backward(n)
    def right(self, n):
        print("right")
        self.t.right(n)
    def left(self, n):
        print("left")
        self.t.left(n)

def mainloop():
    m = movement(chris)
    num = int()
    direction = [m.forward,m.backward,m.left,m.right]
    while True:
        try:
            direction_num = int(input(" hvilken retting(0:fram, 2:bak, 3:venstre, 4:høyre): "))
            num = int(input("lengde:\t"))
        except ValueError:
            print("NAN")
        direction[direction_num](num)
        pass
