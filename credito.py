# ingreso = int(input("Ingrese su renta mensual ($500.000 mínimo): "))
# print("Ingrese su nivel educacional: \n 1.- Basico\n2.-Medio\n3.- Superior")
# edu = int(input())
# nac = int(input("Ingrese su nacionalidad.\n 1.- Chilena\n2.- Extranjero\n "))
# credito = 0


# if ingreso >= 500000 and ingreso < 1000000:
#     credito = 300000
# elif ingreso > 1000000 and ingreso < 1500000:
#     credito = 650000
# elif ingreso > 1500000:
#     credito = 1000000
# else:
#     print("No cumple con renta mínima")


# if edu == 1:
#     credito *= 1
# elif edu == 2:
#     credito *= 1.3
# elif edu == 3:
#     credito *= 1.5

# if nac == 1:
#     credito = credito + 300000


# print(f"Usted tiene acceso a un crédito de ${credito}")


import random

print("Ingrese dos digitos, El segundo debe ser mayor que el primero. ")

while True:
    n1 = int(input("Ingrese el número 1: "))
    n2 = int(input("Ingrese el número 2: "))

    if n1 > n2:
        print("Error: El primer número es mayor que el segundo.")
        

    else:
        print("El número 2 es mayor que el número 1.")
        break    

ale = random.randint(n1, n2)

print(f"El número aleatorio es {ale}.")
print("▄"*ale)





