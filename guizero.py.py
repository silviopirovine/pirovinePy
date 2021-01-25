import string
import numpy as np
import matplotlib.pyplot as plt
from guizero import App, Text, PushButton
f = open("dati4.txt", 'r')

coordX = []
coordY = []

for riga in f:
        valori = str(f.readline())  
        Nval = len(valori)          
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordX.append(int(valori[0])) 
        coordY.append(int(valori[1])) 

f.close() 
def grafico():

    print ("X: ",coordX)
    print ("Y: ",coordY)

    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    print(type(coordX))
    print(type(coordY))

    plt.scatter(coordX,coordY)
    plt.show()

app = App(title="Plot")
message = Text(app, text="Clicca il bottone per vedere il grafico!")
button = PushButton(app, text="Grafico", command=grafico)
app.display()
