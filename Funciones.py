# =============================================================================
# FUNCIONES.PY
# -----------------------------------------------------------------------------
# Este modulo es el "cerebro" del programa. Aca van TODAS las funciones que
# resuelven la logica de los problemas que pide el parcial: calcular totales,
# promedios, filtrar partidos, buscar el menor, ordenar nombres, etc.
#
# La idea de separarlo asi es: si quiero cambiar como se muestra algo, toco
# Prints.py. Si quiero cambiar como se valida una entrada, toco Inputs.py.
# Si quiero cambiar la LOGICA del problema, toco este archivo.
# =============================================================================

# Importo pedir_entero_positivo desde Inputs.py porque la funcion cargar_votos
# de aca abajo necesita pedirle datos al usuario.
from Inputs import pedir_entero_positivo


def cargar_votos(cantidad_partidos):
    """
    Carga secuencialmente los votos de N partidos politicos (pedidos uno por uno).

    Parametro:
        cantidad_partidos (int): cuantos partidos hay que cargar (por defecto 5).

    Devuelve:
        list: una lista con los votos cargados, en orden.
              Ejemplo: [100, 250, 80, 500, 120]
    """

    # Creo una lista vacia. Aca voy a ir guardando cada voto que ingrese el usuario.
    # Los [] vacios significan "lista sin elementos".
    votos = []

    # Inicializo un contador en 0. Lo voy a usar para saber por que partido voy.
    i = 0

    # Mientras i sea menor a la cantidad de partidos (ej: 5), sigo pidiendo votos.
    # i empieza en 0 y termina en 4 (5 iteraciones: 0,1,2,3,4).
    while i < cantidad_partidos:
        # Le pido los votos al usuario usando la funcion que ya valida que sea
        # un entero positivo. La f delante del string permite meter variables
        # dentro del texto con {}. i+1 porque para el usuario el partido 0 no
        # existe, empezamos a contar desde 1.
        v = pedir_entero_positivo(f"Ingrese los votos del partido {i + 1}: ")

        # append() agrega un elemento al final de la lista. Es uno de los pocos
        # metodos de lista que el profe permite usar segun el PDF.
        votos.append(v)

        # Sumo 1 al contador para que en la proxima vuelta pase al siguiente partido.
        i = i + 1

    # Cuando termino el while, devuelvo la lista llena con los 5 (o N) votos.
    return votos


def calcular_total(votos):
    """
    Suma todos los votos manualmente (no se permite usar sum() segun el PDF).

    Parametro:
        votos (list): lista de votos de los partidos.

    Devuelve:
        int: la suma total de los votos.
    """

    # Empiezo con un acumulador en 0. A esta variable le voy a ir sumando cada voto.
    total = 0
    i = 0

    # len(votos) devuelve la cantidad de elementos de la lista.
    # Recorro la lista de a una posicion por vez.
    while i < len(votos):
        # votos[i] es el elemento que esta en la posicion i de la lista.
        # Si votos = [100, 250, 80] y i = 1, entonces votos[i] = 250.
        total = total + votos[i]
        i = i + 1

    return total


def calcular_porcentaje(cantidad, total):
    """
    Calcula que porcentaje representa "cantidad" sobre el "total".
    Por ejemplo, si cantidad=20 y total=100, devuelve 20.0 (20%).

    Devuelve:
        float: el porcentaje calculado.
    """

    # Proteccion: si el total es 0, no puedo dividir (division por cero rompe el
    # programa). Devuelvo 0 como porcentaje y listo.
    if total == 0:
        return 0

    # Formula clasica de regla de tres simple: (parte * 100) / total
    return (cantidad * 100) / total


def calcular_promedio(votos):
    """
    Calcula el promedio (media aritmetica) de los votos.
    Promedio = suma total / cantidad de elementos.

    Devuelve:
        float: el promedio de los votos.
    """

    # Proteccion contra lista vacia (de nuevo, evito dividir por cero).
    if len(votos) == 0:
        return 0

    # Reutilizo la funcion calcular_total que ya hice. Reusar funciones es
    # importante: no escribo dos veces el mismo codigo.
    return calcular_total(votos) / len(votos)


def buscar_maximo(votos):
    """
    Busca el partido con MAS votos (no se permite max() segun el PDF).

    Devuelve:
        int: el INDICE (posicion) del partido mas votado dentro de la lista.
    """

    # Asumo que el primer partido (posicion 0) es el maximo. Despues voy
    # comparando con los demas y, si encuentro uno mas grande, actualizo.
    indice_max = 0

    # Empiezo desde 1 porque el 0 ya lo asumi como maximo.
    i = 1

    while i < len(votos):
        # Si el partido actual tiene mas votos que el que tengo guardado como max,
        # actualizo el indice del maximo.
        if votos[i] > votos[indice_max]:
            indice_max = i
        i = i + 1

    return indice_max


