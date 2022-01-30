from inspect import _void
import random
from typing import List

## 1. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def maximo(a:int, b:int)->int:
    if a > b:
        return a
    else:
        return b

# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def maxTriple(a:int, b:int, c:int)-> int:
    max1: int = maximo(a,b)
    max2: int = maximo(b,c)
    max3: int = maximo(max1, max2)
    return max3

# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def create_pasword(longitud: int)-> str:
    MAYUS: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS: list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS:list = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    charset: list= MAYUS+MINUS+NUMS+CHARS

    password: list=[]

    for _ in range(longitud):
        char_rand: list = random.choice(charset)
        password.append(random.choice(char_rand))
    
    contraseña :str ="".join(password)
    return contraseña

def longitud(cadena:str) -> int:
    cont:int = 0
    for _ in cadena:
        cont += 1
    return cont

# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def esVocal(letra:str)-> str:
    vocales:list = ['a', 'e', 'i', 'o', 'u']
    if letra in vocales:
        return 'es vocal'
    else:
        return 'no es vocal'

#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sumatoria(lista: List[int])-> int:
    resultado:int = 0
    for i in lista:
        resultado += i
    return resultado

def multiplicacion(lista: list)-> int:
    resultado:int = 1
    for i in lista:
        resultado *= i
    return resultado

#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena:str)-> str:
    alReves:str = cadena[::-1]
    return alReves

#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True

def palindromo(cadena: str)-> bool:
    cadena = cadena.replace(" ","").lower()
    inverso:str = cadena[::-1]
    if cadena == inverso:
        return True
    else :
        return False

#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado

def superposicion(lista1, lista2):
    respuesta: bool = False
    for i in lista1:
        for j in lista2:
            if i == j:
                respuesta = True
    return respuesta

#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generarNcaracteres(n: int, c: str)->str:
    string: str = n*c
    return string

#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******

def procedimiento(lista: List[int]):
    caracter: str = '*'
    for i in lista:
        print(caracter*i)

## Ejecución:

def run():
    print('se devuelven los resultados de acuerdo al caso:')
    a: int = random.randint(-100,100)
    b: int = random.randint(-100,100)
    c: int = random.randint(-100,100)
    d: int = random.randint(0,15)
    cadena: str = create_pasword(d)
    numeros: list = [random.randint(1,10) for i in range(0,d)]
    lista1: list = [i for i in create_pasword(5)]
    lista2: list = [i for i in create_pasword(5)]
    letra: str = cadena[random.randint(0,longitud(cadena)-1)].lower()
    print(f'el numero mayor entre {a} y {b} es: {maximo(a,b)}')
    print(f'el numero mayor entre {a}, {b} y {c} es: {maxTriple(a,b,c)}')
    print(f'la longitud de la cadena {cadena} es: {longitud(cadena)}')
    print(f'el simbolo {letra} {esVocal(letra)}')
    print(f'la sumatoria de los numeros de la lista {numeros} es: {sumatoria(numeros)}')
    print(f'la multiplicación de los numeros de la lista {numeros} es: {multiplicacion(numeros)}')
    print(f'la cadena {cadena} es palindromo: {palindromo(cadena)}')
    print(f'las listas {lista1} y {lista2} tienen al menos un elemento en comun: {superposicion(lista1, lista2)}')
    print(f'se multiplica el simbolo {letra} por el numero {d}  y da: {generarNcaracteres(d, letra)}')
    print(f'el histograma de de la lista {numeros} es: ')
    print(procedimiento(numeros))


if __name__=='__main__':
    run()