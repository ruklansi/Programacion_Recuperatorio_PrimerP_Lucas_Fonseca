import random
from Inputs import *

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """
    Crea una matriz de filas x columnas con un valor inicial.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    """
    Crea un array de tamaño especificado con un valor inicial.
    """
    array = [valor_inicial] * cantidad_elementos
    return array

def mostrar_array(array: list) -> None:
    """
    Muestra los elementos de un array.
    """
    for i in range(len(array)):
        print(f"{array[i]}")

def mostrar_matriz(matriz: list) -> None:
    """
    Muestra los elementos de una matriz.
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}", end=" ")
        print("")

def sumar_fila(matriz_numerica, indice_fila):
    suma_fila = 0
    for col in range(len(matriz_numerica[indice_fila])):
        suma_fila += int(matriz_numerica[indice_fila][col])  # Convertir a int por si acaso
    return suma_fila

def sumar_matriz(matriz_numerica: list) -> int | float:
    """
    Suma todos los elementos numéricos de la matriz.
    Asume que los elementos son números (validados en Inputs.py).
    """
    suma = 0
    for fil in range(len(matriz_numerica)):
        for col in range(len(matriz_numerica[fil])):
            suma += matriz_numerica[fil][col]
    return suma

def calcular_promedio(cantidad_total: float, cantidad_elementos: int) -> float:
    """
    Calcula el promedio de una cantidad total entre un número de elementos.
    Retorna None si cantidad_elementos es 0.
    """
    if cantidad_elementos != 0:
        return cantidad_total / cantidad_elementos
    return None

# ESPECÍFICAS
def cargar_nombres_participantes(array_nombres: list) -> bool:
    """
    Carga nombres de participantes en el array usando validar_nombre.
    """    
    if array_nombres != None and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            nombre = validar_nombre()
            array_nombres[i] = nombre
        return True
    return False

def cargar_puntajes(matriz_puntajes: list) -> bool:
    """
    Carga puntajes de jurados para cada participante usando validar_puntaje.
    """ 
    if matriz_puntajes != None and len(matriz_puntajes) > 0:
        for fil in range(len(matriz_puntajes)):
            print(f"\nCargando puntajes para el participante {fil + 1}:")
            for col in range(len(matriz_puntajes[fil])):
                puntaje = validar_puntaje()
                matriz_puntajes[fil][col] = puntaje
        return True
    return False

def mostrar_participante(array_nombres: list, matriz_puntajes: list, indice: int) -> bool:
    """
    Muestra los datos de un participante: nombre, puntajes y promedio.
    """
    if (array_nombres != None and matriz_puntajes != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0 and 0 <= indice < len(array_nombres)):
        promedio = calcular_promedio(sumar_fila(matriz_puntajes, indice), len(matriz_puntajes[0]))
        print(f"NOMBRE PARTICIPANTE: {array_nombres[indice]}")
        for col in range(len(matriz_puntajes[indice])):
            print(f"PUNTAJE JURADO {col + 1}: {matriz_puntajes[indice][col]}")
        print(f"PUNTAJE PROMEDIO: {round(promedio, 2)}/10")
        return True
    return False

