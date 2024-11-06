usuarios_db = {}


def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    
    nombre = input("Ingresa tu nombre: ")
    correo = input("Ingresa tu correo electrónico: ")


    if correo in usuarios_db:
        print("¡Error! Este correo ya está registrado.")
        return
    

    while True:
        contrasena = input("Ingresa tu contraseña: ")
        confirmar_contrasena = input("Confirma tu contraseña: ")
        
        if contrasena == confirmar_contrasena:
            break
        else:
            print("Las contraseñas no coinciden. Intenta de nuevo.")
    
    usuarios_db[correo] = {
        "nombre": nombre,
        "correo": correo,
        "contrasena": contrasena
    }
    
    print(f"¡Usuario {nombre} registrado exitosamente!")

def iniciar_sesion():
    print("\n--- Iniciar Sesión ---")
    
    correo = input("Ingresa tu correo electrónico: ")
    
    if correo not in usuarios_db:
        print("Correo no registrado. Intenta primero registrarte.")
        return
    
    contrasena = input("Ingresa tu contraseña: ")
    
    if usuarios_db[correo]["contrasena"] == contrasena:
        print(f"¡Bienvenido, {usuarios_db[correo]['nombre']}!")
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
