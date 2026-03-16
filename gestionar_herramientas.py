from gestionar_json import *
from validaciones import validar_menu,validar_entero, validar_texto
from gestionar_categorias import seleccionar_categoria

NOMBRE_ARCHIVO='herramientas.json'

def seleccionar_estado():
    op=validar_menu('''
    Seleccione el estado
    1. Bueno
    2.Regular
    3.Malo
    4.salir
                ''', 1,4)
    if op==1:
        return 'Bueno'
    elif op==2:
        return 'regular'
    elif op==3:
        return 'malo'
    else:
        print('saliendo')

def guardar_herramientas():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['nombre']=validar_texto('Ingrese el nombre: ')
    diccionario['categoria']=seleccionar_categoria()
    diccionario['cantidad_disponible']=validar_entero('Ingrese la cantidad disponible')
    diccionario['estado']=seleccionar_estado()
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_herramientas():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            ****************************
            ID:                  {elemento.get('id','clave erronea')}
            Nombre:              {elemento.get('nombre','clave erronea')}
            Categoria:           {elemento.get('categoria','clave erronea')}
            Disponibilidad:      {elemento.get('cantidad_disponible','clave erronea')}
            Estado               {elemento.get('estado','clave erronea')}
            ''')
def listar_herramientas_disponiles():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        if elemento.get('cantidad_disponible') > 0:
            print(f'''
                ****************************
                ID:                  {elemento.get('id','clave erronea')}
                Nombre:              {elemento.get('nombre','clave erronea')}
                Categoria:           {elemento.get('categoria','clave erronea')}
                Disponibilidad:      {elemento.get('cantidad_disponible','clave erronea')}
                Estado               {elemento.get('estado','clave erronea')}
                ''')

def buscar_herramientas():
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
                    Categoria:           {elemento.get('categoria','clave erronea')}
                    Disponibilidad:      {elemento.get('cantidad_disponible','clave erronea')}
                    Estado               {elemento.get('estado','clave erronea')}
                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def validar_herramientas(id):
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
        listar_herramientas()
        id=validar_entero("Ingrese el id a actualizar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Nombre.
                                    2. Categoria
                                    3. Disponibilidad
                                    4. Estado   
                                    5. Cancelar
                                        ''',1,5)
                match op_actualizar:
                    case 1:
                        elemento['nombre']=validar_texto('Ingrese el nombre: ')
                    case 2:
                        elemento['categoria']=seleccionar_categoria()
                    case 3:
                        elemento['cantidad_disponible']=validar_entero('Ingrese la cantidad disponible ')
                    case 4:
                        elemento['estado']=seleccionar_estado()
                    case 5:
                        print('Operación cancelada!')
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def eliminar_herramientas():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_herramientas()
        id=validar_entero("Ingrese el id a eliminar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)
      
def actualizar_herramientas(id_herramienta, cantidad, operacion='restar'):
    registros = cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        if elemento.get('id') == id_herramienta:
            if operacion == 'restar':
                elemento['cantidad_disponible'] -= cantidad
            else:
                elemento['cantidad_disponible'] += cantidad
            guardar(NOMBRE_ARCHIVO, registros)
            return True
    return False
