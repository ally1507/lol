from gestionar_json import *
from validaciones import validar_menu,validar_entero


NOMBRE_ARCHIVO='prestamos.json'

def guardar_prestamos():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['usuario']=input('Ingrese el nombre del usuario: ')
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_categorias():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            ****************************
            ID:             {elemento.get('id','clave erronea')}
            Nombre:         {elemento.get('nombre','clave erronea')}
            ''')
        
def buscar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        id=validar_entero("Ingrese el id a buscar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
                    ****************************
                    ID:             {elemento.get('id','clave erronea')}
                    Nombre:         {elemento.get('nombre','clave erronea')}
                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def validar_categoria(id):
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                return {
                            'id': elemento.get('id', 'clave no encontrada'),
                            'nombre': elemento.get('nombre', 'clave no encontrada')
                        }
    return False

def actualizar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_categorias()
        id=validar_entero("Ingrese el id a actualizar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Nombre.   
                                    2. Cancelar
                                        ''',1,2)
                match op_actualizar:
                    case 1:
                        elemento['nombre']=input('Ingrese el nombre: ')
                    case 2:
                        print('Operación cancelada!')
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def eliminar_categorias():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_categorias()
        id=validar_entero("Ingrese el id a eliminar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def seleccionar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print("No hay categorias registradas")
        return None

    print("\nCATEGORIAS DISPONIBLES")

    for elemento in registros:
        print(f"{elemento['id']}. {elemento['nombre']}")

    id = validar_entero("Seleccione el id de la categoria: ")

    for elemento in registros:
        if elemento['id'] == id:
            return elemento['nombre']

    print("Categoria no encontrada")