def mostrar_puntajes(array_nombres: list, matriz_puntajes: list) -> bool:
    """
    Muestra los datos de todos los participantes.
    """
    if (array_nombres != None and matriz_puntajes != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        for i in range(len(array_nombres)):
            mostrar_participante(array_nombres, matriz_puntajes, i)
            print("")
        return True
    return False

def mostrar_participantes_menor_promedio(matriz_puntajes: list, array_nombres: list, promedio_minimo: float) -> bool:
    """
    Muestra participantes con promedio menor al especificado.
    """
    retorno = False
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        for i in range(len(matriz_puntajes)):
            promedio = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
            if promedio < promedio_minimo:
                mostrar_participante(array_nombres, matriz_puntajes, i)
                print("")
                retorno = True
    return retorno

def promedio_por_jurado(matriz_puntajes: list) -> list:
    """
    Calcula el promedio de puntajes otorgados por cada jurado.
    """
    if matriz_puntajes is not None and len(matriz_puntajes) > 0:
        cantidad_jurados = len(matriz_puntajes[0])
        promedios = [0] * cantidad_jurados
        for col in range(cantidad_jurados):
            suma = 0
            for fil in range(len(matriz_puntajes)):
                suma += matriz_puntajes[fil][col]
            promedio = calcular_promedio(suma, len(matriz_puntajes))
            # Redondeo manual a 2 decimales
            promedio_redondeado = int(promedio * 100 + 0.5) / 100
            promedios[col] = promedio_redondeado
        return promedios
    return []

def jurado_mas_estricto(matriz_puntajes: list) -> list:
    """
    Retorna los índices de los jurados con menor promedio (puede haber más de uno).
    """
    promedios = promedio_por_jurado(matriz_puntajes)
    if len(promedios) == 0:
        return []
    min_promedio = promedios[0]
    for prom in promedios:
        if prom < min_promedio:
            min_promedio = prom
    return [i + 1 for i in range(len(promedios)) if promedios[i] == min_promedio]

def jurado_mas_generoso(matriz_puntajes: list) -> list:
    """
    Retorna los índices de los jurados con mayor promedio (puede haber más de uno).
    """
    promedios = promedio_por_jurado(matriz_puntajes)
    if len(promedios) == 0:
        return []
    max_promedio = promedios[0]
    for prom in promedios:
        if prom > max_promedio:
            max_promedio = prom
    return [i + 1 for i in range(len(promedios)) if promedios[i] == max_promedio]

def participantes_puntajes_iguales(matriz_puntajes: list, array_nombres: list) -> bool:
    """
    Muestra participantes con los mismos puntajes de los tres jurados.
    """
    retorno = False
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        for i in range(len(matriz_puntajes)):
            if matriz_puntajes[i][0] == matriz_puntajes[i][1] == matriz_puntajes[i][2]:
                mostrar_participante(array_nombres, matriz_puntajes, i)
                print("")
                retorno = True
    return retorno

def buscar_participante_por_nombre(array_nombres: list, matriz_puntajes: list, nombre: str) -> bool:
    """
    Busca un participante por nombre y muestra sus datos.
    """
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        for i in range(len(array_nombres)):
            if array_nombres[i].lower() == nombre.lower():
                mostrar_participante(array_nombres, matriz_puntajes, i)
                return True
    return False

# PUNTOS EXTRA
def top_3_participantes(array_nombres: list, matriz_puntajes: list) -> bool:
    """
    Muestra los 3 participantes con mayor promedio usando ordenamiento manual.
    (Sin usar append ni métodos de listas)
    """
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        # Crear lista de tuplas (índice, promedio) sin append
        promedios = [None] * len(array_nombres)
        for i in range(len(array_nombres)):
            promedio = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
            promedios[i] = (i, promedio)
        
        # Ordenamiento burbujeo (descendente por promedio)
        for i in range(len(promedios)):
            for j in range(len(promedios) - i - 1):
                if promedios[j][1] < promedios[j + 1][1]:
                    promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
        
        # Mostrar hasta 3 participantes
        cantidad = 3 if len(promedios) > 3 else len(promedios)
        for i in range(cantidad):
            mostrar_participante(array_nombres, matriz_puntajes, promedios[i][0])
            print("")
        return True
    return False

def participantes_ordenados_alfabeticamente(array_nombres: list, matriz_puntajes: list) -> bool:
    """
    Muestra los participantes ordenados alfabéticamente con sus datos usando ordenamiento manual.
    """
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        # Crear lista de índices
        indices = list(range(len(array_nombres)))
        
        # Ordenamiento burbujeo (alfabético por nombre)
        for i in range(len(indices)):
            for j in range(len(indices) - i - 1):
                if array_nombres[indices[j]].lower() > array_nombres[indices[j + 1]].lower():
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]
        
        # Mostrar participantes en orden
        for i in indices:
            mostrar_participante(array_nombres, matriz_puntajes, i)
            print("")
        return True
    return False

def mostrar_ganador(array_nombres: list, matriz_puntajes: list) -> list:
    """
    Muestra el participante ganador (mayor promedio). Retorna lista de tuplas (índice, promedio) de ganadores.
    """
    if array_nombres and matriz_puntajes:
        promedios = [0] * len(array_nombres)
        for i in range(len(array_nombres)):
            promedios[i] = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
        
        # Buscar el mayor promedio manualmente
        max_promedio = promedios[0]
        for prom in promedios:
            if prom > max_promedio:
                max_promedio = prom
        
        # Recolectar índices de participantes con el mayor promedio
        ganadores = []
        contador = 0
        for i in range(len(promedios)):
            if promedios[i] == max_promedio:
                ganadores += [(i, max_promedio)]  # Usar concatenación en lugar de append
                contador += 1
        
        # Mostrar resultado
        if contador == 1:
            print("El ganador es:")
            mostrar_participante(array_nombres, matriz_puntajes, ganadores[0][0])
        else:
            print("Hay más de un participante con el mayor puntaje promedio. Debe realizarse un desempate.")
        
        return ganadores
    print("No hay participantes para mostrar ganador.")
    return []

def desempatar(array_nombres: list, matriz_puntajes: list) -> tuple:
    """
    Realiza un desempate aleatorio entre participantes con el mayor promedio.
    Retorna tupla (índice, promedio) del ganador o None si no hay empate.
    """
    if array_nombres and matriz_puntajes:
        promedios = [0] * len(array_nombres)
        for i in range(len(array_nombres)):
            promedios[i] = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
        
        # Buscar el mayor promedio
        max_promedio = promedios[0]
        for prom in promedios:
            if prom > max_promedio:
                max_promedio = prom
        
        # Recolectar índices de ganadores
        indices_ganadores = []
        contador = 0
        for i in range(len(promedios)):
            if promedios[i] == max_promedio:
                indices_ganadores += [i]  # Usar concatenación en lugar de append
                contador += 1
        
        if contador > 1:
            # Elegir aleatoriamente un ganador
            elegido = random.randint(0, contador - 1)
            print("El ganador por desempate es:")
            mostrar_participante(array_nombres, matriz_puntajes, indices_ganadores[elegido])
            return (indices_ganadores[elegido], max_promedio)
        else:
            print("No hay empate para desempatar.")
            return None
    print("No hay participantes para desempatar.")
    return None

