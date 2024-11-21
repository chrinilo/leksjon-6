# try:    #importrer biblioteker som brukes under debugging eller er nødvendige for at koden skal fungere
import turtle # gui lib
import random # tilfeldige tall
import time
# from icecream import ic #debugging 
# except ImportError: # hvis man mangler et eller flere lib's så skal denne koden kjøre
#     print("missing imports")
#     raise SystemExit # slutter koden så den ikke forsetter med all den andre koden

turtle.colormode(255) # lar turtle bruke RGB verdier
scr = turtle.Screen() # funksjonene som turtlen ikke skal gjøre
# turtle.register_shape("assets/player.gif") # skal legge til mere men denne legger til en gif fil til en form
class buttons:
    
    def __init__(self, *args):
        turtle.register_shape("./assets/buttons/menu_button.gif")
        self.map = ["assets/maps/map1.png","assets/maps/map2.gif","assets/maps/map3.gif"]
        self.tersure = turtle.Turtle();self.tersure.penup();self.tersure.hideturtle()
        # koden over lager turtle, gjemmer turtle og tar pennen opp
        self.player = ["assets/player.gif","assets/player_modle2.gif"]
        self.scr = args[0]#screen
        
        
    def maps(self,x):
        
        if x == 1:
            self.scr.bgpic(self.map[0])
            self.tersure.setpos(-189.00,-111.53)
            return 
        if x == 2:
            self.scr.bgpic(self.map[1])
            self.tersure.setpos(191.68,-225.03)
        if x == 3:
            self.scr.bgpic(self.map[2])

class entity:
    class player: # lager spilleren 
        def __init__(self): #lager avriablene som skal bli brukt i klassen
            self.t = turtle.Turtle()
            self.shape1 = "assets/player.gif"
            self.shape2 = "assets/player_modle2.gif"
            self.t.ht()
            self.t.pu()
            self.t.setpos((-80,130)) #
            self.t.pd()
            self.t.st()
            # self.t.shapesize(0.4,0.4)

        def forwa(self): # alle rettningen for turtlen å gå
            self.t.forward(1)

        def back(self):
            self.t.back(1)

        def right(self):
            self.t.right(30)

        def left(self):
            self.t.left(30)

    class enemy: # lager finden(e)
        def __init__(self,mengde):
            self.t = []
            self.mengde = mengde
            for i in range(mengde): # lager alle turtlene til finde klassen og lagrer dem i en liste
                self.t.append(turtle.Turtle("classic"))
                self.t[i].color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
                self.t[i].ht();self.t[i].pu() # gjemmer og tar penn opp
                self.t[i].setpos(random.randint(-200,200), random.randint(-200,200)) #
                self.t[i].pd();self.t[i].st() # gjør det motsatte av 
                self.t[i].speed(1)

        def enemy(self): # koden som faktisk beveger på seg
            for i in range(self.mengde):
                dire = random.randint(1,4)      # hvilken retning som findene skal gå
                num = random.randint(1,10)      # hvor langt de skal gå
                if (dire == 1):                 # hvilken retning den fikk
                    for j in range(num):        # hvor mange den skal på fram 
                        self.t[i].forward(2)

                elif (dire == 2):
                    for j in range(num):
                        self.t[i].back(2)

                elif (dire == 3):
                    self.t[i].left(num)

                elif (dire == 4):
                    self.t[i].right(num)

def mainloop_(scr): # main loop som har alle tingene som skal repitere i lokale variabler og henter resten av klassene
    scr.tracer(0) 
    but = buttons(scr)
    scr = turtle.Screen()
    enemy = entity.enemy(1)
    player = entity.player()
    
    try:but.maps(int(scr.numinput("map", "which map do you want to play. (1,2,3)")))
    except TypeError:print("wright a number between 1 and 3")
    scr.onkeypress(player.forwa,'w');scr.onkeypress(player.forwa, 'Up')
    scr.onkeypress(player.back, 's');scr.onkeypress(player.back,  'Down')
    scr.onkeypress(player.left, 'a');scr.onkeypress(player.left,  'Left')
    scr.onkeypress(player.right,'d');scr.onkeypress(player.right, 'Right')
    while (True):
        time.sleep(1/30)
        scr.listen()
        enemy.enemy()
        scr.update()
        print(player.t.pos())

        for i in turtle.turtles():
            
            if (i == player.t and i.distance(but.tersure)<=15):
                print("win")
            
            # if (i != player.t and i != but.tersure and i.distance(player.t)<=15):
            #     raise SystemExit
            
            if i.pos()[1] <= -355:
                i.penup()
                i.setpos(i.pos()[0],350)
                i.pendown()
            
            if i.pos()[1] >= 355:
                i.penup()
                i.setpos(i.pos()[0],-350)
                i.pendown()
            
            if i.pos()[0] <= -384:
                i.penup()
                i.setpos(382,i.pos()[1])
                i.pendown()
            
            if i.pos()[0] >= 384:
                i.penup()
                i.setpos(-382,i.pos()[1])
                i.pendown()

if __name__ == "__main__":
    mainloop_(scr)

