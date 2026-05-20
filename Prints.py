from Funciones import (
    calcular_total,
    calcular_porcentaje,
    filtrar_menores_a_porcentaje,
    filtrar_mayores_a_cantidad,
    filtrar_arriba_del_promedio,
    buscar_menos_votado,
    verificar_segunda_vuelta,
)


def mostrar_menu():
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


def mostrar_mensaje(msg):
    """Imprime un mensaje generico con un salto de linea antes."""
    print("")
    print(msg)


def mostrar_listado(votos):
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
        print(f"Partido {i + 1}: {votos[i]} votos ({porc:.2f}%)")
        i = i + 1


def mostrar_filtrados_menos(votos, limite):
    """Muestra los partidos con menos del 'limite'% del total y el acumulado."""
    indices, cantidades, porcentajes = filtrar_menores_a_porcentaje(votos, limite)
    print("")
    print(f"----- PARTIDOS CON MENOS DEL {limite}% DE VOTOS -----")
    if len(indices) == 0:
        print("No hay partidos que cumplan esta condicion")
        return
    acumulado = 0
    i = 0
    while i < len(indices):
        print(f"Partido {indices[i] + 1}: {cantidades[i]} votos ({porcentajes[i]:.2f}%)")
        acumulado = acumulado + porcentajes[i]
        i = i + 1
    print(f"Porcentaje acumulado de la busqueda: {acumulado:.2f}%")


def mostrar_filtrados_mas(votos, limite):
    """Muestra los partidos con mas de 'limite' votos, mas suma, cantidad y promedio."""
    indices, cantidades, porcentajes = filtrar_mayores_a_cantidad(votos, limite)
    print("")
    print(f"----- PARTIDOS CON MAS DE {limite} VOTOS -----")
    if len(indices) == 0:
        print("No hay partidos que cumplan esta condicion")
        return
    suma = 0
    i = 0
    while i < len(indices):
        print(f"Partido {indices[i] + 1}: {cantidades[i]} votos ({porcentajes[i]:.2f}%)")
        suma = suma + cantidades[i]
        i = i + 1
    promedio_busqueda = suma / len(indices)
    print(f"Suma de votos: {suma}")
    print(f"Cantidad de partidos encontrados: {len(indices)}")
    print(f"Promedio de votos: {promedio_busqueda:.2f}")


def mostrar_arriba_promedio(votos):
    """Muestra los partidos por encima del promedio y el porcentaje acumulado."""
    indices, cantidades, porcentajes, promedio = filtrar_arriba_del_promedio(votos)
    print("")
    print("----- PARTIDOS POR ENCIMA DEL PROMEDIO -----")
    print(f"Promedio general de votos: {promedio:.2f}")
    if len(indices) == 0:
        print("No hay partidos por encima del promedio")
        return
    acumulado = 0
    i = 0
    while i < len(indices):
        print(f"Partido {indices[i] + 1}: {cantidades[i]} votos ({porcentajes[i]:.2f}%)")
        acumulado = acumulado + porcentajes[i]
        i = i + 1
    print(f"Porcentaje acumulado de la busqueda: {acumulado:.2f}%")


def mostrar_menos_votado(votos):
    """Muestra el o los partidos menos votados (contempla empates)."""
    indices, minimo = buscar_menos_votado(votos)
    total = calcular_total(votos)
    porc = calcular_porcentaje(minimo, total)
    print("")
    print("----- PARTIDO MENOS VOTADO -----")
    if len(indices) == 1:
        print(f"Partido {indices[0] + 1}: {minimo} votos ({porc:.2f}%)")
    else:
        print("Hay un empate entre los siguientes partidos:")
        i = 0
        while i < len(indices):
            print(f"Partido {indices[i] + 1}: {minimo} votos ({porc:.2f}%)")
            i = i + 1


def mostrar_segunda_vuelta(votos):
    """Muestra si hay segunda vuelta y, si no, los datos del ganador."""
    hay_segunda, indice, cantidad, porc = verificar_segunda_vuelta(votos)
    print("")
    print("----- VERIFICACION DE SEGUNDA VUELTA -----")
    if hay_segunda:
        print("Debe realizarse una segunda vuelta electoral")
    else:
        print("No debe realizarse una segunda vuelta electoral")
        print(f"Partido ganador: Partido {indice + 1} con {cantidad} votos ({porc:.2f}%)")


def mostrar_nombres_ordenados(nombres):
    """Imprime la lista de nombres de partidos ya ordenada alfabeticamente."""
    print("")
    print("----- PARTIDOS ORDENADOS ALFABETICAMENTE (A-Z) -----")
    i = 0
    while i < len(nombres):
        print(f"{i + 1}. {nombres[i]}")
        i = i + 1
