# total = 0
# nombre = input("Ingrese su nombre: ")
# productos = 0

# while True:
#     op = int(input('''
#                 1. Leche $1000
#                 2. Fideos $500
#                 3. Carne $10-000
#                 4. Pagar
#                 Seleccione una opción: '''))
#     match op:
#         case 1:
#             print("Ha seleccionado Leche")
#             print("Costo de la leche: $1.000")
#             cantidad = int(input("¿Cuántas unidades desea llevar?: "))
#             total = total + (1000*cantidad)
#             productos = productos + (1*cantidad)
#         case 2:
#             print("Ha selecionado fideos")
#             print("Costo: $500")
#             cantidad = int(input("¿Cuántas unidades desea llevar?: "))
#             total = total + (500*cantidad)
#             productos = productos + (1*cantidad)
#         case 3:
#             print("Ha seleccionado carne") 
#             print("Costo: $10.000")
#             cantidad = int(input("¿Cuántas unidades desea llevar?: "))
#             total = total + (10000*cantidad)
#             productos = productos + (1*cantidad)
#         case 4:
#             print(f'''
#                 {nombre}, Usted lleva {productos} productos.
#                 Valor neto = {total // 1.19}
#                 IVA = {round((total // 1.19) * 0.19)}
#                 Valor total= {total}
#                 Gracias por comprar.
#                 ''')
#             break
#         case _:
#             print("Opción no válida.")     

                    

cantAlum = int(input("Ingrese cantidad de alumnos: "))
prom = 0
suma = 0
alumnos = 0
sumaT = 0

for i in range(cantAlum):
    notasAlum = int(input(f"Ingrese cantidad de notas del alumno {i+1}: "))
    suma = 0
    for j in range(notasAlum):
        nota = float(input(f"Ingrese la nota {j+1} del alumno {i+1}: "))
        suma = suma + nota
    prom = suma / notasAlum
    alumnos = alumnos + 1
    sumaT = sumaT + prom
    promedioTotal = sumaT / cantAlum
    
    print(f"El promedio del alumno {i+1} es {prom}")

    if prom >= 4.0:
        print(f"El alumno {i+1} ha aprobado.")
    else:
        print(f"El alumno {i+1} ha reprobado.")  

print(f"La cantidad de alumnos es: {alumnos}")
print(f"El promedio total de todos los alumnos es: {promedioTotal}")                 