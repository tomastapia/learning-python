# ARREGLOS O LISTAS
lenguajes = ["Español", "Chino", "Inglés", "Frances", "Italiano"]
print(lenguajes)

# Accediendo a un elemento del array
print(lenguajes[2])

# Ordenar elementos por orden alfabetico
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento junto a un string
aprendiendo =  f"Estoy aprendiendo el idioma {lenguajes[0]}"
print(aprendiendo)

# Reemplazar un elemento del array (list)
lenguajes[2] = "Alemán"
print(lenguajes)

# Agregar un elemento al array (list)
lenguajes.append("Mandarín")
print(lenguajes)

# Eliminar un elemento del array (list)
del lenguajes[5]
print(lenguajes)

# ELIMINAR USANDO .pop
# Eliminar ultimo elemento de un array (list)
lenguajes.pop() # .pop elimina el último elemento por defecto
print(lenguajes)
# Eliminar con .pop un elemento especifico de un array (list)
lenguajes.pop(3)
print(lenguajes)


# Eliminar por string o numero
lenguajes.remove("Alemán")
print(lenguajes)