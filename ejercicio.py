playlist = {}   #DICCIONARIO VACIO
playlist["canciones"] = []  #LISTA VACIA DE CANCIONES

#FUNCION PRINCIPAL
def app():
    #Agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input("Nombre de la playlist:\r\n")
        if nombre_playlist:
            playlist["nombre"] = nombre_playlist
            # Ya tenemos el nombre, desacticar el True
            agregar_playlist = False
            # Mandar llamar la funcion para agregar canciones
            agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #Preguntar que cancion desea agregar
        nombre_playlist = playlist["nombre"]
        pregunta = f"\r\nAgrega canciones a la playlist {nombre_playlist} \r\n"
        pregunta += 'Escribe "cerrar" para dejar de agregar canciones \r\n'
        cancion = input(pregunta)
        if cancion == "cerrar":
            #Para dejar de agregar canciones
            agregar_cancion = False
            #Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            #Agregar las canciones al playlist
            playlist["canciones"].append(cancion) #.append agrega elementos a la lista
            print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist["nombre"]
    print(f"Playlist: {nombre_playlist}\r\n")
    print("Canciones:\r\n")
    for cancion in playlist["canciones"]:
        print(cancion)
app()

