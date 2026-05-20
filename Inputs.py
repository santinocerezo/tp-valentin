def pedir_entero_positivo(mensaje):
    """Pide un entero mayor a cero y reintenta hasta recibir uno valido."""
    valido = False
    numero = 0
    while not valido:
        entrada = input(mensaje)
        try:
            numero = int(entrada)
            if numero > 0:
                valido = True
            else:
                print("Error: no se permiten numeros negativos ni el cero")
        except ValueError:
            print("Error: tenes que ingresar un numero entero")
    return numero


def pedir_opcion_menu():
    """Pide una opcion del menu entre 0 y 12, reintentando si es invalida."""
    valido = False
    opcion = -1
    while not valido:
        entrada = input("Ingrese una opcion: ")
        try:
            opcion = int(entrada)
            if opcion >= 0 and opcion <= 12:
                valido = True
            else:
                print("Error: la opcion debe estar entre 0 y 12")
        except ValueError:
            print("Error: tenes que ingresar un numero")
    return opcion
