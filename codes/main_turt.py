try:    #importrer biblioteker som brukes under debugging eller er nødvendige for at koden skal fungere
    import turtle # gui lib
    import random # tilfeldige tall
    from icecream import ic #debugging 
    import tkinter
except ImportError: # hvis man mangler et eller flere lib's så skal denne koden kjøre
    print("missing imports")
    raise SystemExit # slutter koden så den ikke forsetter med all den andre koden

turtle.colormode(255) # lar turtle bruke RGB verdier
scr = turtle.Screen() # funksjonene som turtlen ikke skal gjøre
# turtle.register_shape("assets/player.gif") # skal legge til mere men denne legger til en gif fil til en form
class buttons:
    
    def __init__(self, *args):
        turtle.register_shape("./assets/buttons/menu_button.gif")
        self.turtles = {"menu":turtle.Turtle("./assets/buttons/menu_button.gif")
                        
                        ,"map":[turtle.Turtle(),   
                        turtle.Turtle(),turtle.Turtle()],
                        
                        "shape":[turtle.Turtle(),
                        turtle.Turtle(),turtle.Turtle()],
                        
                        "reset":turtle.Turtle()}
        self.map = ["assets/map1.png"]
        self.player = ["assets/player.gif","assets/player_modle2.gif"]
        self.scr = args[0]#screen
        
    def map_1(self):
        self.scr.bgpic(self.map[0])
    def map_2(self):
        self.scr.bgpic()
    def map_2(self):
        self.scr.bgpic()
    
buttons(scr).map_1()

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
                self.t[i].ht()
                self.t[i].pu()
                self.t[i].setpos(random.randint(-200,200), random.randint(-200,200)) #
                self.t[i].pd()
                self.t[i].st()


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

def mainloop(scr): # main loop som har alle tingene som skal repitere i lokale variabler og henter resten av klassene
    
    tk = tkinter.Tk()
    tk.title("map")
    tk.geometry("200x300")
    but = buttons(scr)
    input_box_map = tkinter.Text(tk,height=10,width=20)
    
    
    scr = turtle.Screen()
    enemy = entity.enemy(6)
    player = entity.player()
    scr.onkeypress(player.right,'d');scr.onkeypress(player.right, 'Right')
    scr.onkeypress(player.left, 'a');scr.onkeypress(player.left,  'Left')
    scr.onkeypress(player.back, 's');scr.onkeypress(player.back,  'Down')
    scr.onkeypress(player.forwa,'w');scr.onkeypress(player.forwa, 'Up')
    
    while (True):
        scr.listen()
        enemy.enemy()
        scr.update()
        for i in turtle.turtles():
            
            if (i != player.t and i.distance(player.t)<=15):
                raise SystemExit
            
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
    mainloop(scr)
print("kjørt")
