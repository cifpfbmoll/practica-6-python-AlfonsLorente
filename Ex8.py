#!/usr/bin/env python3
#encoding: "UTF-16"

#Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números 
#introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.
#Escribe límite: 50
#Escribe un valor: 10
#Escribe otro valor: 45
#45 es demasiado grande. Escribe otro valor: 1
#Escribe otro valor: 39
#El límite a alcanzar es 50. La lista creada es: 10, 1, 39

if __name__ == "__main__":
    #declare variables and ask the user for an imput
    numlist = []
    total = 0
    limit = int(input("insert a limit number: "))
    number = int(input("insert a number: "))
    while number > limit:
        number = int(input("The number excided the limit, insert a number smaller or equal than %d: " % (limit)))
    numlist.append(number)
    total += number

    #if the total is not equal than the limit number, keep looping
    while total < limit:
        number = int(input("insert another number: "))
        total += number
        #if the limit is exceeded repeat the number
        while total > limit:
            total -= number
            number = int(input("ERROR: The total excided the limit, you actually are on %d and you gotta get to %d, insert another number: " % (total, limit)))
            total += number
        numlist.append(number)

    #print the numbers
    print("The  limit number, %d, has been acomplished because the sum of the numbers: %d" %(limit, numlist[0]), end="")
    del numlist[0]
    for i in range(len(numlist)):
        print(" +", numlist[i], end="")
    print(" is equal to: %d" % (total))