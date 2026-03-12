

def registrar_habitos():
    '''
    Pide al usuario ingresar una actividad y las agrega a una lista, hasta 
    que el usaurio no quiera agregar mas actividades.
    Returns
    -------
    lista : List
        Contiene la lista de las actividades realizadas por el usuario.

    '''
    actividad= input("Ingresar actividad: ")
    lista= []
    lista.append(actividad)
    agregar= input("Queres agregar otra actividad?")
    while agregar== "si" :
        actividad= input("Ingresar actividad: ")
        lista= []
        lista.append(actividad)
        agregar= input("Queres agregar otra actividad?")
    return lista

def  analizar_habitos(lista):
    '''
    Recibe las actividades ingresadas por el usuario, crea un diccionario cuyas llaves 
    son las actividades y las calves cantas veces estan.

    Parameters
    ----------
    lista : List
        Contiene la lista de las actividades realizadas por el usuario.

    Returns
    -------
    actividades : Dict
        Contiene la cantidad de veces que se realizo cada actividad.

    '''
    actividades = {}
    for act in lista:
        if act not in actividades.keys():
            actividades[act] = 1
        elif act in actividades.keys():
            actividades[act] = actividades[act] + 1
    return actividades 
        
    
    
    