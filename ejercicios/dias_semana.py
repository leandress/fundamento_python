
dias=[ ]
cantidad=int(input("cuanto dias desea agregar "))
for i in range (cantidad):
  print(f"ingrese el dia {i+1}")
  dias.append(input())

print("dias ingresado")
for dia in  dias:
  print(dia)