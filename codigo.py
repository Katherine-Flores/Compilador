# Esto es un comentario

# Asignaciones válidas
x = 10
y = 20.5
suma = x + y

# If y else válidos
if suma >= 30:
    print("Mayor o igual a 30")
else:
    print("Menor a 30")

# Función válida
def saludar(nombre):
    return "Hola " + nombre

# Llamada válida
mensaje = saludar("Katherine")

# Bucle for válido
for i in range(5):
    print(i)

# Bucle while válido
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Clase válida
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Operadores lógicos válidos
if x > 5 and y < 100:
    print("Ambas condiciones se cumplen")

# ERRORES

@error = 10               # Token no reconocido
def sumar(                # Paréntesis sin cerrar y falta ':'
if x > y                  # Falta los dos puntos
print("Hola"              # Falta el parentesis que cierra
x == 10                   # Comparación fuera de una condición
for i in range(5)         # Falta ':'
while contador < 5        # Falta ':'
class Estudiante          # Falta ':'
def (nombre):             # Identificador inválido para nombre de función
if x or:                  # Error en estructura lógica
