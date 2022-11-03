def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Listar personas', listar),
        '2': ('Agregar persona', agregar),
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')

def listar():
    leer_dni = open("dni.txt", "rt")
    datos_dni = leer_dni.read()
    print(datos_dni)

    leer_nombre = open("nombre.txt", "rt")
    datos_nombre = leer_nombre.read()
    print(datos_nombre)

    leer_apellido = open("apellido.txt", "rt")
    datos_apellido = leer_apellido.read()
    print(datos_apellido)


def agregar():
    agregar_dni = open("dni.txt", "at")
    contenidod = input("Digite dni: ")
    agregar_dni.write(contenidod)
    agregar_dni.close()

    agregar_nombre = open("nombre.txt", "at")
    contenidon = input("Digite nombre: ")
    agregar_nombre.write(contenidon)
    agregar_nombre.close()

    agregar_apellido = open("apellido.txt", "at")
    contenidoa = input("Digite apellido: ")
    agregar_apellido.write(contenidoa)
    agregar_apellido.close()


def salir():
    print('Saliendo')
