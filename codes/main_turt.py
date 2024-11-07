try:
    import turtle
    import random
    from icecream import ic
except ImportError:
    print("missing imports")
    raise SystemExit
    
turtle.colormode(255)
scr = turtle.Screen()
turtle.register_shape("assets/player.gif")

class entity:
    def __init__(self):
        pass
    class player:
        def __init__(self):
            self.t = turtle.Turtle("assets/player.gif")
            self.shape1 = "assets/player.gif"
            self.shape2 = "assets/player_modle2.gif"
        def forwa(self):
            self.t.forward(1)
        def back(self):
            self.t.back(1)
        def right(self):
            self.t.right(45)
        def left(self):
            self.t.left(45)
        
    class enemy:
        def __init__(self,mengde):
            self.t = []
            self.mengde = mengde
            for i in range(mengde):
                self.t.append(turtle.Turtle("classic"))
                self.t[i].color(random.randint(1,255),random.randint(1,255),random.randint(1,255))

        
        def enemy(self):
            for i in range(self.mengde):
                ic(i)
                dire = random.randint(1,4)
                num = random.randint(1,50)
                if dire == 1:
                    for j in range(num):
                        self.t[i].forward(1)
                
                elif dire == 2:
                    for j in range(num):
                        self.t[i].back(1)

                elif dire == 3:
                    self.t[i].left(num)
                
                elif dire == 4:
                    self.t[i].right(num)

def mainloop():
    scr = turtle.Screen()
    enemy = entity.enemy(3)
    player = entity.player()
    while True:
        scr.onkeypress(player.forwa,'w');scr.onkeypress(player.forwa, 'Up')
        scr.onkeypress(player.back, 's');scr.onkeypress(player.back, 'Down')
        scr.onkeypress(player.left, 'a');scr.onkeypress(player.left, 'Left')
        scr.onkeypress(player.right,'d');scr.onkeypress(player.right, 'Right')
        scr.listen()
        enemy.enemy()
        scr.update()

if __name__ == "__main__":
    mainloop()