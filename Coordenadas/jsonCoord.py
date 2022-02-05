## generar un csv con las coordenadas de las fotos que se encuentran en una carpeta.
from cmath import isnan, nan
# from pathlib import Path
# from PIL import Image
# from PIL.ExifTags import TAGS
import os 
import exifread
from pyproj import Transformer
import pandas as pd
import numpy as np
import json

pd.options.display.float_format = '{:.9f}'.format

def listarArchivos(path):
    os.chdir(path)
    archivos = os.listdir()
    return archivos

# def hallarMetadatos(archivos, path):
#     metadatos = []
#     cont = 0
#     for archivo in archivos:
#         imagen = Image.open(f'{path}\{archivo}')
#         metadato = imagen.getexif()
#         diccionario = {}
#         diccionario['nombre'] = archivo
#         for etiqueta, valor in metadato.items():
#             if etiqueta in TAGS:
#                 diccionario[TAGS[etiqueta]]= valor
#         metadatos.append(diccionario)
    
#     for i in metadatos:
#         print(f'{i} \n')
#         cont +=1
    
#     print(f'hay {cont} imagenes')

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
    
    print(f'hay {cont} archivos en la carpeta \n\n')
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

def transformar(origen, destino, ListaCoordenadas): 
    CoordTransformadas = []
    for foto in ListaCoordenadas:
        try:
            x=foto[1]
            y=foto[2]
        except:
            x=nan
            y=nan
        origen=4326
        destino=3857
        transformer = Transformer.from_crs(origen, destino)
        x2, y2 = transformer.transform(x, y)
        foto.append(x2)
        foto.append(y2)
        CoordTransformadas.append(foto)

    df=pd.DataFrame(CoordTransformadas, columns=['nombre', 'N', 'W', 'X', 'Y'])
    print(df)

    return df

def json(df):
    lista= df.to_numpy().tolist()
    encabezado = '{"features":['
    cuerpo =''
    cont = 0
    for fila in lista:
        if fila[0] == 'coordenadas.csv':
            continue
        elif isnan(fila[3]):
            continue
        else:
            primero = '{"geometry":{"x":'
            x=lambda x: x if fila[3] != nan else fila[3]
            x=str(fila[3])
            segundo=',"y":'
            y=str(fila[4])
            tercero=',"spatialReference":{"wkid":102100}},"attributes":{"name":"'
            nombre=str(fila[0])
            cuarto= '","description":""},"symbol":{"color":[255,0,0,255],"size":12,"angle":0,"xoffset":0,"yoffset":0,"type":"esriSMS","style":"esriSMSCross","outline":{"color":[0,0,0,255],"width":0.75,"type":"esriSLS","style":"esriSLSSolid"}}},'
            cuerpo = cuerpo+primero+x+segundo+y+tercero+nombre+cuarto
            cont += 1
    cuerpo = cuerpo[:len(cuerpo)-1]
    final = '],"displayFieldName":"","fieldAliases":{},"spatialReference":{"wkid":102100,"latestWkid":3857},"fields":[]}'
    scripJson=encabezado+cuerpo+final
    file = open('data.json', 'w')
    file.write(scripJson)

    print(f'\nse generó un archivo tipo Json con las coordenadas de {cont} imagenes')


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
    origen=4326
    destino=3857
    df=transformar(origen, destino, decimales)
    df.to_csv(f'{PATH}\coordenadas.csv')
    json(df)

