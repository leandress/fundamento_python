#hacer un program que me pida digitar un monto en pesos y mostar el resultado en dolares.hacerlo user-friendly

print("saludos.\nporfavor ingrese la cantidad que desea cambiar")
pesos=float(input())

dolar="{0:.2f}".format(pesos/55.15)

print("el monto introducido= ",pesos, "convertio a peso es= ", dolar,"gracias por preferirnos")

