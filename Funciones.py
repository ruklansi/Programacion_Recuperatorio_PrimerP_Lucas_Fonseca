import random
from Inputs import *

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """Crea una matriz de filas x columnas con un valor inicial.
    Esta función genera una matriz (lista de listas) donde cada elemento es igual al valor inicial proporcionado.
    La matriz se construye iterando sobre la cantidad de filas y columnas especificadas, creando una fila con el valor inicial repetido.
    
    Args:
        cantidad_filas (int): Cantidad de filas de la matriz.
        cantidad_columnas (int): Cantidad de columnas de la matriz.
        valor_inicial (any): Valor inicial para cada elemento de la matriz.

    Returns:
        list: Retorna una matriz (lista de listas) con el valor inicial en cada posición.
    """    
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    """Crea un array de tamaño especificado con un valor inicial.
    Esta función genera un array (lista) donde cada elemento es igual al valor inicial proporcionado.
    El array se construye utilizando una comprensión de lista que repite el valor inicial la cantidad de veces especificada.
    
    Args:
        cantidad_elementos (int): Cantidad de elementos del array.
        valor_inicial (any): Valor inicial para cada elemento del array.

    Returns:
        list: Retorna un array (lista) con el valor inicial en cada posición.
    """    
    array = [valor_inicial] * cantidad_elementos
    return array

def mostrar_array(array: list) -> None:
    """Muestra los elementos de un array.
    Esta función itera sobre los elementos del array y los imprime en la consola.
    Si el array está vacío, no se mostrará nada.

    Args:
        array (list): Array a mostrar.
    """    
    for i in range(len(array)):
        print(f"{array[i]}")

def mostrar_matriz(matriz: list) -> None:
    """Muestra los elementos de una matriz.
    Esta función itera sobre las filas y columnas de la matriz, imprimiendo cada elemento en su posición correspondiente.
    Si la matriz está vacía, no se mostrará nada.
    Muestra los elementos de una matriz en formato de tabla, separando los elementos por espacios.

    Args:
        matriz (list): Matriz a mostrar.
    """    
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}", end=" ")
        print("")

def sumar_fila(matriz_numerica, indice_fila):
    """Suma los elementos de una fila específica de una matriz numérica.
    Esta función toma una matriz numérica y un índice de fila, y calcula la suma de todos los elementos en esa fila.
    Asume que los elementos de la matriz son números (validados en Inputs.py).
    Si el índice de fila es inválido, la función no realizará ninguna operación y retornará 0.
    La suma se realiza iterando sobre cada columna de la fila especificada y acumulando el valor de cada elemento.
    Si la fila está vacía, la suma será 0.
    La función retorna la suma total de los elementos de la fila.

    Args:
        matriz_numerica (_type_): Matriz numérica de la cual se sumarán los elementos.
        indice_fila (_type_): Índice de la fila a sumar.

    Returns:
        _type_: Retorna la suma de los elementos de la fila especificada.
    """    
    suma_fila = 0
    for col in range(len(matriz_numerica[indice_fila])):
        suma_fila += int(matriz_numerica[indice_fila][col])  # Convertir a int por si acaso
    return suma_fila

def sumar_matriz(matriz_numerica: list) -> int | float:
    """Suma todos los elementos numéricos de una matriz.
    Esta función toma una matriz numérica y calcula la suma de todos sus elementos.
    Asume que los elementos de la matriz son números (validados en Inputs.py).
    Si la matriz está vacía, la suma será 0.
    La suma se realiza iterando sobre cada fila y columna de la matriz, acumulando el valor de cada elemento.
    Si la matriz contiene elementos no numéricos, se debe asegurar que todos los elementos sean números antes de llamar a esta función.
    La función retorna la suma total de todos los elementos de la matriz.

    Args:
        matriz_numerica (list): Matriz numérica de la cual se sumarán los elementos.

    Returns:
        int | float: Retorna la suma total de los elementos de la matriz.
    """    
    suma = 0
    for fil in range(len(matriz_numerica)):
        for col in range(len(matriz_numerica[fil])):
            suma += matriz_numerica[fil][col]
    return suma

