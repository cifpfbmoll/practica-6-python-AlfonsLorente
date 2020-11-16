#!/usr/bin/env python3
#encoding: "UTF-16"

import sys

#Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos 
#supere el límite inicial. El programa termina escribiendo la lista de números.
#Escribe límite: 50
#Escribe un valor: 10
#Escribe otro valor: 25
#Escribe otro valor: 7
#Escribe otro valor: 14
#El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56

if __name__ == "__main__":
    #declare variables and ask the user for an imput
    numlist = []
    total = 0
    limit = int(input("insert a limit number: "))
    number = int(input("insert a number: "))
    numlist.append(number)
    total += number

    #if the total is less than the limit number, keep looping
    while total < limit:
        number = int(input("insert another number: "))
        numlist.append(number)
        total += number

    #print the numbers
    print("The limit number, %d, has been acomplished or exceeded by the sum of the numbers: " %(limit), end="")
    print(*numlist, sep=", ", end=" ")
    print("is equal to: %d" % (total))
    