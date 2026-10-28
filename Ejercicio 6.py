#Programa para calcular el 30%, el 60% y el 90% de un numero cualquiera

numero = int(input("Ingrese un numero -->  "))

porcentaje_30 = 30/100
porcentaje_60 = 60/100
porcentaje_90 = 90/100

resultado_30 = numero * porcentaje_30
resultado_60 = numero * porcentaje_60
resultado_90 = numero * porcentaje_90

print("................................")
print(f"el 30% de {numero} es = {resultado_30} ")
print(f"el 60% de {numero} es = {resultado_60} ")
print(f"el 90% de {numero} es = {resultado_90} ")
print("................................")