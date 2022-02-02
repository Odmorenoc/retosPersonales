#reto ejecutado a partir de ver el video: https://www.youtube.com/watch?v=I3tJjQKN0h4&t=548s

def leercadena(texto: str) -> list:
    texto =texto.lower().replace(',','')
    palabras: list = []
    palabra = str()
    for i in texto:
        if i != ' ':
            palabra += i
        else: 
            palabras.append(palabra)
            palabra = str()
    palabras.append(palabra)
    #palabras = texto.split(' ')
    return palabras

def contarPalabras(listaPalabras: list) -> dict:
    diccionario: dict ={}

    for i in listaPalabras:
        if i in diccionario:
            diccionario[i] += 1
        else: 
            diccionario[i] = 1
    return diccionario

def run(texto: str)-> None:
    palabras = leercadena(TEXTO)
    conteo = contarPalabras(palabras)
    for key, value in conteo.items():
        print(f'la palabra "{key}" aparece {value} veces en el texto')


if __name__ == '__main__':
    TEXTO: str = 'creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar'
    run(TEXTO)    