from Inputs import pedir_entero_positivo


def cargar_votos(cantidad_partidos):
    """Pide los votos de cada partido y los devuelve en una lista."""
    votos = []
    i = 0
    while i < cantidad_partidos:
        v = pedir_entero_positivo(f"Ingrese los votos del partido {i + 1}: ")
        votos.append(v)
        i = i + 1
    return votos


def calcular_total(votos):
    """Devuelve la suma de todos los votos."""
    total = 0
    i = 0
    while i < len(votos):
        total = total + votos[i]
        i = i + 1
    return total


def calcular_porcentaje(cantidad, total):
    """Devuelve el porcentaje que representa cantidad sobre total."""
    if total == 0:
        return 0
    return (cantidad * 100) / total


def calcular_promedio(votos):
    """Devuelve el promedio de los votos."""
    if len(votos) == 0:
        return 0
    return calcular_total(votos) / len(votos)


def buscar_indice_maximo(votos):
    """Devuelve el indice del partido con mas votos."""
    indice = 0
    i = 1
    while i < len(votos):
        if votos[i] > votos[indice]:
            indice = i
        i = i + 1
    return indice


def buscar_indice_minimo(votos):
    """Devuelve el indice del partido con menos votos."""
    indice = 0
    i = 1
    while i < len(votos):
        if votos[i] < votos[indice]:
            indice = i
        i = i + 1
    return indice


def buscar_menos_votados(votos):
    """Devuelve los indices de todos los partidos con la menor cantidad de votos."""
    indice_min = buscar_indice_minimo(votos)
    minimo = votos[indice_min]
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] == minimo:
            indices.append(i)
        i = i + 1
    return indices


def filtrar_menores_a_porcentaje(votos, limite):
    """Devuelve los indices de los partidos con menos del 'limite'% del total."""
    total = calcular_total(votos)
    indices = []
    i = 0
    while i < len(votos):
        porc = calcular_porcentaje(votos[i], total)
        if porc < limite:
            indices.append(i)
        i = i + 1
    return indices


def filtrar_mayores_a_cantidad(votos, limite):
    """Devuelve los indices de los partidos con mas de 'limite' votos."""
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] > limite:
            indices.append(i)
        i = i + 1
    return indices


def filtrar_arriba_del_promedio(votos):
    """Devuelve los indices de los partidos por encima del promedio."""
    promedio = calcular_promedio(votos)
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] > promedio:
            indices.append(i)
        i = i + 1
    return indices


def hay_segunda_vuelta(votos):
    """Devuelve True si ningun partido supera el 50% (o lo iguala)."""
    total = calcular_total(votos)
    indice_ganador = buscar_indice_maximo(votos)
    porcentaje = calcular_porcentaje(votos[indice_ganador], total)
    return porcentaje <= 50


def hardcodear_votos():
    """Devuelve el vector hardcodeado del punto 11."""
    return [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]


def ordenar_nombres(lista):
    """Ordena alfabeticamente una lista de nombres con Bubble Sort."""
    nombres = lista.copy()
    n = len(nombres)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if nombres[j] > nombres[j + 1]:
                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux
            j = j + 1
        i = i + 1
    return nombres
