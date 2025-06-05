import random
from Inputs import *

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array

def mostrar_array(array: list) -> None:
    for i in range(len(array)):
        print(f"{array[i]}")

def mostrar_matriz(matriz: list) -> None:
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print(f"{matriz[fila][columna]}", end=" ")
        print("")

def sumar_fila(matriz_numerica: list, indice_fila: int) -> int:
    suma_fila = 0
    for columna in range(len(matriz_numerica[0])):
        suma_fila += matriz_numerica[indice_fila][columna]
    return suma_fila

def sumar_matriz(matriz_numerica: list) -> int:
    suma = 0
    for fila in range(len(matriz_numerica)):
        for columna in range(len(matriz_numerica[fila])):
            suma += matriz_numerica[fila][columna]
    return suma

def calcular_promedio(cantidad_total: float, cantidad_elementos: int) -> float:
    if cantidad_elementos != 0:
        return cantidad_total / cantidad_elementos
    return None

# Especificas

def cargar_nombres_participantes(array_nombres: list) -> bool:
    if array_nombres != None and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            nombre = validar_nombre()
            array_nombres[i] = nombre
        return True
    return False

def cargar_puntajes(matriz_puntajes: list) -> bool:
    if matriz_puntajes != None and len(matriz_puntajes) > 0:
        for fila in range(len(matriz_puntajes)):
            print(f"Ingrese los puntajes para la fila {fila + 1}:")
            for columna in range(len(matriz_puntajes[fila])):
                if columna == 0:
                    print("Ingrese puntaje jurado 1: ")
                elif columna == 1:
                    print("Ingrese puntaje jurado 2: ")
                elif columna == 2:
                    print("Ingrese puntaje jurado 3: ")
                puntaje = validar_puntaje()
                matriz_puntajes[fila][columna] = puntaje
        return True
    return False

def mostrar_participante(array_nombres: list, matriz_puntajes: list, indice: int) -> bool:
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
    if (array_nombres != None and matriz_puntajes != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        for i in range(len(array_nombres)):
            mostrar_participante(array_nombres, matriz_puntajes, i)
            print("")
        return True
    return False

def mostrar_participantes_menor_promedio(matriz_puntajes: list, array_nombres: list, promedio_minimo: float) -> bool:
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
    if matriz_puntajes != None and len(matriz_puntajes) > 0:
        cantidad_jurados = len(matriz_puntajes[0])
        array_promedios = crear_array(cantidad_jurados, 0.0)
        for i in range(cantidad_jurados):
            suma = 0
            for jurado in range(len(matriz_puntajes)):
                suma += matriz_puntajes[jurado][i]
            array_promedios[i] = calcular_promedio(suma, len(matriz_puntajes))
        return array_promedios
    return None

def jurado_mas_estricto(matriz_puntajes: list) -> list:
    if matriz_puntajes != None and len(matriz_puntajes) > 0:
        array_promedios = promedio_por_jurado(matriz_puntajes)
        if array_promedios != None:
            indice_mas_estricto = 0
            for i in range(1, len(array_promedios)):
                if array_promedios[i] < array_promedios[indice_mas_estricto]:
                    indice_mas_estricto = i
            return indice_mas_estricto
    return -1

def jurado_mas_generoso(matriz_puntajes: list) -> list:
    if matriz_puntajes != None and len(matriz_puntajes) > 0:
        array_promedios = promedio_por_jurado(matriz_puntajes)
        if array_promedios != None:
            indice_mas_generoso = 0
            for i in range(1, len(array_promedios)):
                if array_promedios[i] > array_promedios[indice_mas_generoso]:
                    indice_mas_generoso = i
            return indice_mas_generoso
    return -1

def mostrar_participantes_puntajes_iguales(array_nombres: list, matriz_puntajes: list) -> bool:
    encontrados = False
    if array_nombres and matriz_puntajes:
        for i in range(len(matriz_puntajes)):
            if matriz_puntajes[i][0] == matriz_puntajes[i][1] == matriz_puntajes[i][2]:
                mostrar_participante(array_nombres, matriz_puntajes, i)
                print("")
                encontrados = True
    if not encontrados:
        print("No hay participantes con puntajes iguales entre los tres jurados.")
    return encontrados

def buscar_participante_por_nombre(array_nombres: list, matriz_puntajes: list, nombre: str) -> bool:
    if array_nombres and matriz_puntajes:
        for i in range(len(array_nombres)):
            if array_nombres[i].lower() == nombre.lower():
                mostrar_participante(array_nombres, matriz_puntajes, i)
                return True
    print("No existe un participante con ese nombre.")
    return False

def mostrar_top_3_participantes(array_nombres: list, matriz_puntajes: list) -> bool:
    if array_nombres and matriz_puntajes and len(array_nombres) >= 3:
        promedios = [0] * len(array_nombres)
        for i in range(len(array_nombres)):
            promedios[i] = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
        # Crear lista de índices
        indices = list(range(len(array_nombres)))
        # Ordenar índices según los promedios (de mayor a menor)
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                if promedios[indices[j]] > promedios[indices[i]]:
                    aux = indices[i]
                    indices[i] = indices[j]
                    indices[j] = aux
        print("Top 3 participantes con mayor puntaje promedio:")
        for k in range(3):
            mostrar_participante(array_nombres, matriz_puntajes, indices[k])
            print("")
        return True
    print("No hay suficientes participantes para mostrar el Top 3.")
    return False

def participantes_ordenados_alfabeticamente(array_nombres: list, matriz_puntajes: list) -> bool:
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        indices = list(range(len(array_nombres)))

        for i in range(len(indices)):
            for j in range(len(indices) - i - 1):
                if array_nombres[indices[j]].lower() > array_nombres[indices[j + 1]].lower():
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]

        for i in indices:
            mostrar_participante(array_nombres, matriz_puntajes, i)
            print("")
        return True
    return False

