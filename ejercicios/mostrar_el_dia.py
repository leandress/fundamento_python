#sin usar if, while,for mostrar el dia de la semana

numero=int(input("ingrese un un respectivo numero "))
while numero  >7:
  numero=int(input("ingrese un un respectivo numero "))

dias=["domingo","lunes", "martes","miercoles","jueves","viernes","sabado"]

print(dias[numero - 1])