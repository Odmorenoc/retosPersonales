import random

def identificador(list):
    # conjunto=[i for i in set(list)]
    # for i in list:
    #     if i in conjunto:
    #         conjunto.remove(i)
    #     else: 
    #         return i 

    for i in list:
        indice = abs(i)
        if list[indice] < 0:
            return abs(i)
        else:
            list[indice]*=-1

def run(n):
    list=[random.randint(0,n-1) for i in range(n)]
    print(list)
    repetido=identificador(list)
    if repetido is None:
        repetido = "ninguno"   
    print(f"el primer numero repetido es {repetido}")

if __name__=='__main__':
    intro='''
    Este programa corresponde a una reto encontrado en tictok,
    https://www.tiktok.com/@drkbugs/video/7056152079072595205?is_from_webapp=1&sender_device=pc&web_id7035230368740165126
    en el cual se solicita encontrar el primer numero repetido en una lista
    de longitud n, en donde los valores del array, van de 0 a n-1, sin embargo
    la solución debe cumplir 2 condiciones:

    1. Complejidad temporal lineal, es decir O(n)
    2. Complejidad espacial constante, O(1) en otras palabras no se puede
    utilizar un array auxiliar.
    
    '''
    print(intro)
    n=int(input('por favor ingresa el valor de n'))
    run(n)
