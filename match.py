# Uso de match y def
def suma():
      n1 = int(input('Ingrese el primer número: '))
      n2 = int(input('Ingrese el segundo número: '))
      print("La suma es: ", n1 + n2)       
def resta():
      n1 = int(input('Ingrese el primer número: '))
      n2 = int(input('Ingrese el segundo número: '))
      print("La suma es: ", n1 - n2)                     
def multi():
      
      n1 = int(input('Ingrese el primer número: '))
      n2 = int(input('Ingrese el segundo número: '))
      print("La multiplicación es: ", n1 * n2)                     
def divi():  
    
    
         

    try:
     n1 = int(input('Ingrese el primer número: '))
     n2 = int(input('Ingrese el segundo número: '))
     print("El resultado de la división es: ", n1 / n2)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")




def calcu():
     while True:

        op = int(input('''Seleccione una opción:
                    1. Suma
                    2. Resta
                    3. Multiplicación
                    4. División
                    5. Salir      
                    '''))
        match op:
            case 1:
                print('Has seleccionado la opción suma')
                suma()

            case 2:
                print('Has seleccionado la opción resta')
                resta
            case 3:
                print('Has seleccionado la opción multiplicación')
                multi()
            case 4:
                print('Has seleccionado la opción división')
                divi()    
            case 5:
                break
            case _:
                print('Opción no válida')     
calcu()     

# nuevo menu recursivo
# debe tener 3 programas creados anteriormente
# el menu debe llamar a estos programas y ejecutarlos de manera correcta
# debe tener la opcion de salir y la opcion por defecto





            

