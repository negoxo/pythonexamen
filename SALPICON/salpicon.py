import random
salpicones=[]

def costo_total_fruta(fruta):
    return fruta["precio_unitario"] * fruta["cantidad"]

print("Bienvenido a Salpicones el Trío")
print("*")

cantidadFrutas = int(input("Ingrese la cantidad de frutas: "))


for i in range(cantidadFrutas):
        id = random.randint(1,200)
        nombre = input(f"Ingrese el nombre de la fruta : ")
        precio_unitario = float(input(f"Ingrese el precio unitario de la fruta : "))
        cantidad = int(input(f"Ingrese la cantidad de la fruta : "))
        fruta = {"id": id, "nombre": nombre, "precio_unitario": precio_unitario, "cantidad": cantidad}
        salpicones.append(fruta)

valorTotalSalpicon = 0
for fruta in salpicones:
    valorTotalSalpicon += fruta["precio_unitario"] * fruta["cantidad"]

print("\nCosto total del salpicón:", valorTotalSalpicon)
        
costo_ordenado_mayor = sorted(salpicones, key=costo_total_fruta, reverse=True)
print("\nFrutas ordenadas por costo de mayor a menor: ")
for fruta in costo_ordenado_mayor:
    print(f"{fruta['nombre']}: ${costo_total_fruta(fruta)}")

costo_ordenado_menor = sorted(salpicones, key=costo_total_fruta, reverse=False)
print("\nFrutas ordenadas por costo de menor a mayor: ")
for fruta in costo_ordenado_menor:
    print(f"{fruta['nombre']}: ${costo_total_fruta(fruta)}")

print("\n¡Gracias por su compra!")