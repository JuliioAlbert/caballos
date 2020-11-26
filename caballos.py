import json
import random
from operator import itemgetter


key = [0,0,0,0]
movimieno = [0,0,0,0]
negrosyblancos = [1,1,-1,-1]
caballo = [[0,1],[2,1],[6,-1],[8,-1]]
tab = [[0,0,0],[0,0,0],[0,0,0]]

with open('caballo.json') as file:
	data = json.load(file)

def reset(tab):
    for item in range(len(tab)):
        for i in range(len(tab[item])):
            tab[item][i] = 0
    return tab

def Fin(caballo):
    for c in caballo:
        print(c)
    
def play(datos,caballo,key,movimiento):
    for t in range(len(caballo)):
        for d in datos:
            if d[0] == caballo[t][0]:
                if (t == 0)and(key[0] == 0) and (movimiento[0] == 0):
                    caballo[t][0] = d[1]
                    movimiento[0] = 1
                    print("Po => ")
                    print(caballo[t][0])
                    tab = tableroJuego(caballo[t][0],1)
                    if (caballo[t][0]) == 8:
                        key[t] = 1
            
                if (t == 1)and(key[1] == 0)and (movimiento[1] == 0):
                    caballo[t][0] = d[1]
                    movimiento[1] = 1
                    print("Po => ")
                    print(caballo[t][0])
                    tab = tableroJuego(caballo[t][0],2)
                    if (caballo[t][0]) == 6:
                        key[t] = 1
                    
                if (t == 2)and(key[2] == 0)and (movimiento[2] == 0):
                    caballo[t][0] = d[1]
                    movimiento[2] = 1
                    print("Po => ")
                    print(caballo[t][0])
                    tab = tableroJuego(caballo[t][0],3)
                    if (caballo[t][0]) == 2:
                        key[t] = 1
                    
                if (t == 3)and(key[3] == 0)and (movimiento[3] == 0):
                    caballo[t][0] = d[1]
                    movimiento[3] = 1
                    print("Po => ")
                    print(caballo[t][0])
                    tab = tableroJuego(caballo[t][0],4)
                    if (caballo[t][0]) == 0:
                        key[t] = 1
    for t in tab:
        print(t)

    if 0 in key:
        movimiento = [0,0,0,0]
        tab = reset(tab)
        return play(datos,caballo,key,movimiento)
    else:
        return Fin(caballo)

def tableroJuego(posicion,caballo):    
    if posicion==0:
        tab[0][0] = caballo
    if posicion==1:
        tab[0][1] = caballo
    if posicion==2:
        tab[0][2] = caballo
    if posicion==3:
        tab[1][0] = caballo
    if posicion==5:
        tab[1][2] = caballo
    if posicion==6:
        tab[2][0] = caballo
    if posicion==7:
        tab[2][1] = caballo
    if posicion==8:
        tab[2][2] = caballo
    return tab


play(data,caballo,key,movimieno)

