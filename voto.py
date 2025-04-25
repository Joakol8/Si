# num = int(input("Ingrese un numero de votantes: "))

# kaiser = 0
# nose = 0 

# for i in range (1, num+1, 1):
#     voto = int(input("Ingrese su voto. Para Kaiser, vote: 1  Para Nose, vote: 2."))

#     if voto == 1:
#         kaiser = kaiser + 1
#     elif voto == 2:
#         nose = nose + 1
#     else:
#         print("Error. VOTO NULO")

# print(f"Los votos para Kaiser son {kaiser}.") 
# print(f"Los votos para Nose son {nose}") 

# if kaiser > nose:
#     print("Ha ganado Kaiser!")
# elif kaiser == nose:
#     print("No gana nadie. Perkines.")
# else:
#     print("Ha ganado Nose!")        



# palabra = input("Ingrese una palabra: ")
# cont = 0
# vocales = 0
# voca = ["a","e","i","o","u"]


# for i in palabra:
#     if i == voca:
#         vocales = vocales + 1
#     cont = cont + 1


# print(f"Letras: {cont}  Vocales: {vocales}")


# import time
# num = 10
# while num >= 0:
#     print(num)
#     time.sleep(1)
#     num = num - 1

clave = 1234
contraseña = int(input("Ingrese su contraseña : "))
while clave != contraseña:
    print("ERROR CONTRASEÑA INCORRECTA PERKIN")
    contraseña = int(input("Ingrese su contraseña : "))