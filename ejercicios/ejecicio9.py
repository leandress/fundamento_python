#generar usuarios de la forma en que se mustra 

nombre=input("ingrese su nombre " )
apellido=input("ingrese su apellido " )
edad=input("infrese su edad ")

print("los nombre de usuario")

a=nombre+apellido
print("@"+a.title())
b=nombre+"."+apellido
print("@"+b.lower())
c=nombre+"_"+apellido+"_"+edad
print("@"+c.lower())
