def convertir_a_romano(numero):
    
    if type(numero) is not int:
        return "ERROR: el número debe ser un entero"
    
    if not (0 < numero < 4000):
        return "ERROR: número debe estar entre 1 y 3999"
    
    millares = ["", "M", "MM", "MMM"]
    centenas = [" ","C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

    conversores = [unidades, decenas, centenas , millares]

    romano = " "
    
    for n in range(3, -1, -1):
        cociente = numero // 10 ** n
        romano = romano + conversores[n][cociente]
        numero = numero % 10 ** n

    return romano