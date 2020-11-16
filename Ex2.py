#!/usr/bin/env python3


#Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. 
#El programa termina escribiendo la lista de números.
#Escribe un nombre: 14
#Escribe una otro nombre: 123
#Escribe una otro nombre: -25
#Escribe una otro nombre: 123
#Escribe una otro nombre: Salir
#Los números que has escrito son [14, 123, -25, 123]

if __name__ == "__main__":
    #declare the variables
    list = []
    #advise the user
    print("write 'exit' to stop writing numbers")
    #ask for the words
    num = input("insert a number: ")
    num = num.lower()
    while num != "exit": #keep looping while the user enters "exit"
        if num.isnumeric(): 
            list.append(int(num))
            num = input("insert another number: ")
            num = num.lower()
        elif num!= "exit" or num != num.isnumeric():
            print("Error, %s is not a number or 'exit'" %num)
            num = input("Now insert an actual number: ")
    print("your list is", list[:])
        