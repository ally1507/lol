from validaciones import validar_menu
from gestionar_categorias import guardar_categorias, actualizar_categoria, eliminar_categorias, listar_categorias, buscar_categoria
def menu_categorias():
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
                guardar_categorias()
            case 2:
                actualizar_categoria()
            case 3:
                listar_categorias()
            case 4:
                buscar_categoria()
            case 5:
                eliminar_categorias()
            case 6:
                
                break