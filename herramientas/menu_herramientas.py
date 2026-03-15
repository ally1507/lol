from validaciones import validar_menu
from gestionar_herramientas import guardar_herramientas, actualizar_productos, eliminar_productos, buscar_herramientas, listar_herramientas

def menu_herramientas():
    while(True):
        op=validar_menu('''
        1. Registrar.
        2. Actualizar.
        3. Listar.
        4. Buscar.
        5. Eliminar.
        6. Salir

        ''', 1,6)
        match op:
            case 1:
                guardar_herramientas()
            case 2:
                actualizar_productos()
            case 3:
                listar_herramientas()
            case 4:
                buscar_herramientas()
            case 5:
                eliminar_productos()
            case 6:
                break