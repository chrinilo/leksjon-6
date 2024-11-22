try:    #importrer biblioteker som brukes under debugging eller er nødvendige for at koden skal fungere
    import turtle # gui lib
    import random # tilfeldige tall
    from time import sleep # fps
    from tkinter import messagebox # alle popupsa
    from pygame import mixer
    from icecream import ic
except ImportError: # hvis man mangler et eller flere lib's så skal denne koden kjøre
    print("missing imports")
    raise SystemExit # slutter koden så den ikke forsetter med all den andre koden

turtle.colormode(255) # lar turtle bruke RGB verdier
scr = turtle.Screen() # funksjonene som turtlen ikke skal gjøre
# turtle.register_shape("assets/player.gif") # skal legge til mere men denne legger til en gif fil til en form
def sound():
    mixer.init()
    mixer.music.load("assets/sound/musikk.wav","musikk.wav")
    mixer.music.play(start=0, loops=10000000)
class buttons: # klasse for å bytte kart
    
    def __init__(self, *args):
        # alle kartene som kan bli brukt i en liste
        self.map = ["assets/maps/map1.png","assets/maps/map2.gif","assets/maps/map3.gif"]
        # koden over lager turtle, gjemmer turtle og tar pennen opp
        self.tersure = turtle.Turtle();self.tersure.penup();self.tersure.hideturtle()
        self.scr = args[0]#screen
        
        
    def maps(self,x): # oppdaterer kartet til riktig kart
        # denne setter også skatt posisjonen på alle kartene
        if x == 1:
            self.scr.bgpic(self.map[0])
            self.tersure.setpos(-189.00,-111.53)
            return 
        if x == 2:
            self.scr.bgpic(self.map[1])
            self.tersure.setpos(191.68,-225.03)
        if x == 3:
            self.scr.bgpic(self.map[2])
            self.tersure.setpos(84.91,-96.10)

class entity:
    class player: # lager spilleren 
        def __init__(self): #lager avriablene som skal bli brukt i klassen
            self.t = turtle.Turtle()
            self.shape1 = [ "assets/sprites/player.gif",
                            "assets/sprites/player_modle2.gif",
                            "assets/sprites/player_modle2.gif"]
            for i in self.shape1:turtle.register_shape(i)
            # hjemmer pennen og turtlen flytter turtlen og gjør om på koden på de to første linjenne
            self.t.ht()
            self.t.pu()
            self.t.setpos((-80,130))
            self.t.pd()
            self.t.st()

        def forwa(self): # alle rettningen for turtlen å gå
            self.t.forward(1)

        def back(self):
            self.t.back(1)

        def right(self):
            self.t.right(30)

        def left(self):
            self.t.left(30)
        
        def shape(self,x):
            if x == 0:
                self.t.shape(self.shape1[0])
            if x == 1:
                self.t.shape(self.shape1[1])
            if x == 2:
                self.t.shape(self.shape1[2])

    class enemy: # lager finden(e)
        def __init__(self,mengde):
            self.t = [] #lager en tom liste som skal ha findeturtlene.
            self.mengde = mengde
            for i in range(mengde): # lager alle turtlene til finde klassen og lagrer dem i en liste
                self.t.append(turtle.Turtle("classic"))
                self.t[i].color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
                self.t[i].ht();self.t[i].pu() # gjemmer og tar penn opp
                self.t[i].setpos(random.randint(-200,200), random.randint(-200,200)) #
                self.t[i].pd();self.t[i].st() # gjør det motsatte av 

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

# main loop som har alle tingene som skal repitere i lokale variabler og henter resten av klassene
def mainloop_(scr): 
    run = True # main loopen vin var
    #lager variabler med verdier til alle klassene
    sound()
    but = buttons(scr) 
    enemy = entity.enemy(3)
    player = entity.player()
    try:
        # hviket kart spilleren vil spille
        but.maps(int(scr.numinput("map", "which map do you want to play. (1,2,3)")))
        # hvilken sprite spilleren skal bruke
        player.shape(int(scr.numinput("skin","which player model dou you want to use? (1,2,3)")))
        # vansklighetsgraden til spillet
        dif = int(scr.numinput("diff", "which difficulty do you want to play (1 = hard, 2 = easy)"))
        if dif == 1:scr.tracer(0) # setter den til å være vanskligere
    except:raise SystemExit
    # except TypeError:print("wright a number between 1 and 3")
    scr.onkeypress(player.forwa,'w');scr.onkeypress(player.forwa, 'Up')
    scr.onkeypress(player.back, 's');scr.onkeypress(player.back,  'Down')
    scr.onkeypress(player.left, 'a');scr.onkeypress(player.left,  'Left')
    scr.onkeypress(player.right,'d');scr.onkeypress(player.right, 'Right')
    
    #main loopen
    while (run):
        # kjører spillet på 30 fps
        sleep(1/30)
        # ser om du trykker på tastaturet
        scr.listen()
        # påkaller finden sin bevegelse
        enemy.enemy()
        # oppdaterer skjermen for når du spiller den vansklighere modusen
        scr.update()
        #sjekker på alle turtlene
        for i in turtle.turtles():
            # vin cheken
            if (i == player.t and i.distance(but.tersure)<=15):
                print("win")
                messagebox.showinfo("win","du vant!")
                run = False
            
            if (i != player.t and i != but.tersure and i.distance(player.t)<=15):
                messagebox.showinfo("tap","du tapte...")
                run = False
            
            #sjekker om du er utenfor skjermen
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
#kjører koden
mainloop_(scr)

