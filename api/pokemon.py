import requests
x=0
print("Digite el id de un pokemon")
id=input("->")
url=f"https://pokeapi.co/api/v2/pokemon/{id}"
respuesta=requests.get(url)
if respuesta:
  datos=respuesta.json()
  print(datos["abilities"][0]["ability"]["name"])
  print(datos["moves"][0]["move"]["name"])
  
  for habilidad in datos["abilities"]:
    print(habilidad["ability"]["name"])
    
  for movimientos in datos["moves"]:
    x=x+1
    
    print(x,movimientos["move"]["name"])
  
else:
  print("No la para")