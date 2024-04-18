

# WHILE ---> Se ejecuta mientras que una condición sea verdadera
# FOR ---> Se ejecuta al menos una vez por cada elemento

pregunta = "Coloca un numero y te diré si es par o impar.\r\n"
pregunta += 'Escribe "cerrar" para salir:\r\n' # Para concatenar variable
preguntar = True

while preguntar:
    
    numero = input(pregunta)

    if numero == "cerrar":
        preguntar == False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f"El número {numero} es par")
        else:
            print(f"El número {numero} es impar")