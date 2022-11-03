import getpass
import menu
#declaracion de variables

registeredUser =open("login.txt","rt")
user = registeredUser.read()
registeredPW = open("clave.txt","rt")
password = registeredPW.read() 
#declaracion de funciones
def login(usuario,passw):
    if usuario in user:
        passw = getpass.getpass('Contraseña: ')
        if passw in password:
            return 1
        else:
            print("\n\tContraseña Incorrecta, intente de nuevo...\n")
            passw = getpass.getpass('Contraseña: ')
            if usuario in user:
                 if passw in password:
                     return 1
                 else:
                    print("\n\tContraseña Incorrecta\n")
            else:
             return 2
    else:
        return 2
 #inicializacion de procesos
usuario=input('Usuario: ')
while usuario != user:
    usuario=input('Usuario: ')
    passw = "2"

    if login(usuario,passw)==1:
        print('Bienvenido',usuario)
        print("\n\tDatos Persona")
        menu.menu_principal()
        
    else:
        print('Usuario no registrado')