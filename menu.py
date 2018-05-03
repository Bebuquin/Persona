def menu():
    import os, os.path, sys, acercade
    owd = os.getcwd()
    opciones = input ("[1] Jugar\n[2] Seleccionar usuario existente\n[3] Crear usuario\n[4] Versión\n[5] Salir\n")
    if opciones == "1":
        os.system("clear")
        import p4
        os.system("clear")
        menu()
    if opciones == "2" or opciones == "Seleccionar":
        os.system("clear")
        carpetausuarios = ("./.Usuarios")
        listausuarios = os.listdir(carpetausuarios) #Cuando el programa se abre por primera vez, la carpeta no existe (ya que es creada al crear el primer usuario) y da error.
        print("Los usuarios existentes son:")
        for x in listausuarios:
            print (x)
        print("")
        usuario = input("Escribe tu nombre de usuario: ")
        path = ("./.Usuarios/%s" % usuario)
        if os.path.exists(path):
            os.system("clear")
            os.chdir(path)
            #Para crear los archivos, voy a crear otro modulo. Voy a utilizar el método open("file.txt", w+) para crearlos, llenar ciertos campos, y luego cerrarlos.
#Aquí debería crear algunos archivos de usuario en su respectiva carpeta, y luego volver a la carpeta original antes de volver al menú.
#Hecho, vuelvo a la carpera original con owd (Original working directory), que he definido justo al principio con os.getcwd(), que obtiene el current working directory.
            os.chdir(owd)
            print("Bienvenido")
        else:
            os.system("clear")
            print("El usuario %s no existe. Use la opción '3' del menú para crearlo" % usuario)
            menu()
    if opciones == "3" or opciones == "Usuario" or opciones == "Crear":
        os.system("clear")
        usuario = input("Escribe tu nombre de usuario: ")
        path = ("./.Usuarios/%s" % usuario)
        if os.path.exists(path):
            print("El usuario %s ya existe en %s" % (usuario, path))
            menu()        
        os.makedirs(path)
        print("Usuario %s creado en %s." % (usuario, path))
        menu()
    if opciones == "4" or opciones == "Versión":
        os.system("clear")
        acercade.ver()
        input("\n")
        os.system("clear")
        menu()
    if opciones == "5" or opciones == "Salir":
        os.system("clear")
        input ("\nPulse ENTER para finalizar")
        os.system("clear")
        sys.exit(0)
    os.system("clear")
    return menu()

print("Programa de prueba.\n")
menu()
