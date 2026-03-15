from validaciones import validar_menu
from menu_herramientas import menu_herramientas
from menu_categorias import menu_categorias
from gestionar_usuarios import guardar_usuarios


def menu_general():

    while(True):
        op = validar_menu('''
        1. Administrador
        2. Usuario
        3. Salir
        ''',1,3)

        match op:
            case 1:
                usuario = input('Ingrese el usuario: ')
                contraseña = input('Ingrese la contraseña: ')
                if usuario == "administrador" and contraseña == "1508":
                    print('Ingreso de administrador')

                    while(True):
                        op_administrador = validar_menu('''
                        1. Gestionar herramienta
                        2. Gestionar categorias
                        3. Salir
                        ''',1,3)
                        match op_administrador:
                            case 1:
                                menu_herramientas()
                            case 2:
                                menu_categorias()
                            case 3:
                                break
                else:
                    print('Usuario o contraseña no encontrados')
            case 2:
                print('Registro de usuario')
                guardar_usuarios()
            case 3:

                print('Saliendo del programa')
                break


                    

            