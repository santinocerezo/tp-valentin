from Inputs import pedir_entero_positivo


def cargar_votos(cantidad_partidos: int) -> list[int]:
    """Pide los votos de cada partido y los devuelve en una lista."""
    votos = []
    i = 0
    while i < cantidad_partidos:
        v = pedir_entero_positivo(f"Ingrese los votos del partido {i + 1}: ")
        votos.append(v)
        i = i + 1
    return votos


def calcular_total(votos: list[int]) -> int:
    """Devuelve la suma de todos los votos."""
    total = 0
    i = 0
    while i < len(votos):
        total = total + votos[i]
        i = i + 1
    return total


def calcular_porcentaje(cantidad: int, total: int) -> float:
    """Devuelve el porcentaje que representa cantidad sobre total."""
    if total == 0:
        return 0
    return (cantidad * 100) / total


def calcular_promedio(votos: list[int]) -> float:
    """Devuelve el promedio de los votos."""
    if len(votos) == 0:
        return 0
    return calcular_total(votos) / len(votos)


def calcular_suma_indices(votos: list[int], indices: list[int]) -> int:
    """Devuelve la suma de los votos de los partidos indicados por 'indices'."""
    suma = 0
    i = 0
    while i < len(indices):
        suma = suma + votos[indices[i]]
        i = i + 1
    return suma


def calcular_promedio_indices(votos: list[int], indices: list[int]) -> float:
    """Devuelve el promedio de votos de los partidos indicados por 'indices'."""
    if len(indices) == 0:
        return 0
    return calcular_suma_indices(votos, indices) / len(indices)


def calcular_porcentaje_acumulado(votos: list[int], indices: list[int]) -> float:
    """Devuelve la suma de los porcentajes (sobre el total general) de los partidos indicados."""
    total = calcular_total(votos)
    acumulado = 0
    i = 0
    while i < len(indices):
        acumulado = acumulado + calcular_porcentaje(votos[indices[i]], total)
        i = i + 1
    return acumulado


def buscar_indice_maximo(votos: list[int]) -> int:
    """Devuelve el indice del partido con mas votos."""
    indice = 0
    i = 1
    while i < len(votos):
        if votos[i] > votos[indice]:
            indice = i
        i = i + 1
    return indice


def buscar_indice_minimo(votos: list[int]) -> int:
    """Devuelve el indice del partido con menos votos."""
    indice = 0
    i = 1
    while i < len(votos):
        if votos[i] < votos[indice]:
            indice = i
        i = i + 1
    return indice


def buscar_menos_votados(votos: list[int]) -> list[int]:
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


def filtrar_menores_a_porcentaje(votos: list[int], limite: float) -> list[int]:
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


def filtrar_mayores_a_cantidad(votos: list[int], limite: int) -> list[int]:
    """Devuelve los indices de los partidos con mas de 'limite' votos."""
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] > limite:
            indices.append(i)
        i = i + 1
    return indices


def filtrar_arriba_del_promedio(votos: list[int]) -> list[int]:
    """Devuelve los indices de los partidos por encima del promedio."""
    promedio = calcular_promedio(votos)
    indices = []
    i = 0
    while i < len(votos):
        if votos[i] > promedio:
            indices.append(i)
        i = i + 1
    return indices


def verificar_segunda_vuelta(votos: list[int]) -> bool:
    """Devuelve True si ningun partido supera el 50% (o lo iguala) y debe haber segunda vuelta."""
    total = calcular_total(votos)
    indice_ganador = buscar_indice_maximo(votos)
    porcentaje = calcular_porcentaje(votos[indice_ganador], total)
    return porcentaje <= 50


def hardcodear_votos() -> list[int]:
    """Devuelve el vector hardcodeado del punto 11."""
    return [888, 555, 333, 1850, 999, 777, 1400, 180, 2500, 60]


def ordenar_nombres(lista: list[str]) -> list[str]:
    """Ordena alfabeticamente (A-Z) una lista de nombres usando el algoritmo Bubble Sort.

    Bubble Sort ("ordenamiento burbuja") recorre la lista varias veces comparando
    elementos adyacentes de a pares. En cada pasada:
      - Compara el elemento en la posicion j con el de la posicion j + 1.
      - Si estan en el orden incorrecto (el de la izquierda es "mayor" que el de la
        derecha), los intercambia (swap) usando una variable auxiliar.
    De esta forma, en cada pasada el elemento mas grande "burbujea" hacia el final de
    la lista, por eso el bucle interno se acorta (n - 1 - i): las ultimas posiciones ya
    quedaron ordenadas y no hace falta volver a compararlas.

    Como los elementos son cadenas (strings), el operador '>' los compara segun el
    codigo ASCII de cada caracter, letra por letra (igual que en un diccionario). Por
    eso el resultado queda en orden alfabetico de la A a la Z. Si quisieramos ordenar
    al reves (Z-A) bastaria con invertir la comparacion usando '<' en lugar de '>'.

    Se trabaja sobre una copia (copy) para no modificar la lista original recibida.
    """
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
