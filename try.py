

def main():
    
    while True:


            try:
                op = int(input('''
                            Seleccione una opción:
                            1.- Realizar Llamada
                            2.- Enviar correo electronico
                            3.- Cerrar Sesión
                            '''))
                match op:
                    case 1:
                        print('Opción 1 seleccionada')

                        while True:
                            telefono = input("Ingresa un número de celular. Debe ser de 9 dígitos y comenzar con un 9")
                            if (len(telefono == 9)) and telefono[0] == 9:
                                break 
                            else:
                                print("Error: Ingrese un numero valido.")
                            
            


                        
                    case 2:
                        print('Opción 2 seleccionada')
                        arroba = 0
                        while True:
                            email = input("Ingrese un correo electrónico:")
                            for i in email:
                                if i == "@":
                                    arroba = 1
                            if arroba == 0:
                                print("Error: La direción de correo electrónico no tiene @")
                            else:
                                break         
                    

                    case 3:
                        print('Saliendo...')
                        break
                    case _:
                        print('Opción no válida, intente de nuevo.')
            except Exception:
                print("Sólo numeros enteros del 1 al 3")           


main()