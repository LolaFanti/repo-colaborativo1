

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
        
    
    
    