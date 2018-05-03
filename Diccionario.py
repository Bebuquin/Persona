def menu():
    opciones = input ("[1] Jugar\n[2] Seleccionar usuario existente\n[3] Crear usuario\n[4] Versión\n[5] Salir\n")
    if opciones == "1":
        import p4
        menu()
    if opciones == "2" or opciones == "Seleccionar":
        import os, os.path
        carpetausuarios = ("./.Usuarios")
        listausuarios = os.listdir(carpetausuarios)
        print("\nLos usuarios existentes son:")
        for x in listausuarios:
            print (x)
        print("")
        usuario = input("Escribe tu nombre de usuario: ")
        path = ("./.Usuarios/%s" % usuario)
        if os.path.exists(path):
            os.chdir(path)
            print("Hecho")
        else:
            print("El usuario %s no existe. Use la opción '3' del menú para crearlo" % usuario)
            menu()
    if opciones == "3" or opciones == "Usuario" or opciones == "Crear":
        import os, os.path
        usuario = input("Escribe tu nombre de usuario: ")
        path = ("./.Usuarios/%s" % usuario)
        if os.path.exists(path):
            print("El usuario %s ya existe en %s" % (usuario, path))
            menu()        
        os.makedirs(path)
        print("Usuario %s creado en %s." % (usuario, path))
        menu()
    if opciones == "4" or opciones == "Versión":
        import Versión
        menu()
    if opciones == "5" or opciones == "Salir":
        print ("\nSaliendo")
        import sys
        sys.exit(0)
    return menu()
        

print("Diccionario personal creado por Guillermo Izquierdo Sánchez. Añade palabras y definiciones.")
menu()
