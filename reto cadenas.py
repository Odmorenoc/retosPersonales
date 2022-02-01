def leercadena(texto):
    texto =texto.lower()
    palabras = []
    palabra = str()
    for i in texto:
        if i != ' ':
            palabra += i
        else: 
            palabras.append(palabra)
            palabra = str()
    palabras.append(palabra)
    return palabras

def contarPalabras(setPalabras, listaPalabras):
    diccionario ={}
    for i in setPalabras:
        diccionario[i] = 0
    
    for i in listaPalabras:
        if i in diccionario.keys():
            diccionario[i] += 1
        else:
            continue
    return diccionario


if __name__ == '__main__':
    TEXTO = 'creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar'
    palabras = leercadena(TEXTO)
    palabrasUnicas = set(palabras)
    conteo = contarPalabras(palabrasUnicas, palabras)
    print(palabrasUnicas)
    for key, value in conteo.items():
        print(f'la palabra "{key}" aparece {value} veces en el texto')