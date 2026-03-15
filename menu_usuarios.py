from validaciones import validar_menu
from gestionar_usuarios import guardar_usuarios, actualizar_usuarios, eliminar_usuarios, buscar_usuarios, listar_usuarios 

def menu_usuarios():
    while(True):
        op=validar_menu('''
        1. Registrar usuarios
        2. Actualizar usuarios
        3. Listar usuarios
        4. Buscar usuarios
        5. Eliminar usuarios
        6. Salir

        ''', 1,6)
        match op:
            case 1:
                guardar_usuarios()
            case 2:
                actualizar_usuarios()
            case 3:
                listar_usuarios()
            case 4:
                buscar_usuarios()
            case 5:
                eliminar_usuarios()
            case 6:
                break