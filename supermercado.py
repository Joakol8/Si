cantidad = 0
total = 0

while True:
    print("¿Qué producto llevará?")
    print("1.- Leche")
    print("2.- Galleta")
    print("3.- Detergente")
    print("0.- Salir")
    opcion = int(input("Elija una opción: "))
    if opcion == 0:
        print(f"Usted lleva {cantidad} productos. Su total a pagar es ${total}\n\n.")
        break
    elif opcion == 1:
        print("Costo de Leche: $1000")
        total = total + 1000
        cantidad = cantidad + 1 
        print(f"Su total a pagar es ${total}.\n\n\n\n")
    elif opcion == 2:
        print("Costo de Galleta: $600")
        total = total + 600
        cantidad = cantidad + 1
        print(f"Su total a pagar es ${total}.\n\n\n\n")
    elif opcion == 3:
        print("Costo de Detergente: $2000")
        total = total + 2000
        cantidad = cantidad + 1
        print(f"Su total a pagar es ${total}.\n\n\n\n")         

        

