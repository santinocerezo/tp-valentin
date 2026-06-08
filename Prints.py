from Funciones import (
    calcular_total,
    calcular_porcentaje,
    calcular_promedio,
    calcular_suma_indices,
    calcular_promedio_indices,
    calcular_porcentaje_acumulado,
    buscar_indice_maximo,
    buscar_menos_votados,
    filtrar_menores_a_porcentaje,
    filtrar_mayores_a_cantidad,
    filtrar_arriba_del_promedio,
    verificar_segunda_vuelta,
)


def mostrar_menu() -> None:
    """Imprime el menu de opciones del programa."""
    print("")
    print("===== SISTEMA DE ELECCIONES - CENTRO DE ESTUDIANTES UTN FRA =====")
    print("1.  Cargar votos")
    print("2.  Mostrar votos")
    print("3.  Partidos con menos del 10% de votos")
    print("4.  Partidos con menos del 15% de votos")
    print("5.  Partidos con menos del 20% de votos")
    print("6.  Partidos con mas de 500 votos")
    print("7.  Partidos con mas de 1000 votos")
    print("8.  Partidos por encima del promedio")
    print("9.  Partido menos votado")
    print("10. Verificar segunda vuelta")
    print("11. Hardcodear vector de votos")
    print("12. Ordenar partidos por nombre")
    print("0.  Salir")
    print("=================================================================")


def mostrar_mensaje(msg: str) -> None:
    """Imprime un mensaje generico con un salto de linea antes."""
    print("")
    print(msg)


def mostrar_datos_partido(numero: int, votos: int, porcentaje: float) -> None:
    """Muestra la cantidad de votos y el porcentaje de un unico partido.

    Funcion reutilizada por todas las opciones que necesitan listar partidos,
    para no repetir el mismo print en distintos lugares.
    """
    print(f"Partido {numero}: {votos} votos ({porcentaje:.2f}%)")


def mostrar_listado(votos: list[int]) -> None:
    """Muestra todos los partidos con sus votos, porcentajes y totales."""
    total = calcular_total(votos)
    print("")
    print("----- LISTADO DE PARTIDOS -----")
    print(f"Cantidad de partidos postulados: {len(votos)}")
    print(f"Cantidad total de votos: {total}")
    print("")
    i = 0
    while i < len(votos):
        porc = calcular_porcentaje(votos[i], total)
        mostrar_datos_partido(i + 1, votos[i], porc)
        i = i + 1


def mostrar_filtrados_menos(votos: list[int], limite: float) -> None:
    """Muestra los partidos con menos del 'limite'% del total y el acumulado."""
    total = calcular_total(votos)
    indices = filtrar_menores_a_porcentaje(votos, limite)
    print("")
    print(f"----- PARTIDOS CON MENOS DEL {limite}% DE VOTOS -----")
    if len(indices) == 0:
        print("No hay partidos que cumplan esta condicion")
        return
    i = 0
    while i < len(indices):
        idx = indices[i]
        porc = calcular_porcentaje(votos[idx], total)
        mostrar_datos_partido(idx + 1, votos[idx], porc)
        i = i + 1
    acumulado = calcular_porcentaje_acumulado(votos, indices)
    print(f"Porcentaje acumulado de la busqueda: {acumulado:.2f}%")


def mostrar_filtrados_mas(votos: list[int], limite: int) -> None:
    """Muestra los partidos con mas de 'limite' votos, mas suma, cantidad y promedio."""
    total = calcular_total(votos)
    indices = filtrar_mayores_a_cantidad(votos, limite)
    print("")
    print(f"----- PARTIDOS CON MAS DE {limite} VOTOS -----")
    if len(indices) == 0:
        print("No hay partidos que cumplan esta condicion")
        return
    i = 0
    while i < len(indices):
        idx = indices[i]
        porc = calcular_porcentaje(votos[idx], total)
        mostrar_datos_partido(idx + 1, votos[idx], porc)
        i = i + 1
    suma = calcular_suma_indices(votos, indices)
    promedio_busqueda = calcular_promedio_indices(votos, indices)
    print(f"Suma de votos: {suma}")
    print(f"Cantidad de partidos encontrados: {len(indices)}")
    print(f"Promedio de votos: {promedio_busqueda:.2f}")


def mostrar_arriba_promedio(votos: list[int]) -> None:
    """Muestra los partidos por encima del promedio y el porcentaje acumulado."""
    total = calcular_total(votos)
    promedio = calcular_promedio(votos)
    indices = filtrar_arriba_del_promedio(votos)
    print("")
    print("----- PARTIDOS POR ENCIMA DEL PROMEDIO -----")
    print(f"Promedio general de votos: {promedio:.2f}")
    if len(indices) == 0:
        print("No hay partidos por encima del promedio")
        return
    i = 0
    while i < len(indices):
        idx = indices[i]
        porc = calcular_porcentaje(votos[idx], total)
        mostrar_datos_partido(idx + 1, votos[idx], porc)
        i = i + 1
    acumulado = calcular_porcentaje_acumulado(votos, indices)
    print(f"Porcentaje acumulado de la busqueda: {acumulado:.2f}%")


def mostrar_menos_votado(votos: list[int]) -> None:
    """Muestra el o los partidos menos votados con su cantidad de votos y porcentaje (contempla empates)."""
    total = calcular_total(votos)
    indices = buscar_menos_votados(votos)
    minimo = votos[indices[0]]
    porc = calcular_porcentaje(minimo, total)
    print("")
    print("----- PARTIDO MENOS VOTADO -----")
    if len(indices) == 1:
        mostrar_datos_partido(indices[0] + 1, minimo, porc)
    else:
        print("Hay un empate entre los siguientes partidos:")
        i = 0
        while i < len(indices):
            mostrar_datos_partido(indices[i] + 1, minimo, porc)
            i = i + 1


def mostrar_segunda_vuelta(votos: list[int]) -> None:
    """Muestra si hay segunda vuelta y, si no, los datos del ganador."""
    total = calcular_total(votos)
    print("")
    print("----- VERIFICACION DE SEGUNDA VUELTA -----")
    if verificar_segunda_vuelta(votos):
        print("Debe realizarse una segunda vuelta electoral")
    else:
        indice = buscar_indice_maximo(votos)
        porc = calcular_porcentaje(votos[indice], total)
        print("No debe realizarse una segunda vuelta electoral")
        print("Partido ganador:")
        mostrar_datos_partido(indice + 1, votos[indice], porc)


def mostrar_nombres_ordenados(nombres: list[str]) -> None:
    """Imprime la lista de nombres ya ordenada alfabeticamente."""
    print("")
    print("----- PARTIDOS ORDENADOS ALFABETICAMENTE (A-Z) -----")
    i = 0
    while i < len(nombres):
        print(f"{i + 1}. {nombres[i]}")
        i = i + 1
