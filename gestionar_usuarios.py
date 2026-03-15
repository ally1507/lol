from gestionar_json import *
from validaciones import validar_menu, validar_entero, validar_texto
from gestionar_categorias import validar_categoria, listar_categorias

NOMBRE_ARCHIVO='usuarios.json'

def guardar_usuarios():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['nombre']=input('Ingrese su nombre: ')
    diccionario['apellido']=input('Ingrese su apellido: ')
    diccionario['telefono']=validar_entero('Ingrese su telefono: ')
    diccionario['direccion']=input('Ingrese su direccion: ')

    listar_categorias()
    id_cat=validar_entero('Ingrese el codigo de la categoria: ')
    while(validar_categoria(id_cat)==False):
        id_cat=validar_entero('Error, categoria no encontrada. Intente nuevamente: ')
    diccionario['categoria']=validar_categoria(id_cat)
    
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('PRODUCTO GUARDADO CORRECTAMENTE!')

def listar_usuarios():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            ****************************
            ID:                {elemento.get('id','clave erronea')}
            Nombre:            {elemento.get('nombre','clave erronea')}
            Apellido:          {elemento.get('apellido:  ','clave erronea')}
            Telefono:          {elemento.get('telefono', 'clave erronea')}
            Direccion:         {elemento.get('direccion', 'clave erronea')}    
            Tipo usuario:      {elemento.get('tipo_usuario', 'clave erronea')}  
            ''')
        
def buscar_usuarios():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        id=int(input("Ingrese el id a buscar: "))
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
                    ****************************
                    ID:                 {elemento.get('id','clave erronea')}
                    Nombre:             {elemento.get('nombre','clave erronea')}
                    Apellido:           {elemento.get('apellido:  ','clave erronea')}
                    Telefono:           {elemento.get('telefono:  ','clave erronea')}
                    direccion:          {elemento.get('direccion:  ','clave erronea')}
                    Tipo usuario:       {elemento.get('tipo_usuario:  ','clave erronea')}


                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def actualizar_usuarios():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_usuarios()
        id=int(input("Ingrese el id a actualizar: "))
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Nombre.
                                    2. apellido.
                                    3. Telefono
                                    4. Direccion      
                                    5. Tipo usuario
                                    6. Cancelar
                                        ''',1,6)
                match op_actualizar:
                    case 1:
                        elemento['nombre']=input('Ingrese el nombre del producto: ')
                    case 2:
                        elemento['apellido']=input('Ingrese el apellido: ')
                    case 2:
                        elemento['telefono']=input('Ingrese el telefono: ')
                    case 2:
                        elemento['direccion']=input('Ingrese la direccion: ')
                    case 2:
                        elemento['tipo_usuario']=input('Ingrese el tipo de usuario: ')
                    case 3:
                        print('Operación cancelada!')    
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def eliminar_usuarios():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_usuarios()
        id=int(input("Ingrese el id a eliminar: "))
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)