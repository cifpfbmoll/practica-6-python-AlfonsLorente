#!usr/bin/env python3
#encoding: "UTF-16"

import sys

#Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. 
#El programa termina escribiendo nombres y números de teléfono. 
#Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.
#Dame un nombre: Pepe González
#Dame el teléfono: 971971971
#Dame un nombre: Macarena Gómez
#Dame el teléfono: 971999999
#Dame un nombre: Pascual Ribot
#Dame el teléfono: 666555444
#Dame un nombre: S
#Los nombres y teléfonos de la agenda son:
#Pepe González: 971971971
#Macarena Gómez: 971999999
#Pasqual Ribot: 666555444

if __name__ == "__main__":
    #declare variables and ask for some imputs
    contactList = []
    print("insert a name called 'S' to exit")
    name = input("Introduce a name: ")
    
    #While the name is not "S", keep adding contacts
    while name != "S":
        numb = input("Introduce its number phone: ")
        contact = [name]
        contact.append(numb)
        contactList.append(contact)
        name = input("Introduce a name: ")
    
    print("\n", end="")
    print("---------")
    print("\n", end="")

    #show all the contacts
    if not contactList:
        sys.exit("Error. There is no contacts!")
    for i in range(len(contactList)):
        for j in range(len(contactList[i])):
            if contactList[i][j].isnumeric():
                print(contactList[i][j])
            else:
                print(contactList[i][j], end=": ")
    