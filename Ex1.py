#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. 
#El programa termina escribiendo la lista de palabras.
#Escribe una palabra: viaje
#Escribe más palabras: aventura
#Escribe más palabras: cómic
#Escribe más palabras:
#Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']

if __name__ == "__main__":
    #declare the variables
    list = []
    #advise the user
    print("press enter to stop writing words")
    #ask for the words
    word = input("insert a word: ")
    while word != "" "":
        list.append(word)
        word = input("insert a word: ")
    print("Your words were: ", list[:])
