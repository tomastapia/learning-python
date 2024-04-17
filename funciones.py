def cancion(cancion = "desconocida", autor = "desconocido"):
    print(f"La canción es {cancion} del autor {autor}")


cancion("Yesterday", "The Beatles")
cancion("Anothe Brick in the Wall", "Pink Floyd")
cancion("Something in the Way", "Nirvana")
cancion("Thriller")
cancion()

#FUNCIONES QUE RETORNAN UN VALOR
def informacion(nombre):
    return nombre


empleado = informacion("Tomás")
print(empleado)