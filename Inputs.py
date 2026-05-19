# =============================================================================
# INPUTS.PY
# -----------------------------------------------------------------------------
# Este modulo se encarga UNICAMENTE de pedir datos al usuario y validarlos.
# El profe lo separa asi para tener el codigo ordenado: una "caja" para entradas,
# otra para salidas (Prints.py), otra para la logica (Funciones.py), etc.
# Si una funcion pide algo por teclado y lo valida, va aca.
# =============================================================================


def pedir_entero_positivo(mensaje):
    """
    Pide al usuario un numero entero positivo (mayor a cero).
    Si ingresa cualquier cosa que no sea un numero valido (letras, decimales,
    negativos o cero) le vuelve a pedir hasta que ingrese algo correcto.

    Parametro:
        mensaje (str): el texto que se le muestra al usuario al pedirle el dato.
                       Por ejemplo: "Ingrese los votos del partido 1: "

    Devuelve:
        int: el numero entero positivo que ingreso el usuario.
    """

    # Esta variable "bandera" (flag) sirve para saber si ya recibi un dato valido.
    # Mientras sea False, el while sigue pidiendo. Cuando pase a True, sale del loop.
    valido = False

    # Inicializo la variable numero en 0. La voy a sobreescribir mas adelante.
    # Necesito declararla aca afuera porque la quiero usar despues del while.
    numero = 0

    # "while not valido" significa: mientras NO sea valido, repeti.
    # not invierte el booleano. Si valido es False, not valido es True, entra al while.
    while not valido:
        # input() muestra el mensaje y espera que el usuario escriba algo + Enter.
        # Lo que ingresa siempre llega como STRING (texto), aunque escriba numeros.
        entrada = input(mensaje)

        # El bloque try/except sirve para manejar errores sin que el programa "rompa".
        # Si lo que el usuario escribio NO se puede convertir a numero (por ejemplo
        # escribio "hola"), int(entrada) tira un error llamado ValueError. Con except
        # lo "atrapamos" y mostramos un mensaje en vez de que el programa explote.
        try:
            # int(entrada) intenta convertir el texto a numero entero.
            # Si entrada = "42" -> numero = 42.
            # Si entrada = "abc" -> tira ValueError y salta al except.
            numero = int(entrada)

            # Una vez que ya tengo un numero, verifico que sea mayor a cero
            # (el PDF dice que no se permiten ni negativos ni ceros).
            if numero > 0:
                # Si es positivo, marco la bandera como True para que el while termine.
                valido = True
            else:
                # Si es 0 o negativo, le aviso y NO cambio la bandera,
                # asi el while se vuelve a repetir.
                print("Error: no se permiten numeros negativos ni el cero")
        except ValueError:
            # Aca caemos cuando int() no pudo convertir el texto.
            # Le avisamos al usuario y volvemos a repetir el while.
            print("Error: tenes que ingresar un numero entero")

    # Cuando salgo del while es porque el numero es valido. Lo devuelvo
    # con return para que la funcion que me llamo lo pueda usar.
    return numero


def pedir_opcion_menu():
    """
    Pide al usuario una opcion del menu (numero entre 0 y 12).
    Funciona igual que pedir_entero_positivo pero validando el rango del menu.

    Devuelve:
        int: la opcion elegida por el usuario.
    """

    # Misma idea que la funcion anterior: una bandera para controlar el while.
    valido = False

    # Inicializo en -1 (un valor "invalido") para asegurarme de que si por algun
    # motivo el while no entrara, no devolvamos una opcion valida sin querer.
    opcion = -1

    while not valido:
        entrada = input("Ingrese una opcion: ")
        try:
            opcion = int(entrada)
            # Verifico que la opcion este dentro del rango permitido del menu.
            # El 0 es "salir" y del 1 al 12 son las opciones del PDF.
            if opcion >= 0 and opcion <= 12:
                valido = True
            else:
                print("Error: la opcion debe estar entre 0 y 12")
        except ValueError:
            print("Error: tenes que ingresar un numero")

    return opcion
