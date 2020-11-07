"""nombre = input("Cual es tu nombre?\n") 
print("Hola "+nombre)
edad =int(input("Cuál es tu edad?\n"))
edad = edad -10
print(edad)
Mentira= False
Verdad = True
print(Mentira or Verdad)"""

"""Diccionario ={"paella":"comida"}
print(Diccionario["paella"])
A=input("Entrada diccionario\n")
B=input("Entrada descripción\n")
Diccionario[A]=B
print(Diccionario[A])"""


"""
numero = int(input("Numero: "))
if numero>-3 and numero<0:
    print("pertenece")
elif numero<6 and numero>=3:
    print("pertence")
else:
    print("no pertence")
"""



"""
n = int(input("Numero: "))
i=0
for x in range(2,n):
    if n % x==0:
        i+=1
        
if i!=0:
    print(f"{n}no es primo")
else:
    print(f"{n}es primo")
"""

"""
frase = input()
print(frase.count("a"))
n=0
for i in range(len(frase)):
    if frase[i]=="a":
        n+=1
print(n)
"""

"""
usuarios = {"juanito":1245613, "eva":9109201, "santi":9239367}
usuario = input()
if usuario in usuarios:
    print(usuarios[usuario])
else:
    print("no encontrado")
"""

"""
Usuarios={"Fitzgerald":"111mKj","Laura":"CasarDE","Adam":"lololo1212","Bob":"ee3345","Emma":"333kjf"}
A=input("Introduzca su usuario\n")
if A in Usuarios:
    B=input("Introduzca contraseña\n")
    if B==Usuarios[A]:
        print("Contraseña correcta\n")
    else:
        print("Contraseña errónea\n")
else:
    print("Usuario no existente\n")
"""
"""
def correo(email):
    n=len(email)
    B=False
    if "@" in email:
        if email[n-4:n]==".com":
            B=True
    return B

print(correo("l@l.com"))
"""

"""
def esprimo(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

def factorial(n):
    B=1
    for i in range(1,n+1):
        B=i*B
    return B
    """

# El enunciado está mal redactado, en la primera parte se pide hacer un programa que calcule el factorial de un numero.
# En la segunda parte se nos pide que el script responda a si un número es factorial o no
# Haré la primera variante
import Comprobar
N=int(input("Introduzca un número entero\n"))
print("¿EL número introducido es primo?:\n",Comprobar.esprimo(N))
print("El factorial del número introducido es\n",Comprobar.factorial(N))

