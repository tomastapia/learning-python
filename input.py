#INPUT (ENTRADA DE DATOS)
nombre = input("Coloca tu nombre:\r\n") # \r\n : Salto de linea en consola/terminal
print(f"Hola {nombre}")

#Leer datos numéricos
edad = input("Coloca tu edad:\r\n")
#Convertir edad (string) a int (número entero) - str (string) - float
edad = int(edad)

if edad >= 18:
    print("Puedes acceder")
else:
    print("No tienes la edad suficiente")

#Mezclando operadores

numero = input("Coloca un numero y te diré si es par o impar:\r\n")
numero = int(numero)

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

