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

CANTIDAD_PARTIDOS = 5


def ejecutar_menu() -> None:
    """Bucle principal: muestra el menu y ejecuta la opcion elegida por el usuario."""
    votos = []
    votos_cargados = False
    nombres_partidos = [
        "Frente UTN",
        "Alianza Scarafilo",
        "La libertad de Baus",
        "Unidad de Python",
        "Frente de Java",
    ]

    salir = False
    while not salir:
        mostrar_menu()
        opcion = pedir_opcion_menu()

        if opcion == 0:
            mostrar_mensaje("Saliendo del sistema...")
            salir = True
        elif opcion == 1:
            votos = cargar_votos(CANTIDAD_PARTIDOS)
            votos_cargados = True
            mostrar_mensaje("Votos cargados correctamente")
        elif opcion == 11:
            votos = hardcodear_votos()
            votos_cargados = True
            mostrar_mensaje("Vector hardcodeado correctamente (10 partidos)")
        elif opcion == 12:
            ordenados = ordenar_nombres(nombres_partidos)
            mostrar_nombres_ordenados(ordenados)
        elif opcion >= 2 and opcion <= 10:
            if not votos_cargados:
                mostrar_mensaje("Primero tenes que cargar los votos (opcion 1 u 11)")
            else:
                if opcion == 2:
                    mostrar_listado(votos)
                elif opcion == 3:
                    mostrar_filtrados_menos(votos, 10)
                elif opcion == 4:
                    mostrar_filtrados_menos(votos, 15)
                elif opcion == 5:
                    mostrar_filtrados_menos(votos, 20)
                elif opcion == 6:
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
            mostrar_mensaje("Opcion invalida")