def calcular_promedio(cantidad_total: float, cantidad_elementos: int) -> float:
    """Calcula el promedio de una cantidad total entre un número de elementos.
    Esta función toma una cantidad total y un número de elementos, y calcula el promedio dividiendo la cantidad total por la cantidad de elementos.
    Si la cantidad de elementos es 0, la función retorna None para evitar una división por cero.
    La función asume que la cantidad total es un número (int o float) y la cantidad de elementos es un entero.
    Si la cantidad de elementos es mayor que 0, se realiza la división y se retorna el resultado.
    Si la cantidad de elementos es 0, se retorna None.

    Args:
        cantidad_total (float): Descripción de la cantidad total a promediar.
        cantidad_elementos (int): Descripción del número de elementos entre los cuales se promediará la cantidad total.

    Returns:
        float: Retorna el promedio de la cantidad total entre el número de elementos.
    """    
    if cantidad_elementos != 0:
        return cantidad_total / cantidad_elementos
    return None

# ESPECÍFICAS
def cargar_nombres_participantes(array_nombres: list) -> bool:
    """Carga los nombres de los participantes en el array.
    Esta función solicita al usuario que ingrese los nombres de los participantes y los valida usando la función validar_nombre.
    Cada nombre ingresado se almacena en el array proporcionado.
    Si el array es válido y tiene al menos un elemento, se itera sobre cada posición del array y se solicita un nombre.
    Si el nombre es válido, se almacena en la posición correspondiente del array.
    Si el array es None o está vacío, la función retorna False.
    Si se cargan los nombres correctamente, la función retorna True.

    Args:
        array_nombres (list): Array donde se almacenarán los nombres de los participantes.
    Returns:
        bool: Retorna True si se cargan los nombres correctamente, False si el array es None o está vacío.
    """       
    if array_nombres != None and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            nombre = validar_nombre()
            array_nombres[i] = nombre
        return True
    return False

