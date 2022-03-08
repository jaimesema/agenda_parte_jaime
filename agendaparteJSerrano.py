def buscar_JSerrano(nombre, agenda):
    cadena = input("¿Qué contacto buscas?: ")
    for nombre, numtel in agenda.items():
        if nombre.startswith(cadena):
            print("El número de teléfono de %s es el %s" % (nombre, agenda [nombre]))