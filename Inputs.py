def validar_nombre() -> str:
    while True:
        nombre = input("Ingrese el nombre del participante: ")
        inicio = 0
        fin = len(nombre) - 1
        while inicio <= fin and nombre[inicio] == ' ':
            inicio += 1
        while fin >= inicio and nombre[fin] == ' ':
            fin -= 1
        nombre_limpio = nombre[inicio:fin + 1]

        if len(nombre_limpio) >= 3:
            solo_letras_espacio = True
            for caracteres in nombre_limpio:
                es_letra = ('a' <= caracteres <= 'z') or ('A' <= caracteres <= 'Z')
                es_espacio = caracteres == " "
                if not (es_letra or es_espacio):
                    solo_letras_espacio = False
                    break
            if solo_letras_espacio:
                return nombre_limpio
        print("El nombre debe tener al menos 3 caracteres y solo contener letras y espacios.")

def validar_puntaje() -> int:
    while True:
        try:
            puntaje = int(input("Ingrese el puntaje entre (1-10): "))
            if 1 <= puntaje <= 10:
                return puntaje
            else:
                print("El puntaje debe estar entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero entre 1 y 10.")

def validar_opcion_menu(max_opcion: int) -> int:
    while True:
        try:
            opcion = int(input(f"Ingrese una opción (1-{max_opcion}): "))
            if 1 <= opcion <= max_opcion:
                return opcion
            else:
                print(f"Por favor, ingrese un número entre 1 y {max_opcion}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")