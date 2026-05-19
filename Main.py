# =============================================================================
# MAIN.PY
# -----------------------------------------------------------------------------
# Este es el archivo "principal" del programa. Es el que se ejecuta primero.
# El profe pide que este modulo sea CASI VACIO y que solo invoque lo necesario
# para que el programa funcione. Por eso aca adentro solo llamamos al menu.
# =============================================================================

# "from Menu import ejecutar_menu" significa: del archivo Menu.py, traeme la
# funcion llamada ejecutar_menu. Es como "importar" una herramienta de otra caja.
from Menu import ejecutar_menu

# Aca arranca todo. Llamamos a la funcion que muestra el menu y maneja todo
# el programa. Esta funcion tiene adentro un while que se repite hasta que el
# usuario elija salir.
ejecutar_menu()
