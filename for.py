clave = 1234




for i in range(3, -1, -1):

    password = int(input("Ingrese la contraseña:"))

    if password==clave:
        print("Bienvenido al sistema")
        break
    else:
        print(f"Clave invalida. Quedan {i} intentos.")
