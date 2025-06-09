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
        entrada = input("Ingrese el puntaje (1-10): ")
        es_entero = True
        if len(entrada) == 0:
            es_entero = False
        else:
            for c in entrada:
                if not ('0' <= c <= '9'):
                    es_entero = False
                    break
        if es_entero:
            puntaje = 0
            for c in entrada:
                puntaje = puntaje * 10 + (ord(c) - ord('0'))
            if 1 <= puntaje <= 10:
                return puntaje
            else:
                print("Error: El puntaje debe estar entre 1 y 10.")
        else:
            print("Error: Ingrese un número entero.")