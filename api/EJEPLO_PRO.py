import re

usuario= input("digite el usuario ")
patron= "^[a-zA-Z0-9]${3,25}"

resultado = re.search(patron, usuario)

if resultado:
  print("bien")
else:
  print("intente de nuevo")
  