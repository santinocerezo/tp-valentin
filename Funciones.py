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
    """Devuelve la suma de todos los votos de la lista."""
    total = 0
    i = 0
    while i < len(votos):
        total = total + votos[i]
        i = i + 1
    return total


def calcular_porcentaje(cantidad, total):
    """Devuelve el porcentaje que representa 'cantidad' sobre el total."""
    if total == 0:
        return 0
    return (cantidad * 100) / total


def calcular_promedio(votos):
    """Devuelve el promedio de los votos de la lista."""
    if len(votos) == 0:
        return 0
    return calcular_total(votos) / len(votos)


def buscar_maximo(votos):
    """Devuelve el indice del partido con mayor cantidad de votos."""
    indice_max = 0
    i = 1
    while i < len(votos):
        if votos[i] > votos[indice_max]:
            indice_max = i
        i = i + 1
    return indice_max


def buscar_minimo(votos):
    """Devuelve el valor del voto mas bajo de la lista."""
    minimo = votos[0]
    i = 1
    while i < len(votos):
        if votos[i] < minimo:
            minimo = votos[i]
        i = i + 1
    return minimo


def filtrar_menores_a_porcentaje(votos, limite):
    """Devuelve indices, cantidades y porcentajes de los partidos con menos del 'limite'%."""
    total = calcular_total(votos)
    indices = []
    cantidades = []
    porcentajes = []
    i = 0
    while i < len(votos):
        porc = calcular_porcentaje(votos[i], total)
        if porc < limite:
            indices.append(i)
            cantidades.append(votos[i])
            porcentajes.append(porc)
        i = i + 1
    return indices, cantidades, porcentajes


def filtrar_mayores_a_cantidad(votos, limite):
    """Devuelve indices, cantidades y porcentajes de los partidos con mas de 'limite' votos."""
    total = calcular_total(votos)
    indices = []
    cantidades = []
    porcentajes = []
    i = 0
    while i < len(votos):
        if votos[i] > limite:
            indices.append(i)
            cantidades.append(votos[i])
            porcentajes.append(calcular_porcentaje(votos[i], total))
        i = i + 1
    return indices, cantidades, porcentajes


def filtrar_arriba_del_promedio(votos):
    """Devuelve los partidos que superan el promedio general, junto con el promedio."""
    total = calcular_total(votos)
    promedio = calcular_promedio(votos)
    indices = []
    cantidades = []
    porcentajes = []
    i = 0
    while i < len(votos):
        if votos[i] > promedio:
            indices.append(i)
            cantidades.append(votos[i])
            porcentajes.append(calcular_porcentaje(votos[i], total))
        i = i + 1
    return indices, cantidades, porcentajes, promedio


def buscar_menos_votado(votos):
    """Devuelve los indices del o los partidos menos votados (contempla empates)."""
    minimo = buscar_minimo(votos)
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] == minimo:
            indices.append(i)
        i = i + 1
    return indices, minimo


def verificar_segunda_vuelta(votos):
    """Verifica si hace falta segunda vuelta segun el 50% del ganador."""
    total = calcular_total(votos)
    indice_max = buscar_maximo(votos)
    porc_max = calcular_porcentaje(votos[indice_max], total)
    if porc_max <= 50:
        hay_segunda = True
    else:
        hay_segunda = False
    return hay_segunda, indice_max, votos[indice_max], porc_max


def hardcodear_votos():
    """Devuelve el vector hardcodeado de 10 partidos del punto 11."""
    return [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]


def comparar_strings(s1, s2):
    """Compara dos strings por codigo ASCII. Devuelve -1, 0 o 1."""
    largo1 = len(s1)
    largo2 = len(s2)
    if largo1 < largo2:
        minimo = largo1
    else:
        minimo = largo2
    i = 0
    while i < minimo:
        c1 = ord(s1[i])
        c2 = ord(s2[i])
        if c1 >= 65 and c1 <= 90:
            c1 = c1 + 32
        if c2 >= 65 and c2 <= 90:
            c2 = c2 + 32
        if c1 < c2:
            return -1
        if c1 > c2:
            return 1
        i = i + 1
    if largo1 < largo2:
        return -1
    if largo1 > largo2:
        return 1
    return 0


def ordenar_nombres(lista):
    """Ordena alfabeticamente una lista de nombres usando Bubble Sort."""
    nombres = lista.copy()
    largo = len(nombres)
    i = 0
    while i < largo - 1:
        j = 0
        while j < largo - 1 - i:
            if comparar_strings(nombres[j], nombres[j + 1]) > 0:
                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux
            j = j + 1
        i = i + 1
    return nombres
