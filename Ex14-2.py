#!/usr/bin/env python3
#encoding: "UTF-16"

#Desarrolla un programa que tenga las siguientes características:
#Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
#Dicho problema resuélvelo con bucles for y while. 
#Justifica en el propio programa porque una opción es adecuada y la otra no.
#¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente una solución es 
#más eficiente? Investiga para comprobarlo.

#El programa consiste en lanzar 2 dados y sumarlos tantas veces como se establezca i mostrar el resultado por pantalla

#WHILE

import random
import time

if __name__ == "__main__":
    #Declare variales and ask for the inputs
    random.seed(a=None, version=2)
    total = 0
    num = int(input("Introduce a number: "))
    #make the loop to sum all the dices
    while num != 0:
        dice = random.randint(1,6)
        total += dice
        num-=1
    #print the total
    print("The total is: %d" % (total))

#En este caso este es peor ya que no tenemos un número predefinido o una variable a buscar
#Ademas en este caso tenemos más variables y es más complicado de leer