def convertir_a_romano(numero):
    """
    Convierte el valor de `numero` a una cadena que
    representa el valor de ese número entero como
    número romano.
    """

    # comprobar que `numero` es un entero
    if type(numero) is not int:
        return 'ERROR: el número debe ser un entero'

    # `numero` está entre 1 y 3999 (incluidos)
    # if not (0 < numero < 4000):
    if numero < 1 or numero > 3999:
        return 'ERROR: número debe estar entre 1 y 3999'

    millares = ['', 'M', 'MM', 'MMM']
    centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    decenas = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    conversores = [unidades, decenas, centenas, millares]

    # conversores = [
    #     ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    #     ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    #     ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    #     ['', 'M', 'MM', 'MMM'                                      ]
    # ]

    romano = ''

    for n in range(3, -1, -1):
        cociente = numero // 10 ** n
        romano = romano + conversores[n][cociente]
        numero = numero % 10 ** n

    return romano


def romano_a_entero(romano):
    """
    MCXXIII ====> 1123
    """
    digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    if not isinstance(romano, str):
        return 'ERROR: el número romano debe ser una cadena'

    if romano == '':
        return 'ERROR: no se admite la cadena vacía'
    
    resultado = 0
    anterior = 0
    for letra in romano:
        if letra not in digitos_romanos:
            return 'ERROR: no son símbolos de número romano válidos'
        
        actual = digitos_romanos.get(letra)

        if anterior < actual:
            resultado = resultado + actual - anterior * 2

        else:
            resultado = resultado + actual
        anterior = actual

    return resultado


pruebas = [
    #'A', '', 'XXii', 3, ['X', 'X'], 
    'I', 'MCXXIII', 'XVI', 'CDVII'
]

for elem in pruebas:
    print(elem, romano_a_entero(elem))
