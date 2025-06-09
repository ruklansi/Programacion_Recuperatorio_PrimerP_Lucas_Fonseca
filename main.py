import os
from Funciones import *
from Inputs import *

array_nombres = crear_array(5, "")
matriz_puntajes = crear_matriz(5, 3, 0)
bandera_carga_nombres = False
bandera_carga_puntajes = False

while True:
    print("\n=== Menu de Opciones ===")
    print("1. Cargar Participantes")
    print("2. Cargar Puntuaciones")
    print("3. Mostrar Puntuaciones")
    print("4. Mostrar Participantes con promedio menor a 4")
    print("5. Mostrar Participantes con promedio mayor a 8")
    print("6. Mostrar Promedio de cada Jurado")
    print("7. Mostrar Jurado más estricto")
    print("8. Mostrar Jurado más generoso")
    print("9. Mostrar Participantes con puntaje iguales")
    print("10. Buscar Participantes por nombre")
    print("11. Top 3 Participantes")
    print("12. Participantes ordenados alfabéticamente")
    print("13. Mostar Ganador")
    print("14. Desempatar Ganador")
    print("15. Salir")
    print("=========================")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 15:
            print("Error: Opción invalida.")
            input("Presione cualquier tecla para continuar...")
            os.system("clear")
            continue
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        input("Presione cualquier tecla para continuar...")
        os.system("clear")
        continue

    if opcion == 1:
        if cargar_nombres_participantes(array_nombres):
            print("Nombres cargados correctamente...")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error al realizar la carga")
    
    elif opcion == 2:
        if cargar_puntajes(matriz_puntajes):
            print("Carga exitosa de puntajes!")
            mostrar_matriz(matriz_puntajes)
            bandera_carga_puntajes = True
        else:
            print("Error al realizar la carga")
    
    elif opcion == 3 and bandera_carga_nombres and bandera_carga_puntajes:
        if not mostrar_puntajes(array_nombres, matriz_puntajes):
            print("Error al mostrar las puntuaciones")
    
    elif opcion == 4 and bandera_carga_nombres and bandera_carga_puntajes:
        if not mostrar_participantes_menor_promedio(matriz_puntajes, array_nombres, 4):
            print("No hay participantes con promedio menor a 4")
    
    elif opcion == 5 and bandera_carga_nombres and bandera_carga_puntajes:
        if not mostrar_participantes_menor_promedio(matriz_puntajes, array_nombres, 8):
            print("No hay participantes con promedio menor a 8")

    elif opcion == 6 and bandera_carga_nombres and bandera_carga_puntajes:
        promedios = promedio_por_jurado(matriz_puntajes)
        if promedios:
            for i in range(len(promedios)):
                prom = promedios[i]
                print(f"Jurado {i+1}: Promedio = {prom}")

    elif opcion == 7 and bandera_carga_nombres and bandera_carga_puntajes:
        promedios = promedio_por_jurado(matriz_puntajes)
        if promedios:
            min_prom = min(promedios)
            print("Jurado(s) más estricto(s):")
            for i in range(len(promedios)):
                if promedios[i] == min_prom:
                    print(f"Jurado {i+1} con promedio {min_prom:.2f}")
        else:
            print("No se pudieron calcular los promedios.")

    elif opcion == 8 and bandera_carga_nombres and bandera_carga_puntajes:
        promedios = promedio_por_jurado(matriz_puntajes)
        if promedios:
            max_prom = max(promedios)
            print("Jurado(s) más generoso(s):")
            for i in range(len(promedios)):
                if promedios[i] == max_prom:
                    print(f"Jurado {i+1} con promedio {max_prom:.2f}")
        else:
            print("No se pudieron calcular los promedios.")

    elif opcion == 9 and bandera_carga_nombres and bandera_carga_puntajes:
        if not participantes_puntajes_iguales(matriz_puntajes, array_nombres):
            print("No hay participantes con puntajes iguales")

    elif opcion == 10 and bandera_carga_nombres and bandera_carga_puntajes:
        nombre = validar_nombre()
        if not buscar_participante_por_nombre(array_nombres, matriz_puntajes, nombre):
            print(f"No se encontró el participante con nombre: {nombre}")

    elif opcion == 11 and bandera_carga_nombres and bandera_carga_puntajes:
        if not top_3_participantes(array_nombres, matriz_puntajes):
            print("Error al mostrar el top 3")

    elif opcion == 12 and bandera_carga_nombres and bandera_carga_puntajes:
        if not participantes_ordenados_alfabeticamente(array_nombres, matriz_puntajes):
            print("Error al mostrar los participantes ordenados")

    elif opcion == 13 and bandera_carga_nombres and bandera_carga_puntajes:
        ganadores = mostrar_ganador(array_nombres, matriz_puntajes)  # Ahora devuelve lista de (índice, promedio)
        if ganadores:
            if len(ganadores) == 1:
                print(f"El ganador es: {array_nombres[ganadores[0][0]]} con un puntaje de {ganadores[0][1]:.2f}")
            else:
                print("Hay más de un participante con el puntaje más alto. Debe realizar un desempate primero.")
        else:
            print("No se pudo determinar el ganador.")
        
    elif opcion == 14 and bandera_carga_nombres and bandera_carga_puntajes:
        ganador = desempatar(array_nombres, matriz_puntajes)
        if ganador:
            print(f"El ganador desempate es: {array_nombres[ganador[0]]} con un puntaje de {ganador[1]:.2f}")
        else:
            print("No se pudo realizar el desempate.")

    elif opcion == 15:
        print("Saliendo del programa...")
        break
    else:
        print("Error: Debe cargar los participantes y puntajes antes de realizar esta acción.")
    input("Presione cualquier tecla para continuar...")
    os.system("clear")