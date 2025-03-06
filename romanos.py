class Romano:
    def __init__(self, entrada):
        print("Creando un romano a partir de", entrada)
        if isinstance(entrada, str):
            self.cadena = entrada
        elif isinstance(entrada, int):
            self.valor = entrada
        else:
            raise TypeError("Solo acepto cadenas o enteros")
        
    def convertir_a_romano(self):
        """
        Convierte el valor de `numero` a una cadena que
        representa el valor de ese número entero como
        número romano.
        """

        numero = self.valor

        if type(numero) is not int:
            return 'ERROR: el número debe ser un entero'

        if numero < 1 or numero > 3999:
            return 'ERROR: número debe estar entre 1 y 3999'

        millares = ['', 'M', 'MM', 'MMM']
        centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        decenas = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        conversores = [unidades, decenas, centenas, millares]

        romano = ''

        for n in range(3, -1, -1):
            cociente = numero // 10 ** n
            romano = romano + conversores[n][cociente]
            numero = numero % 10 ** n

        return romano

    def romano_a_entero(self) -> int:

        romano = self.cadena

        digitos_romanos = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }

        if not isinstance(romano, str):
            raise TypeError(
                'El parámetro "romano" debe ser una cadena de texto que representa un número romano')

        if romano == '':
            raise ValueError('No se admite la cadena vacía')

        pares_no_validos = ['VV', 'LL', 'DD']
        for par in pares_no_validos:
            if par in romano:
                raise ValueError('No puede haber repetidas ni V, ni L, ni D')

        resultado = 0
        anterior = 0
        repeticiones = 0

        # - leemos las letras de izquierda a derecha
        for letra in romano:
            if letra not in digitos_romanos:
                raise ValueError('No son símbolos de número romano válidos')

            actual = digitos_romanos.get(letra)

            if actual == anterior:
                repeticiones = repeticiones + 1
            else:
                repeticiones = 1

            if repeticiones > 3:
                # FIX: Lanzar una excepción en lugar de hacer return
                return 'ERROR: no puedes tener más de tres veces seguidas la misma letra'

            if anterior < actual:
                # if anterior > 0 and anterior < actual / 10:
                es_resta_valida = self.resta_valida(anterior, actual)
                if es_resta_valida:
                    # RESTA!!!! actual - anterior
                    # resultado = resultado - anterior + (actual - anterior)
                    resultado = resultado + actual - anterior * 2
                else:
                    # FIX: Lanzar una excepción en lugar de hacer return
                    return 'ERROR: no puedo restar eso!!'
            else:
                # - vamos acumulando el valor sumando al anterior
                resultado = resultado + actual
            anterior = actual

        # - cuando ya no quedan más letras, el valor acumulado es el resultado
        return resultado

    def resta_valida(self, anterior: int, actual: int) -> bool:
        """
        Devuelve `True` si el valor de `anterior` se puede restar
        del valor `actual` en un número romano.

        Ejemplo: 1 (I) puede restar a 5 (V) pero 1 (I) no puede restar a 50 (L)
        """
        es_cero = anterior == 0
        resta_tipo_uno = actual == anterior * 5 or actual == anterior * 10
        no_es_tipo_cinco = anterior not in (5, 50, 500)
        es_resta_valida = (es_cero or resta_tipo_uno) and no_es_tipo_cinco
        return es_resta_valida