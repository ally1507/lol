from validaciones import validar_menu
from gestionar_prestamos import  guardar_prestamos, actualizar_prestamos, eliminar_prestamos, listar_prestamos, buscar_prestamos, registrar_devoluciones
def menu_prestamos():
    while(True):
        op=validar_menu('''
        1. Guardar prestamos 
        2. Actualizar prestamos
        3. Listar prestamos
        4. Buscar prestamos
        5. Eliminar prestamos.
        6. Registrar devoluciones
        7. Salir
                        ''', 1,7)
        match op:
            case 1:
                guardar_prestamos()
            case 2:
                actualizar_prestamos()
            case 3:
                listar_prestamos()
            case 4:
                buscar_prestamos()
            case 5:
                eliminar_prestamos()
            case 6:
                registrar_devoluciones()
            case 7:
                break
