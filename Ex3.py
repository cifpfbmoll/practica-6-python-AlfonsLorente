#!/usr/bin/env python3

#Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
#Escribe una nota: 7.5
#Escribe una nota: 0
#Escribe una nota: 10
#Escribe una nota: -1
#Las notas que has Escrito son [7.5, 0.0, 10.0]

if __name__ == "__main__":
    #declare the variables
    marklist = []
    #advise the user
    print("Write a number other than 10 - 0 to finish the program")
    #ask for the words
    mark = float(input("Write a note: "))
    while mark >= 0 and mark <= 10: #keep looping while the user enters "exit"
        marklist.append(mark)
        mark = float(input("Write another note: "))
    print("las notas introducidas son: ", marklist[:])


        