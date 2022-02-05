## generar un csv con las coordenadas de las fotos que se encuentran en una carpeta.
from PIL import Image
from PIL.ExifTags import TAGS
import os 
import exifread


def listarArchivos(path):
    os.chdir(path)
    archivos = os.listdir()
    return archivos

def hallarMetadatos(archivos, path):
    metadatos = []
    cont = 0
    for archivo in archivos:
        imagen = Image.open(f'{path}\{archivo}')
        metadato = imagen.getexif()
        diccionario = {}
        diccionario['nombre'] = archivo
        for etiqueta, valor in metadato.items():
            if etiqueta in TAGS:
                diccionario[TAGS[etiqueta]]= valor
        metadatos.append(diccionario)
    
    for i in metadatos:
        print(f'{i} \n')
        cont +=1
    
    print(f'hay {cont} imagenes')

def hallarCoords(archivos, path):
    coords = []
    cont = 0
    for archivo in archivos:
        imagen = open(f'{path}\{archivo}', 'rb')
        contents = exifread.process_file(imagen)
        diccionario = {}
        diccionario['nombre'] = archivo
        for key in contents:
            if key == "GPS GPSLongitude":
                long = str(contents[key])
                dirLong = str(contents['GPS GPSLongitudeRef'])
                diccionario['long'] = long, dirLong
                # print("latitud =", contents[key],contents['GPS GPSLongitudeRef'], '\n')
            elif key =="GPS GPSLatitude":
                lat = str(contents[key])
                dirLat = str(contents['GPS GPSLatitudeRef'])
                diccionario['lat'] = lat, dirLat
                # print("longitud =",contents[key],contents['GPS GPSLatitudeRef'])
        coords.append(diccionario)
    
    for i in coords:
        cont +=1
    
    print(f'hay {cont} imagenes')
    return coords

def CoordenadasDecimales(DATOSFOTOS):
    coordenadasFotos =[]
    for datosfoto in DATOSFOTOS:
        coordenadaFoto =[datosfoto['nombre']]
        coordenadaDecimal= int()
        for key, value in datosfoto.items():
            if key == 'lat' or key == 'long':
                datosLista = list(value)
                cont =0
                coordenada = []
                for dato in datosLista:
                    if cont == 0:
                        numero = ''
                        for elemento in dato:
                            if elemento not in ('[', ']', ' ', ',', '/'):
                                numero+=elemento
                            elif elemento in (',', '/', ']'):
                                numero = int(numero)
                                coordenada.append(numero)
                                numero = ''
                            else: 
                                continue 
                        cont += 1   
                    else:
                        coordenadaDecimal= coordenada[0] + (coordenada[1]/60)+ ((coordenada[2]/coordenada[3])/3600)
                        if dato == 'W':
                            coordenadaDecimal *= -1
                        coordenadaFoto.append(coordenadaDecimal)
        coordenadasFotos.append(coordenadaFoto)
        
    return coordenadasFotos

def run(path):
    listArchivos = listarArchivos(path)
    coords=hallarCoords(listArchivos, path)
    decimales = CoordenadasDecimales(coords)
    print('el archivo CSV y json se han creado con exito:')


if __name__=='__main__':
    PATH = input('cual es la carpeta en la que se encuentran las fotos?: ')
    listArchivos = listarArchivos(PATH)
    coords=hallarCoords(listArchivos, PATH)
    decimales = CoordenadasDecimales(coords)
    for i in decimales:
        print(i)
    # run(PATH)
