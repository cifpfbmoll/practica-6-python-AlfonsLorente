#!/usr/bin/env python3

#Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. 
#Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. 
#El programa termina escribiendo la lista de números:
#Escribe un número: 6
#Escribe un número mayor que 6: 10
#Escribe un número mayor que 10: 12
#Escribe un número mayor que 12: 25
#Escribe un número mayor que 25: 9
#Los números que has escrito son: 6, 10, 12, 25  
#(Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista,
#haced esto así a partir de ahora)

if __name__ == "__main__":
    #declare variables and ask for the inputs
    marklist = []
    mark1 = int(input("insert a note: "))
    mark2 = int(input("enter a greater note: "))
    marklist.append(mark1)
    marklist.append(mark2)

    #if the second number is greater, repeat the operation
    while mark1 <= mark2:
        mark1 = mark2
        mark2 = int(input("enter a greater note: "))
        marklist.append(mark2)
    #eliminar el numero sobreante introducido para salir
    del marklist[-1]
    #print answer
    print("the introduced marks are: ", end="")
    print(*marklist, sep = ", ")