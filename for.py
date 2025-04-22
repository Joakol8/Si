clave = 1234




for i in range(3):

    password = int(input("Ingrese la contraseña:"))

    if password==clave:
        print("Bienvenido al sistema")
        break
    else:
        print(f"Clave invalida. Llevas {i} intentos.")
