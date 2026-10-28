#Programa que permita a una tienda saber el valor de la compra añadiendo al final el 16% del IVA


valor = int(input("Ingrese el precio unitario del producto --> "))
cantidad = int(input("Ingrese la cantidad de productos --> "))

resultado = valor * cantidad

resultado_2 = resultado * 0.16

resultado_final = resultado + resultado_2

print(".........................")
print(f"El valor que pagara el cliente es = {resultado_final} incluyendo el 16% del IVA")
print(".........................")
