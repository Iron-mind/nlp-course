import requests
import os

def savefile_from_url(url, filename):
  ruta_json = url#"https://drive.usercontent.google.com/download?id=1vd1TXPVf7qIfBoLlENxAJJzA-xqUHST2&export=download&authuser=2&confirm=t&uuid=a7f1c72f-018e-4e3c-a343-5108ac0f4309&at=APZUnTUJlETGpaE6wFiLnNiKg0HD:1713928747604"


  respuesta = requests.get(ruta_json)
  contenido = respuesta.content
  #os.makedirs("/data", exist_ok=True)
  nombre_archivo = os.path.basename(filename)

  with open(os.path.join("./data", nombre_archivo), "wb") as archivo:
      archivo.write(contenido)