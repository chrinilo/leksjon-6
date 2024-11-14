#importerer pyplot som  er hva vi bruker til å lage grafen, og vi kaler den plt
import matplotlib.pyplot as plt


#gir navn til grafen og dennes x og y
plt.title("sammenheng")

plt.ylabel("pris")
plt.xlabel("folk")

# lagger variabler til de forskjellie faktorene vi trenger å beriene for
fastpris = 4500
per_p = [500, 750, 900]
max_p = [40, 20, 10]
rabatpris = 10000

# regne selve rabaten
def regn_rabat(x):
    y =int( x * (100-15) /100)
    return y

#regne å skrive grafen
def regn_graf(z, farge_navn):
    #loope tre ganger, for å passe på at vi får alle de forskelige nivåene.
    for d in range(0, 3, 1):
        #lage en variabel, så vi kan skrive alle de tre type grafene
        farge =["green", "yellow", "red"]
        #lage andre variabler
        pris = fastpris
        y = []
        x = []
        #passe på at det ikke er flere folk en det er mment til å være
        if z > max_p[d]:
            z = max_p[d]
        #en loop hvor vi regner vær eneste y posisjon basert på x
        for i in range(z):
            #legger til en x til listen
            x.append(i)
            # regner prisen vi skal legge till y, siden den gror exponensielt
            pris += per_p[d]
            #sjekker om prisen vi legger til y er støre eller min dre en priusen der vi legger til rabat.
            if pris > rabatpris:
                #hvis den er støre, legg til rabat
                y.append(regn_rabat(pris))
            if pris < rabatpris:
                # ellers bare leg det til y
                y.append(pris)
        print(len(x),x)
        print(len(y), y)
        #print grafen med x og y kordinatene, itilleg med dennes farge og titel basert på nivået
        plt.plot(x, y, color=farge[d], label=farge_navn[d])
    #vise titel
    plt.legend(loc='upper center')
    #åpne grafen
    plt.show()





# lage main loop/kretsløpet
def main_loop():
    #gjøre run til true som er hva som holder loopen gåene.
    run = True
    #navn til de forskjelige nivåene
    farge_navn = ["grønn", "gul", "rød"]

    #starter loopen
    while run:
        #lager en loop, hvor man ber dem putte in et gyldig tall, og bare slutter etter de har gjort det
        ferdig = True
        try:
            inp = int(input("hvor mange er dere? "))
        except:
            print("skriv ett helt tall.")
            print()
            continue
        #passer på at man ikke får null
        if inp == 0:
            print("Skriv noe over null.")
            print()
            continue
        #regner pris og totalpris for de forskjelige nivåene.
        for i in range(0,3,1):
            pris = 0
            #passer på at det er nåk folk basert på nivå
            if inp > max_p[i]:
                inp = max_p[i]
            #regner pris
            pris = inp * per_p[i] + fastpris

            #skjekker om prisen er over 10000 og legger til rabat hvis den er, før man legger til pris.
            if pris >= rabatpris:
                totalpris = regn_rabat(pris)
            else:
                totalpris = pris
            #printe pris, og totalpris basert på om nivået.
            print(f"{farge_navn[i]} nivå, prisen hadde vært {pris}")
            print(f"{farge_navn[i]} nivå, totalprisen er {totalpris}")
            print()
        #spøre om du vil se grafen, til du gir et gyldig svar
        while ferdig:
            inp2 = input("vil du se en graff?(J/N): ")
            #hvis du skriver j, viser den grafen.
            if inp2.upper() == "J":
                regn_graf(inp, farge_navn)
                ferdig = False
            #hvis du skriver nei,starter den mainloopen på nytt.
            elif inp2.upper() == "N":
                print("ok")
                ferdig = False
            else:
                print("skriv J eller N")





#starter main loopen
main_loop()