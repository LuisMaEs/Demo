# El enunciado está mal redactado, en la primera parte se pide hacer un programa que calcule el factorial de un numero.
# En la segunda parte se nos pide que el script responda a si un número es factorial o no
# Haré la primera variante
import Comprobar
N=int(input("Introduzca un número entero\n"))
print("¿EL número introducido es primo?:\n",Comprobar.esprimo(N))
print("El factorial del número introducido es\n",Comprobar.factorial(N))