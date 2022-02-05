DATOSFOTOS = [{'nombre': 'TimePhoto_20210303_092433.jpg', 'lat': ('[5, 4, 23349/500]', 'N'), 'long': ('[75, 30, 15509/1000]', 'W')}, {'nombre': 'TimePhoto_20210303_092456.jpg', 'lat': ('[5, 4, 9367/200]', 'N'), 'long': ('[75, 30, 15563/1000]', 'W')}, 
{'nombre': 'TimePhoto_20210303_111049.jpg', 'lat': ('[5, 1, 449/40]', 'N'), 'long': ('[75, 32, 21851/1000]', 'W')}, 
{'nombre': 'TimePhoto_20210303_111052.jpg', 'lat': ('[5, 1, 11279/1000]', 'N'), 'long': ('[75, 32, 21527/1000]', 'W')}, 
{'nombre': 'TimePhoto_20210303_111107.jpg', 'lat': ('[5, 1, 2859/250]', 'N'), 'long': ('[75, 32, 21629/1000]', 'W')}, 
{'nombre': 'TimePhoto_20210303_111126.jpg', 'lat': ('[5, 1, 291/25]', 'N'), 'long': ('[75, 32, 10821/500]', 'W')}]

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




          

