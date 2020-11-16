#!/usr/bin/env python3

#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. 
#El programa termina escribiendo los dos números tal y como se pide:
#Escribe un número: 6
#Escribe un número mayor que 6: 6
#6 no es mayor que 6. Vuelve a introducir un número: 1
#1 no es mayor que 6. Vuelve a introducir un número: 8
#Los números que has escrito son 6 y 8

if __name__ == "__main__":
    #declare variables and ask for the inputs
    marklist = []
    mark1 = float(input("insert a note: "))
    mark2 = float(input("enter a greater note: "))
    #if the second number is lower, repeat the operation
    while mark1 >= mark2:
        mark2 = float(input("the second mark is not greater than the first mark, please enter a greater mark: "))
    #print answer
    print("the introduced marks are: ", "%.2f" % mark1 ," and ", "%.2f"%mark2)