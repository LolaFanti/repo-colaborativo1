

def registrar_habitos():
    actividad= input("Ingresar actividad: ")
    lista= []
    lista.append(actividad)
    agregar= input("queres ptra?")
    while agregar== "SI" :
        actividad= input("Ingresar actividad: ")
        lista= []
        lista.append(actividad)
        agregar= input("Queres agregar otra actividad?")
    return lista

def  analizar_habitos(lista):
    actividades = {}
    for act in lista:
        if act not in actividades.keys():
            actividades[act] = 1
        elif act in actividades.keys():
            actividades[act] = actividades[act] + 1
    return actividades 
        
    
    
    