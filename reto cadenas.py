def leercadena(texto):
    palabras = []
    for i in texto:
        if i != ' ':
            palabra = str()
            palabra += i
        else: 
            palabras.append(palabra)
            palabra = str()
    
    return palabras

if __name__ == '__main__':
    TEXTO = 'hola hola hola'
    palabrasUnicas = set(leercadena(TEXTO))
    print(palabrasUnicas)