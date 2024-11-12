try:    #importrer biblioteker som brukes under debugging eller er nødvendige for at koden skal fungere
    import turtle # gui lib
    import random # tilfeldige tall
    from icecream import ic #debugging 
except ImportError: # hvis man mangler et eller flere lib's så skal denne koden kjøre
    print("missing imports")
    raise SystemExit # slutter koden så den ikke forsetter med all den andre koden
    
turtle.colormode(255) # lar turtle bruke RGB verdier
scr = turtle.Screen() # funksjonene som turtlen ikke skal gjøre
turtle.register_shape("assets/player.gif") # skal legge til mere men denne legger til en gif fil til en form

class entity: # kan egentlig fjerne
    class player: # lager spilleren 
        def __init__(self): #lager avriablene som skal bli brukt i klassen
            self.t = turtle.Turtle("assets/player.gif")
            self.shape1 = "assets/player.gif"
            self.shape2 = "assets/player_modle2.gif"
            # self.t.shapesize(0.4,0.4)
        
        def forwa(self): # alle rettningen for turtlen å gå
            self.t.forward(1)
        
        def back(self):
            self.t.back(1)
        
        def right(self):
            self.t.right(45)
        
        def left(self):
            self.t.left(45)

    class enemy: # lager finden(e)
        def __init__(self,mengde):
            self.t = []
            self.mengde = mengde
            for i in range(mengde): # lager alle turtlene til finde klassen og lagrer dem i en liste
                self.t.append(turtle.Turtle("classic"))
                self.t[i].color(random.randint(1,255),random.randint(1,255),random.randint(1,255))

                
        def enemy(self): # koden som faktisk beveger på seg
            for i in range(self.mengde):
                ic(i)
                dire = random.randint(1,4)
                num = random.randint(1,10)
                if (dire == 1):
                    for j in range(num):
                        self.t[i].forward(2)
                
                elif (dire == 2):
                    for j in range(num):
                        self.t[i].back(2)

                elif (dire == 3):
                    self.t[i].left(num)
                
                elif (dire == 4):
                    self.t[i].right(num)

def mainloop(): # main loop som har alle tingene som skal repitere i lokale variabler og henter resten av klassene
    scr = turtle.Screen()
    enemy = entity.enemy(5)
    player = entity.player()
    scr.onkeypress(player.right,'d');scr.onkeypress(player.right, 'Right')
    scr.onkeypress(player.left, 'a');scr.onkeypress(player.left, 'Left')
    scr.onkeypress(player.back, 's');scr.onkeypress(player.back, 'Down')
    scr.onkeypress(player.forwa,'w');scr.onkeypress(player.forwa, 'Up')
    while (True):
        scr.listen()
        enemy.enemy()
        scr.update()
        for i in turtle.turtles():
            if (i == player.t):
                print("ikke død")
            
            elif (i.distance(player.t )<=10):
                print("død")
            
            
            ic(i.pos())
            if i.pos()[1] <= -355:
                print("bunn")
                i.penup()
                i.setpos(i.pos()[0],350)
                i.pendown()
            
            if i.pos()[1] >= 355:
                print("topp")
                i.penup()
                i.setpos(i.pos()[0],-350)
                i.pendown()
            
            if i.pos()[0] <= -384:
                print("venstre")
                i.penup()
                i.setpos(382,i.pos()[1])
                i.pendown()
            
            if i.pos()[0] >= 384:
                print("høyre")
                i.penup()
                i.setpos(-382,i.pos()[1])
                i.pendown()
        
        ic (scr.screensize())

if __name__ == "__main__":
    mainloop()
