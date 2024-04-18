


playlist = {}   #DICCIONARIO VACIO
playlist["canciones"] = []  #LISTA VACIA DE CANCIONES

#FUNCION PRINCIPAL
def app():

    #Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        
        nombre_playlist = input("Nombre de la playlist:\r\n")

        if nombre_playlist == True:
            playlist["nombre"] = nombre_playlist
            agregar_playlist = False

app()