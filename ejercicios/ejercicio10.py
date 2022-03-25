#loging 

import getpass
import time
texto="github \nVamos a empezar la aventura\n"

for letra in texto :
  print(letra, end="",flush=True)
  time.sleep(0.04)

email=input("ingrese su email\n->")
contraseña=getpass.getpass(prompt="Ingrese la contraseña\n->")
print(contraseña)
