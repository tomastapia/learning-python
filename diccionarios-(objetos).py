# DICCIONARIOS (Objetos en otros lenguajes)
estudiante_a = {
    "nombre" : "Nicole",    # "Llaves" : "Valores",
    "apellido" : "López",
    "edad" : 28,
    "empleo" : "Auditoría",
    "estudia" : "Idioma Chino",
    }

# Acceder a los elementos del diccionario
print(estudiante_a["nombre"])
print(estudiante_a["edad"])

# Mezclar con un String, se debe añadir una variable
nombre_estudiante = estudiante_a["nombre"]
print(f"El nombre del estudiante es {nombre_estudiante}")

# Agregar nuevos valores
estudiante_a["Certificado"] = "HSK"
print(estudiante_a)

# Reemplazar valor existente
estudiante_a["empleo"] = "Facturadora"
print(estudiante_a)

# Eliminar valores
del estudiante_a["apellido"]
print(estudiante_a)

# <------------------------------------------------------------------------>

# INICIAR UN DICCIONARIO VACIO
jugador = {}
print(jugador)

# Se une un jugador
jugador ["nombre"] = "Tomás"
print(jugador)

# Agregando puntaje
jugador ["puntaje"] = 0
print(jugador)
# incrementando puntaje
jugador ["puntaje"] = 100
print(jugador)

# Acceder a un valor
print(jugador.get("puntaje"))
print(jugador.get("juego", "Juego no especificado")) # Si no encuentra el valor, se puede personalizar el mensaje despues del ","

# ITERAR EN EL DICCIONARIO
for llave, valor in jugador.items():
    print(llave)
    print(valor)

# Eliminar valores
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)