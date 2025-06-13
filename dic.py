fruta = {
    "manzana" : 3000

}

while True:
    print('''
        1.- Ingresar fruta y precio
        2.- Actualizar precio de fruta
        3.- Borrar fruta y precio
        4.- Mostrar frutas y precios
        5.- Comprar
        6.- Salir
        ''')  

    op = int(input("Ingresa una opción: "))



    match op:
        case 1:
            print("Opción 1")
            nueva = input("Ingrese el nombre de la fruta: ")
            precio = int(input("Ingrese el precio de la fruta: "))
            fruta[nueva] = precio
            print(f'''
                Lista actual:
                {fruta}''')
        case 2:
            print("Opción 2")
            act = input("Ingrese el nombre de la fruta a actualizar: ")
            actprecio = int(input(f"Ingrese el nuevo precio de {act}: "))
            fruta[act] = actprecio
            print(f'''
                Lista actual:
                {fruta}''')

        case 3:
            print("Opción 3")
            borrar = input("Ingrese el nombre de la fruta a borrar: ")
            del fruta[borrar]
            print(f'''
                Lista actual:
                {fruta}''')

        case 4:
            print("Opción 4")
            print(f'''
                Lista actual:
                {fruta}''')
        case 5:
            print("Opción 5")
            print("Productos a comprar: \n")
            for i,j in fruta.items():
                print(f"{i} = ${j}")
            print("\nGracias por tu compra")    
        case 6:
            print("Salir")
            break
        case _:
            print("Opción no válida")
