# CONDICIONALES
dinero_cliente = 690
if dinero_cliente >= 500:
    print("Compra aceptada")
else:
    print("Compra rechazada")


# Ejemplo con likes
likes = 220
if likes >= 200:
    print("Felicidades, alcazaste los 200 likes")
else:
    print("No alcanzaste, sigue intentandolo")


# Ejemplo con Strings
perfil_usuario = "Nicole"
if not perfil_usuario == "Tomás": # IF NOT para negar un valor
    print("El usuario es incorrecto")


# Ejemplo con booleano
perfil_autenticado = True
if perfil_autenticado: # Sin operadores, por defecto intenta verificar boleanos true
    print("Usuario verificado")
else:
    print("Usuario rechazado")


# Ejemplo para evaluar elementos de una lista
carrito = ["Monitor", "Laptop", "Celular", "IPad"]


if "IPad" in carrito:
    print("El producto está en el carrito")
else:
    print("El producto no está en el carrito")


# Ejemplo de IF's anidados
usuario_verificado = True
usuario_admin = True


if usuario_verificado: # Sin operadores, por defecto intenta verificar boleanos true
    print("Usuario verificado")
    if usuario_admin: # Sin operadores, por defecto intenta verificar boleanos true
        print("Tienes acceso como administrador")
    else:
        print("Tienes acceso")
else:
    print("Usuario no verificado")


# Ejemplo de ELIF
ocupacion = "Jubilado"


if ocupacion == "Estudiante":
    print("Tienes un descuento del 30%")
elif ocupacion == "Jubilado":
    print("Tienes un descuento del 50%")
elif ocupacion == "desempleado":
    print("Tienes un descuento del 10%")
else:
    print("No tienes descuentos disponibles")


#Operador AND y OR
usuario_log = True
usuario_admin = False


# OR:   una condicion es suficiente para que cumpla
# AND:  para que dos o más condiciones se cumplan


if usuario_log and usuario_admin:
    print("Inicio de sesión exitoso")
elif usuario_log:
    print("Inicio exitoso")
else:
    print("No se ha podido iniciar sesión")


# Condicionales y FOR en un Array (List)
idiomas = ["Español", "Chino", "Inglés", "Frances", "Italiano", "Mandarin"]


for idioma in idiomas:
    if idioma == "Chino" or idioma == "Mandarin":
        print(f"Idioma {idioma} disponible")
    else:
        print(f"Idioma {idioma} no disponible")