def cargar_puntajes(matriz_puntajes: list) -> bool:
    """Carga los puntajes de los jurados para cada participante.
    Esta función solicita al usuario que ingrese los puntajes de los jurados para cada participante.
    Utiliza la función validar_puntaje para asegurarse de que los puntajes estén dentro del rango permitido (1 a 10).
    Si la matriz de puntajes es válida y tiene al menos una fila, se itera sobre cada fila (participante) y cada columna (jurado).
    En cada iteración, se solicita un puntaje al usuario y se almacena en la posición correspondiente de la matriz.
    Si la matriz es None o está vacía, la función retorna False.
    Si se cargan los puntajes correctamente, la función retorna True.

    Args:
        matriz_puntajes (list): Matriz donde se almacenarán los puntajes de los jurados para cada participante.

    Returns:
        bool: Retorna True si se cargan los puntajes correctamente, False si la matriz es None o está vacía.
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
    """Muestra los datos de un participante específico.
    Esta función imprime el nombre del participante, los puntajes otorgados por cada jurado y el promedio de esos puntajes.
    Utiliza la función sumar_fila para obtener la suma de los puntajes del participante y calcular el promedio.
    Si el array de nombres y la matriz de puntajes son válidos, y el índice está dentro del rango de participantes,
    se muestra la información del participante.
    Si el array de nombres o la matriz de puntajes son None, están vacíos o el índice es inválido, la función no realizará ninguna operación y retornará False.
    La función retorna True si se muestra la información correctamente, o False si no se pudo mostrar.

    Args:
        array_nombres (list): Contiene los nombres de los participantes.
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.
        indice (int): Índice del participante a mostrar.

    Returns:
        bool: Retorna True si se muestra la información correctamente, False si no se pudo mostrar.
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
    """Muestra los datos de todos los participantes.
    Esta función itera sobre todos los participantes y muestra su nombre, los puntajes otorgados por cada jurado y el promedio de esos puntajes.
    Si el array de nombres y la matriz de puntajes son válidos, y tienen al menos un participante,
    se muestra la información de cada participante.
    Si el array de nombres o la matriz de puntajes son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará False.
    La función retorna True si se muestran los datos de todos los participantes correctamente, o False si no se pudo mostrar.
    Muestra los datos de todos los participantes, incluyendo sus nombres y puntajes otorgados por los jurados.

    Args:
        array_nombres (list): Muestra los nombres de los participantes.
        matriz_puntajes (list): Muestra los puntajes otorgados por los jurados a cada participante.

    Returns:
        bool: Retorna True si se muestran los datos correctamente, False si no se pudo mostrar.
    """    
    if (array_nombres != None and matriz_puntajes != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        for i in range(len(array_nombres)):
            mostrar_participante(array_nombres, matriz_puntajes, i)
            print("")
        return True
    return False

def mostrar_participantes_menor_promedio(matriz_puntajes: list, array_nombres: list, promedio_minimo: float) -> bool:
    """Muestra los participantes con un promedio menor al especificado.
    Esta función itera sobre los participantes y calcula el promedio de sus puntajes.
    Si el promedio de un participante es menor al promedio mínimo especificado, se muestra su información.
    Si la matriz de puntajes y el array de nombres son válidos, y tienen al menos un participante,
    se muestra la información de los participantes que cumplen con la condición.
    Si la matriz de puntajes o el array de nombres son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará False.
    La función retorna True si se muestran los participantes con promedio menor al especificado, o False si no se pudo mostrar.
    Muestra los participantes cuyos puntajes promedio son menores al promedio mínimo especificado.

    Args:
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.
        array_nombres (list): Contiene los nombres de los participantes.
        promedio_minimo (float): Promedio mínimo para filtrar participantes.

    Returns:
        bool: Retorna True si se muestran los participantes con promedio menor al especificado, False si no se pudo mostrar.
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
    """Calcula el promedio de puntajes otorgados por cada jurado.
    Esta función toma una matriz de puntajes y calcula el promedio de los puntajes otorgados por cada jurado.
    Itera sobre las columnas de la matriz (cada jurado) y suma los puntajes de cada fila (participante).
    Luego, divide la suma por la cantidad de participantes para obtener el promedio.
    Si la matriz de puntajes es válida y tiene al menos una fila, se calcula el promedio para cada jurado.
    Si la matriz es None o está vacía, la función no realizará ninguna operación y retornará una lista vacía.
    La función retorna una lista con los promedios de puntajes por jurado, redondeados a 2 decimales.
    Muestra el promedio de puntajes otorgados por cada jurado.

    Args:
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        list: Retorna una lista con los promedios de puntajes por jurado, redondeados a 2 decimales.
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
    """Retorna los índices de los jurados con menor promedio (puede haber más de uno).
    Esta función calcula el promedio de puntajes otorgados por cada jurado y determina cuáles tienen el menor promedio.
    Si la matriz de puntajes es válida y tiene al menos una fila, se calcula el promedio para cada jurado.
    Si la matriz es None o está vacía, la función no realizará ninguna operación y retornará una lista vacía.
    La función retorna una lista con los índices de los jurados que tienen el menor promedio.
    Muestra los índices de los jurados con menor promedio de puntajes.

    Args:
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        list: Retorna una lista con los índices de los jurados con menor promedio.
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
    """Retorna los índices de los jurados con mayor promedio (puede haber más de uno).
    Esta función calcula el promedio de puntajes otorgados por cada jurado y determina cuáles tienen el mayor promedio.
    Si la matriz de puntajes es válida y tiene al menos una fila, se calcula el promedio para cada jurado.
    Si la matriz es None o está vacía, la función no realizará ninguna operación y retornará una lista vacía.
    La función retorna una lista con los índices de los jurados que tienen el mayor promedio.
    Muestra los índices de los jurados con mayor promedio de puntajes.

    Args:
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        list: Retorna una lista con los índices de los jurados con mayor promedio.
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
    """Muestra los participantes cuyos puntajes de los tres jurados son iguales.
    Esta función itera sobre los participantes y verifica si los puntajes otorgados por los tres jurados son iguales.
    Si los puntajes de un participante son iguales, se muestra su información utilizando la función mostrar_participante.
    Si la matriz de puntajes y el array de nombres son válidos, y tienen al menos un participante,
    se muestra la información de los participantes que cumplen con la condición.
    Si la matriz de puntajes o el array de nombres son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará False.
    La función retorna True si se muestran los participantes con puntajes iguales, o False si no se pudo mostrar.
    Muestra los participantes cuyos puntajes de los tres jurados son iguales.

    Args:
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.
        array_nombres (list): Contiene los nombres de los participantes.

    Returns:
        bool: Retorna True si se muestran los participantes con puntajes iguales, False si no se pudo mostrar.
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
    """Busca un participante por nombre y muestra sus datos.
    Esta función itera sobre el array de nombres y compara cada nombre con el nombre proporcionado.
    Si encuentra un nombre que coincide, muestra la información del participante utilizando la función mostrar_participante.
    Si el array de nombres y la matriz de puntajes son válidos, y tienen al menos un participante,
    se muestra la información del participante que coincide con el nombre buscado.
    Si el array de nombres o la matriz de puntajes son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará False.
    La función retorna True si se encuentra y muestra el participante, o False si no se pudo encontrar.

    Args:
        array_nombres (list): Contiene los nombres de los participantes.
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.
        nombre (str): Nombre del participante a buscar.

    Returns:
        bool: Retorna True si se encuentra y muestra el participante, False si no se pudo encontrar.
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
    """Muestra los 3 participantes con mayor promedio usando ordenamiento manual.
    Esta función calcula el promedio de puntajes de cada participante y los ordena manualmente para mostrar los 3 con mayor promedio.
    Si la matriz de puntajes y el array de nombres son válidos, y tienen al menos un participante,
    se muestra la información de los 3 participantes con mayor promedio.
    Si la matriz de puntajes o el array de nombres son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará False.
    La función retorna True si se muestran los 3 participantes con mayor promedio, o False si no se pudo mostrar.
    Muestra los 3 participantes con mayor puntaje promedio, ordenados de mayor a menor.
    Esta función utiliza un algoritmo de ordenamiento manual (burbujeo) para ordenar los promedios de los participantes.

    Args:
        array_nombres (list): Contiene los nombres de los participantes.
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        bool: Retorna True si se muestran los 3 participantes con mayor promedio, False si no se pudo mostrar.
    """    
    if (matriz_puntajes != None and array_nombres != None and
        len(matriz_puntajes) > 0 and len(array_nombres) > 0):
        # Crear lista de tuplas (índice, promedio)
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
    """Muestra los participantes ordenados alfabéticamente con sus datos usando ordenamiento manual.
    Esta función ordena los participantes alfabéticamente por su nombre utilizando un algoritmo de ordenamiento manual (burbujeo).
    Si la matriz de puntajes y el array de nombres son válidos, y tienen al menos un participante,
    se muestra la información de todos los participantes ordenados alfabéticamente.
    Si la matriz de puntajes o el array de nombres son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará False.
    La función retorna True si se muestran los participantes ordenados alfabéticamente, o False si no se pudo mostrar.
    Muestra los participantes ordenados alfabéticamente por nombre, junto con sus puntajes y promedios.

    Args:
        array_nombres (list): Contiene los nombres de los participantes.
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        bool: Retorna True si se muestran los participantes ordenados alfabéticamente, False si no se pudo mostrar.
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
    """Muestra el participante ganador (mayor promedio) y retorna lista de tuplas (índice, promedio) de ganadores.
    Esta función calcula el promedio de puntajes de cada participante y determina quién tiene el mayor promedio.
    Si la matriz de puntajes y el array de nombres son válidos, y tienen al menos un participante,
    se muestra la información del participante ganador.
    Si la matriz de puntajes o el array de nombres son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará una lista vacía.
    La función retorna una lista de tuplas (índice, promedio) de los participantes ganadores.
    Muestra el participante ganador (mayor puntaje promedio) y retorna una lista de tuplas con los ganadores.

    Args:
        array_nombres (list): Contiene los nombres de los participantes.
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        list: Retorna una lista de tuplas (índice, promedio) de los participantes ganadores.
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
                ganadores += [(i, max_promedio)]
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
    """Realiza un desempate aleatorio entre participantes con el mayor promedio.
    Esta función calcula el promedio de puntajes de cada participante y determina quiénes tienen el mayor promedio.
    Si hay más de un participante con el mayor promedio, se realiza un desempate aleatorio entre ellos.
    Si la matriz de puntajes y el array de nombres son válidos, y tienen al menos un participante,
    se muestra el ganador del desempate.
    Si la matriz de puntajes o el array de nombres son None, están vacíos o no tienen participantes, la función no realizará ninguna operación y retornará None.
    La función retorna una tupla (índice, promedio) del ganador o None si no hay empate.
    Muestra el ganador del desempate aleatorio entre participantes con el mayor puntaje promedio.

    Args:
        array_nombres (list): Contiene los nombres de los participantes.
        matriz_puntajes (list): Contiene los puntajes otorgados por los jurados a cada participante.

    Returns:
        tuple: Retorna una tupla (índice, promedio) del ganador o None si no hay empate.
    """    
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
                indices_ganadores += [i] # Guardar el índice del ganador
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

