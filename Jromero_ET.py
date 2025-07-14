def stock_marca(marca):
    contMarca = 0

    for producto, datos in productos.items():
        if datos[0].lower() == marca.lower():
            contMarca = contMarca + 1
    print(f"El stock es: {contMarca}")
def busqueda_precio(p_min, p_max):  
    consulta = []
    for producto, datos in productos.items():
        if precios[producto][0] >= p_min and precios[producto][0] <= p_max:
            consulta.append(f"{datos[0]}--{producto}")
    if consulta == []:
        print("No hay productos en el rango de precios consultados.")
    else:    
        print(f"Los notebooks entre los precios consultas son: {consulta}")       
def actualizar_precio(modelo, p):

    if modelo in precios:

        precios[modelo][0] = p
        return True
    else:
        
        return False


productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

precios = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

while True:
    try:
        op = int(input('''*** MENU PRINCIPAL ***
        1. Stock marca.
        2. Búsqueda por precio.
        3. Actualizar precio.
        4. Salir.'''))

        match op:
            case 1:
                marcaUsuario = input("Ingrese la marca del producto para saber cuanto stock tiene en su marca: ")
                stock_marca(marcaUsuario)
            case 2:
                while True:
                    try:
                        precioMin = int(input("Ingrese el precio mínimo a buscar: "))
                        precioMax = int(input("Ingrese el precio máximo a buscar: "))
                        busqueda_precio(precioMin, precioMax)
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")    
            case 3:
                
                validacion = False
                while validacion == False:
                    try:
                        modeloUsuario = input("Ingrese el modelo del producto a actualizar: ")
                        nuevoPrecio = int(input("Ingrese el nuevo precio del producto: "))
                        if actualizar_precio(modeloUsuario, nuevoPrecio):
                            print("Precio actualizado!!")

                        else:
                            print("El modelo no existe!!")

                        
                        while True:    
                            decision = input("¿Desea actualizar otro producto? (si/no): ")
                            if decision.lower() == 'si':
                                break
                            elif decision.lower() == 'no':
                                validacion = True
                                break
                                
                            else:
                                print("Debe ingresar 'si' o 'no'!!")
                                
                        



        
                    except ValueError:
                        print("Debe ingresar un valor entero!!")        

                
            case 4:
                print("Programa finalizado.")
                break
            case _:
                print("Debe seleccionar una opción válida!!")
    except ValueError:
        print("Error: Debe ingresar un número entero.")            