# =============================================================================
# MENU.PY
# -----------------------------------------------------------------------------
# Este modulo es el "director de orquesta" del programa. Tiene la funcion
# principal que muestra el menu, lee la opcion del usuario y decide a quien
# llamar para resolver lo que pidio.
#
# La logica de cada opcion NO esta aca (eso vive en Funciones.py y Prints.py).
# Aca solo decidimos QUE HACER segun lo que apreto el usuario.
# =============================================================================

# Traigo lo necesario de los otros modulos:
# - de Inputs: la funcion que pide la opcion del menu validandola
# - de Funciones: las funciones de logica que voy a invocar
# - de Prints: las funciones que muestran los resultados
from Inputs import pedir_opcion_menu
from Funciones import cargar_votos, hardcodear_votos, ordenar_nombres
from Prints import (
    mostrar_menu,
    mostrar_mensaje,
    mostrar_listado,
    mostrar_filtrados_menos,
    mostrar_filtrados_mas,
    mostrar_arriba_promedio,
    mostrar_menos_votado,
    mostrar_segunda_vuelta,
    mostrar_nombres_ordenados,
)

# CONSTANTE: una variable cuyo valor no va a cambiar durante el programa.
# Por convencion se escribe en MAYUSCULAS. Tener esto separado en una sola
# linea permite cambiar facilmente la cantidad de partidos sin tocar el resto
# del codigo (cumple el requisito del PDF: "el sistema debe funcionar igual
# si cambia el tamano del vector").
CANTIDAD_PARTIDOS = 5


def ejecutar_menu():
    """
    Esta es LA funcion principal del programa. Maneja todo el ciclo:
      1. Muestra el menu
      2. Pide la opcion al usuario
      3. Ejecuta la opcion correspondiente
      4. Repite hasta que el usuario elija salir
    """

    # Lista vacia donde se van a guardar los votos cuando el usuario los cargue.
    # Esta variable es LOCAL a esta funcion (no existe afuera).
    votos = []

    # Bandera para saber si los votos ya fueron cargados o no. Esto sirve para
    # bloquear el acceso a las opciones 2-10 antes de cargar nada (lo pide el PDF).
    votos_cargados = False

    # Lista hardcodeada con los nombres de los partidos para el punto 12.
    # Ojo: este punto es INDEPENDIENTE de los votos. Por eso esta lista
    # no se modifica ni se relaciona con la otra.
    nombres_partidos = [
        "Frente UTN",
        "Alianza Scarafilo",
        "La libertad de Baus",
        "Unidad de Python",
        "Frente de Java",
    ]

    # Bandera para controlar el while principal del programa.
    salir = False

    # Bucle principal: se ejecuta hasta que el usuario elija salir (opcion 0).
    while not salir:
        mostrar_menu()

        # Pido la opcion validada al modulo Inputs.
        # Esta funcion ya valida que sea numero y que este en el rango 0-12.
        opcion = pedir_opcion_menu()

        # Cascada de if/elif: solo se ejecuta UNA opcion segun lo que eligio.
        # Es como un "switch" de otros lenguajes pero en Python se hace con if/elif.

        if opcion == 0:
            # Salida limpia del programa.
            mostrar_mensaje("Saliendo del sistema...")
            salir = True

        elif opcion == 1:
            # Carga manual de votos pidiendolos uno por uno al usuario.
            # Le paso la cantidad de partidos como parametro para que la funcion
            # sea generica (sirve tambien si cambio CANTIDAD_PARTIDOS).
            votos = cargar_votos(CANTIDAD_PARTIDOS)
            votos_cargados = True
            mostrar_mensaje("Votos cargados correctamente")

        elif opcion == 11:
            # Hardcodear: reemplaza completamente lo que habia en votos
            # con el vector predefinido de 10 partidos.
            votos = hardcodear_votos()
            votos_cargados = True
            mostrar_mensaje("Vector hardcodeado correctamente (10 partidos)")

        elif opcion == 12:
            # Punto 12 es INDEPENDIENTE: no necesita votos cargados, trabaja
            # solo con la lista de nombres. Por eso lo pongo aca afuera del
            # bloque que valida votos_cargados.
            ordenados = ordenar_nombres(nombres_partidos)
            mostrar_nombres_ordenados(ordenados)

        elif opcion >= 2 and opcion <= 10:
            # GUARDA DE ACCESO: si la opcion es del 2 al 10 y todavia no se
            # cargaron los votos, no dejo continuar. Esto es lo que pide el PDF:
            # "el usuario no deberia poder acceder a ninguna otra opcion si
            #  antes no cargo los votos".
            if not votos_cargados:
                mostrar_mensaje("Primero tenes que cargar los votos (opcion 1 u 11)")
            else:
                # Si ya hay votos, ejecuto la opcion correspondiente.
                # Cada una llama a una funcion de Prints (que internamente
                # le pide los calculos a Funciones).
                if opcion == 2:
                    mostrar_listado(votos)
                elif opcion == 3:
                    # Le paso el limite 10 -> partidos con < 10% del total.
                    mostrar_filtrados_menos(votos, 10)
                elif opcion == 4:
                    mostrar_filtrados_menos(votos, 15)
                elif opcion == 5:
                    mostrar_filtrados_menos(votos, 20)
                elif opcion == 6:
                    # Limite 500 -> partidos con MAS de 500 votos.
                    mostrar_filtrados_mas(votos, 500)
                elif opcion == 7:
                    mostrar_filtrados_mas(votos, 1000)
                elif opcion == 8:
                    mostrar_arriba_promedio(votos)
                elif opcion == 9:
                    mostrar_menos_votado(votos)
                elif opcion == 10:
                    mostrar_segunda_vuelta(votos)
        else:
            # En teoria esta rama nunca se ejecuta porque pedir_opcion_menu()
            # ya valida el rango 0-12. La dejo igual como "red de seguridad"
            # por si alguien cambia esa validacion en el futuro.
            mostrar_mensaje("Opcion invalida")
