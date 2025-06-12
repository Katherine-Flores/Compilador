# Nombre: Katherine Nayelhi Flores Figueroa
# Carnet: 0909-22-1883
import re

print()
print("------------------[ ANALIZADOR LEXICO Y SINTACTICO ]------------------")

# Diccionarios de tokens
operadores = {
    '+': 'suma',
    '-': 'resta',
    '*': 'multiplicación',
    '/': 'división',
    '=': 'asignación',
    '==': 'igualdad',
    '!=': 'diferente',
    '<': 'menor que',
    '>': 'mayor que',
    '<=': 'menor o igual que',
    '>=': 'mayor o igual que'
}

palabras_reservadas = {
    'if': 'condicional',
    'else': 'sino',
    'for': 'bucle for',
    'while': 'bucle while',
    'def': 'definición de función',
    'return': 'retorno',
    'class': 'definición de clase',
    'import': 'importación',
    'from': 'desde',
    'as': 'alias',
    'print': 'imprimir en pantalla'
}

datos = {
    'int': 'int',
    'float': 'float',
    'str': 'str',
    'bool': 'bool',
    'list': 'list',
    'dict': 'dict'
}

simbolo_puntuacion = {
    ':': 'dos puntos',
    ';': 'punto y coma',
    '.': 'punto',
    ',': 'coma',
    '(': 'parentesis que abre',
    ')': 'parentesis que cierra'
}

# Expresiones Regulares
regex_numero = r'^\d+(\.\d+)?$'
regex_identificador = r'^[a-zA-Z]+$'
regex_cadena = r'^".*"|^\'.*\''

# Definir las reglas de producción
def es_asignacion(tokens):
    return (
        len(tokens) >= 3 and
        re.match(regex_identificador, tokens[0]) and
        tokens[1] == '='
    )

def es_condicional(tokens):
    return (
        len(tokens) >= 4 and
        tokens[0] == 'if' and
        tokens[-1] == ':'  # termina con dos puntos
    )

def es_else(tokens):
    return (
        len(tokens) == 2 and
        tokens[0] == 'else' and
        tokens[1] == ':'
    )

def es_llamada_funcion(tokens):
    return (
        len(tokens) >= 3 and
        re.match(regex_identificador, tokens[0]) and
        tokens[1] == '(' and
        tokens[-1] == ')'
    )

def es_definicion_funcion(tokens):
    return (
        len(tokens) >= 6 and
        tokens[0] == 'def' and
        re.match(regex_identificador, tokens[1]) and
        tokens[2] == '(' and
        tokens[-2] == ')' and
        tokens[-1] == ':'
    )

def es_return(tokens):
    return (
        len(tokens) >= 2 and
        tokens[0] == 'return' and
        re.match(regex_identificador, tokens[1])
    )

# Leer el archivo que se estará analizando
with open("codigo.py") as archivo:
    lineas = archivo.readlines()

# Analizar las lineas
for num_lineas, linea in enumerate(lineas, start=1):

    # Ignorar comentarios y lineas en blanco
    linea = linea.split("#")[0].strip()
    if not linea:
        continue

    print(f"\nLinea {num_lineas}: {linea.strip()}")
    tokens = re.findall(r'\".*?\"|\'.*?\'|\d+\.\d+|\w+|==|!=|<=|>=|[^\s\w]', linea)
    print("Tokens: ", tokens)

    # Analizador Lexico
    for token in tokens:
        if token in operadores:
            print(f"Operador: {token} => {operadores[token]}")
        elif token in simbolo_puntuacion:
            print(f"Símbolo de puntuación: {token} => {simbolo_puntuacion[token]}")
        elif token in palabras_reservadas:
            print(f"Palabra reservada: {token} => {palabras_reservadas[token]}")
        elif token in datos:
            print(f"Tipo de dato: {token} => {datos[token]}")
        elif re.match(regex_numero, token):
            print(f"Número: {token}")
        elif re.match(regex_cadena, token):
            print(f"Cadena: {token}")
        elif re.match(regex_identificador, token):
            print(f"Identificador: {token}")
        else:
            print(f"Token no reconocido: {token}")

    # Analizador Sintactico
    if es_asignacion(tokens):
        print("Asignación válida")
    elif es_condicional(tokens):
        print("Condicional válida")
    elif es_else(tokens):
        print("Else válido")
    elif es_llamada_funcion(tokens):
        print("Llamada a función válida")
    elif es_definicion_funcion(tokens):
        print("Definición de función válida")
    elif es_return(tokens):
        print("Sentencia return válida")
    else:
        print("Error de sintaxis")