def mostrar_ganador(array_nombres: list, matriz_puntajes: list) -> bool:
    if array_nombres and matriz_puntajes:
        promedios = [0] * len(array_nombres)
        for i in range(len(array_nombres)):
            promedios[i] = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
        # Buscar el mayor promedio
        max_promedio = promedios[0]
        for i in range(1, len(promedios)):
            if promedios[i] > max_promedio:
                max_promedio = promedios[i]
        # Contar cuántos tienen el mayor promedio
        cantidad_ganadores = 0
        indice_ganador = -1
        for i in range(len(promedios)):
            if promedios[i] == max_promedio:
                cantidad_ganadores += 1
                indice_ganador = i
        if cantidad_ganadores == 1:
            print("El ganador es:")
            mostrar_participante(array_nombres, matriz_puntajes, indice_ganador)
            return True
        else:
            print("Hay más de un participante con el mayor puntaje promedio. Debe realizarse un desempate.")
            return False
    print("No hay participantes para mostrar ganador.")
    return False

def desempatar(array_nombres: list, matriz_puntajes: list) -> bool:
    if array_nombres and matriz_puntajes:
        promedios = [0] * len(array_nombres)
        for i in range(len(array_nombres)):
            promedios[i] = calcular_promedio(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))
        # Buscar el mayor promedio
        max_promedio = promedios[0]
        for i in range(1, len(promedios)):
            if promedios[i] > max_promedio:
                max_promedio = promedios[i]
        # Guardar los índices de los ganadores
        indices_ganadores = [0] * len(array_nombres)
        cantidad_ganadores = 0
        for i in range(len(promedios)):
            if promedios[i] == max_promedio:
                indices_ganadores[cantidad_ganadores] = i
                cantidad_ganadores += 1
        if cantidad_ganadores > 1:
            elegido = random.randint(0, cantidad_ganadores - 1)
            print("El ganador por desempate es:")
            mostrar_participante(array_nombres, matriz_puntajes, indices_ganadores[elegido])
            return True
        else:
            print("No hay empate para desempatar.")
            return False
    print("No hay participantes para desempatar.")
    return False

