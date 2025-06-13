# notas = [7, 2, 4]

# while True:
#     try:

#         print('''
#             1.- Ingresar nota
#             2.- Borrar nota
#             3.- Mostrar notas
#             4.- Sacar promedio, nota mayor y nota menor
#             5.- Limpiar todas las notas
#             6.- Salir
#             ''')
#         op = int(input("Ingrese una opción: "))

#         match op:
#             case 1:
#                 print("Opción 1")
#                 nueva = int(input("Ingrese una nota para agregar a la lista: "))
#                 notas.append(nueva)
#                 print(f'''
#                       Lista actual:
#                        {notas}''')

#             case 2:
#                 print("Opción 2")
                
#                 for i, n in enumerate(notas):
#                     print(f"{i+1}.- {n}")
#                 borrar = int(input("Seleccione la posición de la nota a borrar: "))  
#                 notas.pop(borrar-1)  

#                 print(f'''
#                       Lista actual:
#                        {notas}''')

#             case 3:
#                 print("Opción 3")
#                 print(f'''
#                       Lista actual:
#                        {notas}''')
#             case 4:
#                 print("Opción 4")
#                 sum = 0
#                 cont = 0
#                 for i in notas:
#                     sum = sum + i
#                     cont = cont + 1
#                 promedio = sum / cont    

#                 print(f"El promedio es {promedio}.")    
#                 print(f"Nota min: {min(notas)}")
#                 print(f"Nota max: {max(notas)}")

#             case 5:
#                 print("Opción 5")
#                 notas.clear
#                 print("La lista ha sido limpiada")
#             case 6:
#                 print("Opción 1")
#                 break
#             case _:
#                 print("Opción no válida")                     

#     except ValueError:
#          print("Error: Ingrese sólamente digitos enteros.")
            






