# repo-colaborativo
actividades = []

while True:
    actividad = input("Ingresa una actividad (o escribe 'fin' para terminar): ")
    
    if actividad == "fin":
        break
    
    actividades.append(actividad)

resumen = {}

for act in actividades:
    if act in resumen:
        resumen[act] += 1
    else:
        resumen[act] = 1

print("\nResumen del día:")
for act, cantidad in resumen.items():
    print(act, ":", cantidad)
