#pedir al usuario que ingrese su nombre y edad imprimir que tipo de datos son las variables y decir en que año nacio
nombre=input("ingrese su nombre ")
edad=input("ingrese su edad ")
edad=int(edad)
print(nombre)
print(type(nombre))
print(edad)
print(type(edad))
año=2022-edad
print("su año de nacimiento",año)