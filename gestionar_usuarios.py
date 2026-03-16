from gestionar_json import *
from validaciones import validar_menu, validar_entero, validar_texto
from gestionar_categorias import validar_categoria, listar_categorias

NOMBRE_ARCHIVO='usuarios.json'

def tipo_usuario():
    op=validar_menu('''
    Seleccioneque usuario es:
     1. Residente
     2. Administrador
     3. Salir


''', 1,3)

def guardar_usuarios():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['nombre']=input('Ingrese su nombre: ')
    diccionario['apellido']=input('Ingrese su apellido: ')
    diccionario['telefono']=validar_entero('Ingrese su telefono: ')
    diccionario['direccion']=input('Ingrese su direccion: ')
    diccionario['tipo_usuario']=tipo_usuario()
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
        id=validar_entero("Ingrese el id a actualizar: "))
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
                        elemento['nombre']=validar_texto('Ingrese el nombre del producto: ')
                    case 2:
                        elemento['apellido']=validar_texto('Ingrese el apellido: ')
                    case 3:
                        elemento['telefono']=validar_entero('Ingrese el telefono: ')
                    case 4:
                        elemento['direccion']=validar_texto('Ingrese la direccion: ')
                    case 5:
                        elemento['tipo_usuario']=tipo_usuario()
                    case 6:
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