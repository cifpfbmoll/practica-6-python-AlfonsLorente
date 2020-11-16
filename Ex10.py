#!usr/bin/env python3
#encoding: "UTF-16"

import sys

#Escribe un programa que te pida los nombres y notas de alumnos. 
#Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. 
#Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. 
#Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
#Dame un nombre: Héctor Quiroga
#Escribe una nota: 4
#Escribe otra nota: 8.5
#Escribe otra nota: 12
#Dame otro nombre: Inés Valls
#Escribe una nota: 7.5
#Escribe otra nota: 1
#Escribe otra nota: 2
#Escribe otra nota: -5
#Dame otro nombre:
#Las notas de los alumnos son:
#Héctor Quiroga: 4.0 - 8.5
#Inés Valls: 7.5 - 1.0 - 2.0

def isFloat(num):
    try:
        float(num)
    except ValueError:
        return False
    else: 
        return True

if __name__ == "__main__":
    #declare variables and ask for some imputs
    studentList = []
    print("Insert a number less than 0 or greater than 10 to change the person and a empty name to exit the program")
    name = input("Introduce a name: ")
    
    #While the name is not EMPTY, keep adding contacts
    while name != "" "":
        student = [name]
        #add marks for every student
        mark = input("Introduce a mark: ")
        while float(mark) >= 0 and float(mark) <= 10:
            student.append(mark)
            mark = input("Introduce another mark: ")
        studentList.append(student)
        name = input("Introduce a name: ")
    
    print("\n", end="")
    print("---------")
    print("\n", end="")

    #show all the contacts
    if not studentList:
        sys.exit("Error. There is no students!")
    for i in range(len(studentList)):
        for j in range(len(studentList[i])):
            if studentList[i][j].isnumeric() or isFloat(studentList[i][j]):
                print("%.2f" % float(studentList[i][j]), end=" - ")

            else:
                print(studentList[i][j], end=": ")
        print("\n", end="")
    