def buscar_minimo(votos):
    """
    Busca el VALOR del menor voto de la lista (no se permite min() segun el PDF).

    Devuelve:
        int: la cantidad de votos del partido menos votado.
    """

    # Asumo que el primer partido es el minimo y despues comparo.
    minimo = votos[0]
    i = 1

    while i < len(votos):
        # Si el partido actual tiene menos votos que el minimo que llevo guardado,
        # ese pasa a ser el nuevo minimo.
        if votos[i] < minimo:
            minimo = votos[i]
        i = i + 1

    return minimo


def filtrar_menores_a_porcentaje(votos, limite):
    """
    Devuelve la lista de partidos que recibieron MENOS de cierto porcentaje
    del total general de votos. Sirve para los puntos 3, 4 y 5 (10%, 15%, 20%).

    Parametros:
        votos (list): lista con los votos de cada partido.
        limite (int): porcentaje limite (ej: 10 para "menos del 10%").

    Devuelve:
        Tres listas en paralelo (mismas posiciones):
            - indices:     posiciones de los partidos encontrados
            - cantidades:  cantidad de votos de cada uno
            - porcentajes: porcentaje que representa cada uno
    """

    total = calcular_total(votos)

    # Creo tres listas vacias. Las voy a llenar con los datos de los partidos
    # que cumplan la condicion. Las tres listas se "mueven juntas": la posicion 0
    # de cada una se refiere al mismo partido.
    indices = []
    cantidades = []
    porcentajes = []

    i = 0
    while i < len(votos):
        # Calculo el porcentaje del partido actual.
        porc = calcular_porcentaje(votos[i], total)

        # Si el porcentaje es menor al limite (ej: < 10%), guardo los datos.
        if porc < limite:
            indices.append(i)
            cantidades.append(votos[i])
            porcentajes.append(porc)
        i = i + 1

    # Devuelvo las tres listas. En Python se pueden devolver varios valores
    # separados por coma. Despues quien me llama los recibe asi:
    # ind, cant, porc = filtrar_menores_a_porcentaje(...)
    return indices, cantidades, porcentajes


def filtrar_mayores_a_cantidad(votos, limite):
    """
    Devuelve los partidos que recibieron MAS de cierta CANTIDAD de votos
    (no porcentaje, cantidad directa). Sirve para los puntos 6 y 7 (500 y 1000).

    Parametros:
        votos (list): lista con los votos de cada partido.
        limite (int): cantidad de votos limite (ej: 500).
    """

    total = calcular_total(votos)
    indices = []
    cantidades = []
    porcentajes = []

    i = 0
    while i < len(votos):
        # Aca la condicion no es por porcentaje, es directo por cantidad de votos.
        if votos[i] > limite:
            indices.append(i)
            cantidades.append(votos[i])
            # Igual calculo el porcentaje porque el PDF pide mostrarlo en la salida.
            porcentajes.append(calcular_porcentaje(votos[i], total))
        i = i + 1

    return indices, cantidades, porcentajes


def filtrar_arriba_del_promedio(votos):
    """
    Devuelve los partidos que estan POR ENCIMA del promedio general de votos.
    Sirve para el punto 8.

    Devuelve tambien el valor del promedio, porque el PDF pide mostrarlo.
    """

    total = calcular_total(votos)
    promedio = calcular_promedio(votos)

    indices = []
    cantidades = []
    porcentajes = []

    i = 0
    while i < len(votos):
        # Comparo si los votos del partido actual son mayores al promedio.
        if votos[i] > promedio:
            indices.append(i)
            cantidades.append(votos[i])
            porcentajes.append(calcular_porcentaje(votos[i], total))
        i = i + 1

    return indices, cantidades, porcentajes, promedio


def buscar_menos_votado(votos):
    """
    Encuentra el partido (o partidos, si hay empate) con MENOS votos.
    Esto es para el punto 9 y el punto extra del parcial: contemplar empates.

    Devuelve:
        - indices (list): TODAS las posiciones de partidos con el minimo.
                          Si hay empate, la lista tiene mas de un elemento.
        - minimo (int):   la cantidad de votos del menor.
    """

    # Primero encuentro CUAL es el valor minimo.
    minimo = buscar_minimo(votos)

    # Despues recorro toda la lista buscando TODOS los partidos que tengan
    # ese valor minimo (puede haber mas de uno empatados).
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] == minimo:
            indices.append(i)
        i = i + 1

    return indices, minimo


def verificar_segunda_vuelta(votos):
    """
    Verifica si hace falta una segunda vuelta electoral.
    Segun el PDF:
      - Si ningun partido supera el 50% -> hay segunda vuelta.
      - Si justo el ganador tiene 50% exacto -> tambien hay segunda vuelta.
      - Si tiene mas del 50% -> NO hay segunda vuelta y gana.

    Devuelve:
        - hay_segunda (bool): True si hay segunda vuelta, False si no.
        - indice_max (int):   posicion del partido con mas votos.
        - votos_max (int):    cantidad de votos del ganador potencial.
        - porc_max (float):   porcentaje que saco el ganador potencial.
    """

    total = calcular_total(votos)

    # Reutilizo buscar_maximo para no repetir codigo.
    indice_max = buscar_maximo(votos)

    porc_max = calcular_porcentaje(votos[indice_max], total)

    # Si el ganador tiene 50% o menos, hay segunda vuelta.
    if porc_max <= 50:
        hay_segunda = True
    else:
        hay_segunda = False

    return hay_segunda, indice_max, votos[indice_max], porc_max


