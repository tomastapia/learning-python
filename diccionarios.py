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