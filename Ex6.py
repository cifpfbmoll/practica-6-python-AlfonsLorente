#!/usr/bin/env python3
#encoding: "UTF-16"

import sys

#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. 
#Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. 
#El programa termina escribiendo la lista de números.
#Escribe un número: 6
#Escribe un número mayor que 6: 4
#4 no es mayor que 6. Vuelve a probar: 50
#Escribe un número entre 6 y 50: 45
#Escribe otro número entre 6 y 50: 13
#Escribe otro número entre 6 y 50: 4
#Los números situados entre 6 y 50 que has escrito son: 45, 13 

if __name__ == "__main__":
    #declare variables and ask the user for an input
    numlist = []
    minVal = int(input("Write the minumum value: "))
    maxVal = int(input("Write the maximum value: "))
    num1 = 0
    lastnum = 0

    #loop until the second number is greater than the first one
    while minVal >= maxVal:
        maxVal = int(input("%d is not greater than %d. Try again: " % (maxVal, minVal)))

    #loop until the number is not between the before two numbers
    num1 = int(input("Write a number between %d and %d: " % (minVal, maxVal)))
    while num1 > minVal and num1 < maxVal:
        numlist.append(num1)
        num1 = int(input("Write another number between %d and %d: " % (minVal, maxVal)))
    else:
        print("The number %d is not betweeen %d and %d. Operation ended." % (num1, minVal, maxVal))
    
    #Make an exception If the list has no number
    try:
        lastnum = numlist[-1]
        del numlist[-1]
    except IndexError:
        sys.exit("There isn't any number in the list")
    
    #print the numbers of the list
    print("The numbers introduced between %d and %d are: " % (minVal, maxVal), end="")
    for i in range(len(numlist)):
        print(numlist[i], end=", ")
    print(lastnum)
