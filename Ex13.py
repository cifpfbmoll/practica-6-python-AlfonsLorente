#!/usr/bin/env python3
#encoding: "UTF-16"

#Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. 
#Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.

import sys

if __name__ == "__main__":
    #ask for the number and set variables
        num = int(input("Insert an integer: "))
        prime = True
        counter = 0
        divisor = 2
        #the number must be greater than 0
        if num < 1:
            sys.exit("The number must be more than 0") 
        #Look if its prime
        while counter == 0 and divisor < num:
            if num % divisor == 0:
                counter += 1
            divisor += 1

        #print if its a prime number or not
        if counter == 0:
            print("The number %d IS a prime number" % num)
        else:
            print("The number %d is NOT a prime number" % num)

#Aunque en mi caso han hecho falta algunas variables más, se reduce mucho se consumo de potencia utilizado para el loop
#es decir, cuando llega al while, si no es primo, la primera vez que consigue aumentar el contador sale del while i finaliza.