def hardcodear_votos():
    """
    Devuelve un vector de votos HARDCODEADO (escrito a mano) con 10 partidos,
    tal cual lo pide el punto 11 del PDF. Esto reemplaza a los votos cargados
    previamente por el usuario.
    """

    # Devuelvo la lista TAL CUAL la pide el enunciado, sin modificar valores.
    return [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]


# =============================================================================
# SECCION DE ORDENAMIENTO (PUNTO 12)
# -----------------------------------------------------------------------------
# Aca esta toda la logica para ordenar los nombres de los partidos
# alfabeticamente (A-Z). Como el PDF prohibe los metodos de string, tengo que
# comparar las palabras letra por letra usando el codigo ASCII.
# =============================================================================


def comparar_strings(s1, s2):
    """
    Compara dos strings (textos) letra por letra usando codigo ASCII.

    Devuelve:
        -1 si s1 es "menor" alfabeticamente que s2 (ej: "Alianza" < "Frente")
         0 si son iguales
         1 si s1 es "mayor" alfabeticamente que s2

    ¿Como funciona el codigo ASCII? Cada caracter tiene un numero asociado:
        'A' = 65, 'B' = 66, 'C' = 67 ... 'Z' = 90
        'a' = 97, 'b' = 98 ... 'z' = 122
    La funcion ord('A') devuelve 65. Comparando esos numeros puedo saber
    cual letra va antes alfabeticamente.
    """

    largo1 = len(s1)
    largo2 = len(s2)

    # Voy a comparar hasta donde alcance el string mas corto. Si los primeros
    # caracteres son todos iguales, despues comparo cual es mas largo.
    if largo1 < largo2:
        minimo = largo1
    else:
        minimo = largo2

    i = 0
    while i < minimo:
        # ord() devuelve el codigo ASCII del caracter en la posicion i.
        # s1[i] accede al caracter i del string (igual que con una lista).
        c1 = ord(s1[i])
        c2 = ord(s2[i])

        # Si la letra esta en MAYUSCULA (codigo entre 65 y 90 = 'A' a 'Z'),
        # le sumo 32 para convertirla a minuscula (asi "frente" y "Frente"
        # se comparan igual). Esto es lo que se llama "comparacion case-insensitive".
        # Ejemplo: ord('A')=65, le sumo 32 y queda 97 que es ord('a').
        if c1 >= 65 and c1 <= 90:
            c1 = c1 + 32
        if c2 >= 65 and c2 <= 90:
            c2 = c2 + 32

        # Comparo los codigos ASCII letra por letra.
        if c1 < c2:
            return -1
        if c1 > c2:
            return 1

        # Si son iguales, paso a la siguiente letra (no retorno todavia).
        i = i + 1

    # Si llegue hasta aca es porque todas las letras comparadas eran iguales.
    # En ese caso, decide el largo: el mas corto va primero.
    # Ejemplo: "Frente" vs "Frente de Java" -> "Frente" es menor (mas corto).
    if largo1 < largo2:
        return -1
    if largo1 > largo2:
        return 1

    # Si los largos son iguales tambien -> son strings identicos.
    return 0


def ordenar_nombres(lista):
    """
    Ordena una lista de nombres alfabeticamente (A-Z) usando BUBBLE SORT.

    ¿Que es Bubble Sort?
    Es el algoritmo de ordenamiento mas basico que se ensena en clase.
    Funciona asi: recorre la lista comparando elementos contiguos (de a pares)
    y si estan en el orden incorrecto, los intercambia (swap). Repite el proceso
    hasta que no haga falta hacer mas intercambios. Se llama "burbuja" porque
    los elementos mas grandes "burbujean" (suben) hacia el final.

    Devuelve:
        list: una NUEVA lista ordenada (la original no se modifica).
    """

    # copy() crea una copia de la lista para no modificar la original.
    # copy() esta en la lista de metodos permitidos del PDF.
    nombres = lista.copy()

    largo = len(nombres)

    # El i representa "cuantas vueltas completas ya hice". Cada vuelta deja
    # al ultimo elemento (el mas grande) en su posicion final, asi que la
    # siguiente vuelta puede ser mas corta.
    i = 0
    while i < largo - 1:
        # En esta vuelta interna comparo cada par de elementos contiguos.
        # Le resto i porque los ultimos i elementos ya estan ordenados.
        j = 0
        while j < largo - 1 - i:
            # Comparo el elemento j con el j+1 (el de al lado).
            # Si comparar_strings devuelve > 0 significa que estan en orden
            # incorrecto (el de la izquierda es "mayor" que el de la derecha).
            if comparar_strings(nombres[j], nombres[j + 1]) > 0:
                # SWAP (intercambio): para intercambiar dos variables necesito
                # una auxiliar, sino pierdo el valor. Es como tener dos vasos
                # con agua y querer cambiarlos: necesitas un tercer vaso temporal.
                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux
            j = j + 1
        i = i + 1

    return nombres
