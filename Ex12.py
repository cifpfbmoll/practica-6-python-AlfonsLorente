#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). 
#El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. 
#El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
#Valor mínimo: 0
#Valor máximo: 100
#Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
#Es 50 ?: mayor
#Es 75 ?: menor
#Es 62 ?: menor
#Es 56 ?: mayor
#Es 59 ?: igual
#Gracias por jugar!!
#Mejoras (opcionales):
#    • que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
#    • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26" 
#      le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.

import random
import time

if __name__ == "__main__":
    random.seed(a=None, version=2)
    #declare the variables and ask the user for some imputs
    minimum = int(input("Insert the minimum number: "))
    maximum = int(input("Insert the maximum number: "))
    
    #Repeat until the maximum number is greater
    while minimum >= maximum:
        print("The minimum number cannot be less than or equal to the maximum")
        maximum = int(input("Insert a greater maximum number: "))
    
    guessNum = random.randint(minimum, maximum)
    #tell the user how the game will work
    print("Think about a number between %d and %d and i'll have to guess it!"%(minimum, maximum))
    print("You have to respond with: 'smaller', 'bigger' and 'equal'")
    userResp = input("Is your number %d? "%(guessNum))
    userResp.lower()
    
    #Repeat the loop until the user response is "equal"
    while userResp != "equal":
        if userResp == "bigger":
            minimum = guessNum
            guessNum = random.randint(minimum, maximum)
            userResp = input("Is your number %d? "%(guessNum))
            userResp.lower()
        elif userResp == "smaller":
            maximum = guessNum
            guessNum = random.randint(minimum, maximum)
            userResp = input("Is your number %d? "%(guessNum))
            userResp.lower()
        elif userResp != "smaller" and userResp != "bigger" and userResp != "equal":
            print("that is not a valid answer, you have to say 'smaller', 'bigger' or 'equal'")
            userResp = input("Input a valid answer: ")
            userResp.lower()
    #print the end
    print("Yeah! I win!")
    print("I hope you really enjoyed the game! Thanks for playing <3")

        




    
   
    

    