from gestionar_herramientas import listar_herramientas_disponiles
from gestionar_json import *
from validaciones import validar_menu,validar_entero


NOMBRE_ARCHIVO='prestamos.json'


def seleccionar_estado():
    op=validar_menu('''
    Seleccione el prestamo
    1. Activo
    2. devuelto
    3. Vencido
    4. salir
                    
    if op==1:
        return 'activo'
    elif op==2:
        return 'devuelto'
    elif op==3:
        return 'vencido'
    else:
        print('saliendo')
                    
                ''', 1,4)


def guardar_prestamos():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    listar_usuarios()
    id_usuario=validar_entero('Ingrese el id del usuario:')
    registros_usuarios=cargar('usuarios.json')
    for elemento in registros_usuarios:
        if elemento.get('id','clave no encontrada')==id_usuario:
            diccionario['usuario_id']=elemento.get('id','clave no encontrada')
            diccionario[nombre_usuario]= f"{elemento.get('nombre','clave no encontrada')}"{elemento.get('apellido','clave no encontrada')}""
            break
    else:
        print('No se encontro el usuario')
        return
    listar_herramientas_disponiles()
    id_herramienta=validar_entero('Ingrese el id de la herramienta: ')
    for elemento in cargar('herramientas.json'):
        if elemento.get('id','clave no encontrada')==id_herramienta:
            diccionario['herramienta_id']=elemento.get('id','clave no encontrada')
            diccionario['nombre_herramienta']=elemento.get('nombre','clave no encontrada')
        break #El break se pone para detener el for en el momento que encuentra el ID, así no sigue recorriendo el resto de la lista innecesariamente.
    else:
        print('La herramienta no se encontro')
        return
    cantidad=validar_entero('Ingree la cantidad que queir prestas:')
    while cantidad > cantidad_disponible:
        print(f'Solo queda {cantidad_disponible} disponible')
        cantidad=validar_entero('Ingrese la cantidad a prstar: ')
        diccionario['cantidad']=cantidad

    dias=validar_entero(input('ingrese los dias que la necesita:'))
    fecha_inicio= date.today()
    fecha_final= date.today()+ timedelta(days=dias)
    diccionario['fecha_inicio']=str(fecha_inicio)
    diccionario['fecha_final']=str(fecha_final)
    print(f'la fecha de inicio es: {fecha_inicio} y la fecha final es: {fecha_final}')

    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_prestamos():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se registraron prestamos')
    for elemento in registros:
        print(f'''
            ****************************
            ID:              {elemento.get('id','clave erronea')}
            Nombre:          {elemento.get('nombre','clave erronea')}
            Herramienta:     {elemento.get('herramienta','clave erronea')}
            Cantidad:        {elemento.get('cantidad','clave erronea')}
            Fecha inicio:    {elemento.get('fecha_inicio','clave erronea')}
            Fecha final:     {elemento.get('fecha_final','clave erronea')}
            Estado:          {elemento.get('estado','clave erronea')}
            ''')
        
def buscar_prestamos():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        id=validar_entero("Ingrese el id a buscar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
                    ****************************
                    ID:              {elemento.get('id','clave erronea')}
                    Nombre:          {elemento.get('nombre','clave erronea')}
                    Herramienta:     {elemento.get('herramienta','clave erronea')}
                    Cantidad:        {elemento.get('cantidad','clave erronea')}
                    Fecha inicio:    {elemento.get('fecha_inicio','clave erronea')}
                    Fecha final:     {elemento.get('fecha_final','clave erronea')}
                    Estado:          {elemento.get('estado','clave erronea')}
                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)


def actualizar_prestamos():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_prestamos()
        id=validar_entero("Ingrese el id a actualizar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Fecha final
                                    2.Estado
                                    3.Observaciones   
                                    4. Cancelar
                                        ''',1,4)
                match op_actualizar:
                    case 1:
                        dias=validar_entero('Ingrese lo otros dias que necesta la herramieta:')
                        fecha_inicio= date.fromisoformat(elemento.get('fecha_inicio','clave no encontrada'))
                        fecha_nueva=fecha_inicio + timedelta(days=dias)
                        elemento.get('fecha_final','clave no encontrada')=str(fecha_nueva)
                    case 2:
                        elemento['estado']=seleccionar_estado()
                    case 3:
                        print('Operación cancelada!')
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def registrar_devoluciones():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
        return
    for elemento in registros:
        if elemento.get('estado','clave no encontrada') == 'activo' :
            print(f'''
            ID:              {elemento.get('id','clave erronea')}
            Nombre:          {elemento.get('nombre','clave erronea')}
            Herramienta:     {elemento.get('herramienta','clave erronea')}
            Cantidad:        {elemento.get('cantidad','clave erronea')}
            Fecha inicio:    {elemento.get('fecha_inicio','clave erronea')}
                    ''')   


def eliminar_prestamos():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
        return
    listar_prestamos()
    id=validar_entero("Ingrese el id a eliminar: ")
    for elemento in registros:
        if elemento.get('id', 'clave no encontrada')==id:
            print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
            registros.remove(elemento)
            guardar(NOMBRE_ARCHIVO,registros)
            return
        print('NO SE ENCONTRÓ EL ID: ',id)



 

