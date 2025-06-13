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
    '>=': 'mayor o igual que',
    '+=': 'asignación con suma',
    '-=': 'asignación con resta',
    '*=': 'asignación con multiplicación',
    '/=': 'asignación con división',
    'and': 'operador lógico AND',
    'or': 'operador lógico OR',
    'not': 'operador lógico NOT'
}

palabras_reservadas = {
    'if': 'condicional',
    'else': 'sino',
    'for': 'bucle for',
    'in': 'en',
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
regex_identificador = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
regex_cadena = r'^".*"|^\'.*\''

# Lista para acumular los errores encontrados
errores = []

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
        tokens[0] == 'return'
    )

def es_bucle_while(tokens):
    return (
        len(tokens) >= 4 and
        tokens[0] == 'while' and
        tokens[-1] == ':'
    )

def es_bucle_for(tokens):
    return (
        len(tokens) >= 6 and
        tokens[0] == 'for' and
        'in' in tokens and
        tokens[-1] == ':'
    )

def es_import(tokens):
    return (
        len(tokens) >= 2 and
        tokens[0] == 'import' and
        re.match(regex_identificador, tokens[1])
    )

def es_clase(tokens):
    return (
        len(tokens) >= 3 and
        tokens[0] == 'class' and
        re.match(regex_identificador, tokens[1]) and
        tokens[-1] == ':'
    )

def falta_parentesis(tokens):
    return tokens.count('(') != tokens.count(')')

def es_asignacion_compuesta(tokens):
    return (
        len(tokens) == 3 and
        re.match(regex_identificador, tokens[0]) and
        tokens[1] in ['+=', '-=', '*=', '/='] and
        (
            re.match(regex_numero, tokens[2]) or
            re.match(regex_identificador, tokens[2])
        )
    )

def es_asignacion_atributo(tokens):
    return (
        len(tokens) == 5 and
        re.match(regex_identificador, tokens[0]) and
        tokens[1] == '.' and
        re.match(regex_identificador, tokens[2]) and
        tokens[3] == '=' and
        any([
            re.match(regex_identificador, tokens[4]),
            re.match(regex_cadena, tokens[4]),
            re.match(regex_numero, tokens[4])
        ])
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
    tokens = re.findall(r'\".*?\"|\'.*?\'|\d+\.\d+|\w+|==|!=|<=|>=|\+=|-=|\*=|/=|[^\s\w]', linea)
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
    elif es_asignacion_compuesta(tokens):
        print("Asignación compuesta válida")
    elif es_asignacion_atributo(tokens):
        print("Asignación a atributo válida")
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
    elif es_bucle_while(tokens):
        print("Bucle while válido")
    elif es_bucle_for(tokens):
        print("Bucle for válido")
    elif es_import(tokens):
        print("Importación válida")
    elif es_clase(tokens):
        print("Definición de clase válida")
    else:
        errores.append(f"Línea {num_lineas}: Error de sintaxis -> {linea}")
        print("Error de sintaxis")

    # Verificación adicional de errores
    if falta_parentesis(tokens):
        errores.append(f"Línea {num_lineas}: Falta parentesis -> {linea}")
        print("Error: Falta cerrar o abrir parentesis")

    if tokens[0] in ('if', 'while', 'for', 'def', 'else') and not tokens[-1] == ':':
        errores.append(f"Línea {num_lineas}: Falta ':' al final de la estructura -> {linea}")
        print("Error: Falta ':' al final de la estructura")

# Mostrar los errores encontrados
print()
print("------------------[ RESUMEN DE ERRORES ]------------------")
if errores:
    for error in errores:
        print("🔴", error)
else:
    print("✅ No se encontraron errores de sintaxis.")