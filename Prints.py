# =============================================================================
# PRINTS.PY
# -----------------------------------------------------------------------------
# Este modulo se encarga UNICAMENTE de mostrar cosas por pantalla.
# Toda funcion que usa print() o que tiene como tarea principal "armar la
# salida visual" va aca. La idea es separar PRESENTACION de LOGICA.
#
# Estas funciones reciben datos ya calculados (o piden a Funciones.py que se
# los calcule) y los muestran formateados.
# =============================================================================

# Importo todas las funciones de Funciones.py que necesito para mostrar datos.
# Notar que NO importo nada de Menu.py: las dependencias van en una sola
# direccion (Prints -> Funciones -> Inputs), nunca al reves. Si se cruzaran
# (Prints importa Menu y Menu importa Prints) habria un "import circular" que
# rompe el programa.
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
    """
    Muestra el menu de opciones por pantalla. No recibe ni devuelve nada,
    su unica tarea es imprimir el menu.
    """
    # Imprimo una linea vacia para separar visualmente del texto anterior.
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
    """
    Muestra un mensaje generico (avisos, confirmaciones, errores).
    Se usa para no repetir print("") + print(...) en cada llamada del menu.
    """
    print("")
    print(msg)


def mostrar_listado(votos):
    """
    Muestra el listado completo de partidos con sus votos y porcentajes
    (opcion 2 del menu).

    Tambien muestra:
      - cantidad de partidos postulados
      - cantidad total de votos
    """

    # Pido el total a Funciones.py. Yo no calculo nada aca, solo muestro.
    total = calcular_total(votos)

    print("")
    print("----- LISTADO DE PARTIDOS -----")

    # f-strings ({variable}) permiten meter el valor de una variable dentro de un texto.
    print(f"Cantidad de partidos postulados: {len(votos)}")
    print(f"Cantidad total de votos: {total}")
    print("")

    i = 0
    while i < len(votos):
        # Por cada partido, calculo su porcentaje y lo muestro.
        porc = calcular_porcentaje(votos[i], total)

        # :.2f despues de la variable significa "formatear como flotante con
        # 2 decimales". El profe lo recomienda para que se vea prolijo.
        # i + 1 porque el usuario cuenta desde 1, no desde 0.
        print(f"Partido {i + 1}: {votos[i]} votos ({porc:.2f}%)")
        i = i + 1


def mostrar_filtrados_menos(votos, limite):
    """
    Muestra los partidos que tienen MENOS de cierto porcentaje del total.
    Sirve para los puntos 3, 4 y 5 (cambia solo el limite: 10, 15 o 20).

    Reutilizar la misma funcion para tres opciones diferentes del menu es
    aprovechar bien el codigo: cambia un parametro y listo.
    """

    # La funcion de Funciones.py me devuelve TRES listas a la vez.
    # Las "desempaqueto" en tres variables separadas en una sola linea.
    indices, cantidades, porcentajes = filtrar_menores_a_porcentaje(votos, limite)

    print("")
    print(f"----- PARTIDOS CON MENOS DEL {limite}% DE VOTOS -----")

    # Si no encontre ningun partido que cumpla, muestro un mensaje de error
    # tal como pide el PDF en el punto 3.a.
    # "return" sin valor corta la funcion sin devolver nada (sale de aca).
    if len(indices) == 0:
        print("No hay partidos que cumplan esta condicion")
        return

    # Acumulador para sumar los porcentajes de todos los partidos encontrados
    # (lo pide el punto 3.c del PDF: "porcentaje acumulado").
    acumulado = 0
    i = 0
    while i < len(indices):
        # indices[i] me dice en que posicion ORIGINAL estaba el partido.
        # Por eso le sumo 1 para mostrarlo numerado desde 1 al usuario.
        print(f"Partido {indices[i] + 1}: {cantidades[i]} votos ({porcentajes[i]:.2f}%)")
        acumulado = acumulado + porcentajes[i]
        i = i + 1

    print(f"Porcentaje acumulado de la busqueda: {acumulado:.2f}%")


def mostrar_filtrados_mas(votos, limite):
    """
    Muestra los partidos que tienen MAS de cierta CANTIDAD de votos.
    Sirve para los puntos 6 (500) y 7 (1000).

    Ademas muestra al final: suma de votos, cantidad de partidos y promedio.
    """

    indices, cantidades, porcentajes = filtrar_mayores_a_cantidad(votos, limite)

    print("")
    print(f"----- PARTIDOS CON MAS DE {limite} VOTOS -----")

    if len(indices) == 0:
        print("No hay partidos que cumplan esta condicion")
        return

    # Sumador para calcular el total de votos de los resultados (no del total general).
    suma = 0
    i = 0
    while i < len(indices):
        print(f"Partido {indices[i] + 1}: {cantidades[i]} votos ({porcentajes[i]:.2f}%)")
        suma = suma + cantidades[i]
        i = i + 1

    # Promedio de los resultados encontrados (NO de todos los partidos).
    promedio_busqueda = suma / len(indices)
    print(f"Suma de votos: {suma}")
    print(f"Cantidad de partidos encontrados: {len(indices)}")
    print(f"Promedio de votos: {promedio_busqueda:.2f}")


def mostrar_arriba_promedio(votos):
    """
    Muestra los partidos que superan el promedio general de todos los votos
    (opcion 8 del menu). Tambien muestra el promedio y el porcentaje acumulado.
    """

    # La funcion me devuelve 4 valores esta vez (le agregue el promedio).
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
    """
    Muestra el partido menos votado, o si hay varios empatados los muestra a todos
    (opcion 9 + punto extra del parcial por contemplar empates).
    """

    # indices puede tener 1 elemento (sin empate) o varios (con empate).
    indices, minimo = buscar_menos_votado(votos)
    total = calcular_total(votos)

    # El porcentaje es el mismo para todos los empatados porque tienen los mismos votos.
    porc = calcular_porcentaje(minimo, total)

    print("")
    print("----- PARTIDO MENOS VOTADO -----")

    if len(indices) == 1:
        # Caso normal: un solo partido fue el menos votado.
        print(f"Partido {indices[0] + 1}: {minimo} votos ({porc:.2f}%)")
    else:
        # Caso con empate: aviso que hay empate y los muestro a todos.
        print("Hay un empate entre los siguientes partidos:")
        i = 0
        while i < len(indices):
            print(f"Partido {indices[i] + 1}: {minimo} votos ({porc:.2f}%)")
            i = i + 1


def mostrar_segunda_vuelta(votos):
    """
    Muestra si hay segunda vuelta o no (opcion 10).
    Si NO hay segunda vuelta, muestra ademas la info del ganador.
    """

    # Desempaqueto los 4 valores que devuelve la funcion.
    hay_segunda, indice, cantidad, porc = verificar_segunda_vuelta(votos)

    print("")
    print("----- VERIFICACION DE SEGUNDA VUELTA -----")

    if hay_segunda:
        # Mensaje exacto que pide el PDF.
        print("Debe realizarse una segunda vuelta electoral")
    else:
        print("No debe realizarse una segunda vuelta electoral")
        print(f"Partido ganador: Partido {indice + 1} con {cantidad} votos ({porc:.2f}%)")


def mostrar_nombres_ordenados(nombres):
    """
    Muestra la lista de nombres de partidos ya ordenada alfabeticamente (opcion 12).
    """

    print("")
    print("----- PARTIDOS ORDENADOS ALFABETICAMENTE (A-Z) -----")
    i = 0
    while i < len(nombres):
        # i + 1 para mostrarlos numerados desde 1.
        print(f"{i + 1}. {nombres[i]}")
        i = i + 1
