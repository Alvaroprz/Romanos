from romanos import romano_a_entero

no_valida  = True

while no_valida:
    try:
        numero = input("Escribe un número romano: ")
        print(romano_a_entero(numero))
    except TypeError as ex:
        print("No puedo convertir a entero eso que me pides")
        print(ex)
    except ValueError as error:
        print("No puedo convertir eso que tú me das")
        print(error)