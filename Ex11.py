#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). 
#El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el 
#usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños. pista:
#import random
#import time
#minimo = int (input ( "Valor mínimo:"))
#max = int (input ( "Valor máximo:"))
#secreto = random.randint (mínimo, máximo)
#Valor mínimo: 0
#Valor máximo: 100
#A ver si adivinas un número entero entre 0 y 100.
#Escribe un número: 20
#Demasiado pequeño! Volver a probar: 30
#Demasiado grande! Volver a probar: 27
#Correcto! Lo has intentado 3 veces.

import random
import time

if __name__ == "__main__":
    random.seed(a=None, version=2)
    #declare the variables and ask the user for some imputs
    minimum = int(input("Insert the minimum number: "))
    maximum = int(input("Insert the maximum number: "))
    counter = 1
    #Repeat until the maximum number is greater
    while minimum >= maximum:
        print("The minimum number cannot be less than or equal to the maximum")
        maximum = int(input("Insert a greater maximum number: "))

    secretNum = random.randint(minimum, maximum)
    #Tell the user what to do
    print("Guess the number between %d and %d!" % (minimum, maximum))
    userNum = int(input("Insert a number: "))
    #loop till the user get the right number
    while (userNum != secretNum):
        if userNum < secretNum and userNum >= minimum and userNum <= maximum:
            print("TOO LOW!")
            userNum = int(input("Try again: "))
        elif userNum > secretNum and userNum >= minimum and userNum <= maximum:
            print("TOO HIGH!")
            userNum = int(input("Try again: "))
        else:
            print("The number isn't between the numbers %d and %d" % (minimum, maximum))
            userNum = int(input("Insert a right number: "))
        counter += 1
    
    #when the number is achived, print this output
    print("THE NUMBER %d IS CORRECT!" % (userNum))
    print("You have tried %d times" % (counter))

