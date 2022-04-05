#hacer un prograa que muestre un listado con los pokemonoes, el usurio tendra la oportunidad de digitar su id correspondiente. y se le mostrara la informacion.
#ademas el usuario podra navegar en el programa mediantes shortcuts y/o teclas del teclado
#algunas de las opciones serian
#ver siguiente y anterior liistado y pokemon 
#salir del programa
#buscar un pokemon por su id
#buscar un pokemon por su nombre

x=0
import requests
url="https://pokeapi.co/api/v2/pokemon{}"
respuesta=requests.get(url)
if respuesta:
  datos=respuesta.json()
  for nombres in datos["results"]:
    x=x+1    
    print(x,nombres ["name"])

  id=int(input("digite el id"))
  url=f"https://pokeapi.co/api/v2/pokemon{id}"
  print("
        
        ")
  
else:
  print("no funciona")