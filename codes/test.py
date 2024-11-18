try:
    import matplotlib.pyplot as plt
    from icecream import *
except:
    print("du mangler en import.")
#loop var
kjør = True

#var
mengde = int(10)
tur = 4500
per_person = 500
pris_med_rabat = 0
pris_uten_rabat = 0
rabat = 10000
pris_penger_uten_rabat_gul = 0
pris_penger_uten_rabat_rød = 0
pris_penger_med_rabat_gul = 0
pris_penger_med_rabat_rød = 0

pris_g = 750 #20 personer
pris_r = 900 #10 presoner
y_n = ''

#def regner graph
try:
    def graph_regning(meng, meng_g,meng_r):
        pris = []
        pris_gul = []
        pris_rød = []
        y_axen = []
        global kjør,pris_penger_uten_rabat_gul, pris_penger_uten_rabat_rød, pris_penger_med_rabat_gul, pris_penger_med_rabat_rød, pris_med_rabat, pris_uten_rabat

        x = 1
        y = 1
        z = 1

        if meng > 40:
            meng = 40
        if meng_g > 20:
            meng_g = 20
        if meng_r > 10:
            meng_r = 10

        y_axen_g = []
        y_axen_r = []

        pris_gul.append(pris_uten_rabat)
        pris_rød.append(pris_uten_rabat)
        pris.append(pris_uten_rabat)
        y_axen.append(x)
        y_axen_g.append(y)
        y_axen_r.append(z)
        for i in range(meng):

            y_axen.append(x)
            x += 1

            if pris_uten_rabat >= rabat:
                pris_med_rabat = pris_uten_rabat * 85 / 100
                pris.append(pris_med_rabat)
                pris_uten_rabat += per_person

            else:
                pris.append(pris_uten_rabat)
                pris_uten_rabat += per_person

        for j in range(meng_g):

            y_axen_g.append(y)
            y += 1
            if pris_penger_uten_rabat_gul >= rabat:
                pris_penger_med_rabat_gul = pris_penger_uten_rabat_gul * 85 / 100
                pris_gul.append(pris_penger_med_rabat_gul)
                pris_penger_uten_rabat_gul += pris_g

            else:
                pris_gul.append(pris_penger_uten_rabat_gul)
                pris_penger_uten_rabat_gul += pris_g
        for k in range(meng_r):    

            y_axen_r.append(z)
            z += 1

            if pris_penger_uten_rabat_rød >= rabat:
                pris_penger_med_rabat_rød = pris_penger_uten_rabat_rød * 80 / 100
                pris_rød.append(pris_penger_med_rabat_rød)
                pris_penger_uten_rabat_rød += pris_r

            else:
                pris_rød.append(pris_penger_uten_rabat_rød)
                pris_penger_uten_rabat_rød += pris_r

        ic(y_axen, pris, pris_gul, pris_rød)
        plt.plot(y_axen, pris, c="#0f0")
        plt.plot(y_axen_g, pris_gul, ls = '--', c= '#efcc00')
        plt.plot(y_axen_r, pris_rød, ls = '-.', c= '#f00')



        høyest_pris = len(pris) - 1
        høyest_pris_r = len(pris_rød) - 1
        høyest_pris_y = len(pris_gul) - 1

        y_n = input('vil du se graphen? ')

        if y_n == 'j':
                print ('her er graphen')
                plt.show()
                kjør = False
        else:            
            print( høyest_pris, "grønnt nivå er", pris[høyest_pris], "gult nivå er", pris_gul[høyest_pris_y], "rødt nivå er", pris_rød[høyest_pris_r])
            kjør = False

    
    def main_loop():
        kjør = True
        y_n = ''
        mengde = 0
        while kjør:
            try:
                mengde =int(input('hvor mange er dere? '))
            except:
                pass
            if mengde == 0:
                print ("ikke nokk folk")
                print (" ")
                main_loop()
                break
            
            graph_regning(mengde,mengde,mengde)
            if kjør == True:
                kjør = False
except:
    print("error")
    pass
    
main_loop()        
    