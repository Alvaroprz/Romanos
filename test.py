import unittest
from romanos_funcional import romano_a_entero

class RomanosTest(unittest.TestCase):

    def test_una_sola_letra(self):
        self.assertEqual(romano_a_entero("I"), 1, "I debe valer 1")
        self.assertEqual(romano_a_entero("V"), 5, "V debe valer 5")
        self.assertEqual(romano_a_entero("X"), 10, "X debe valer 10")
        self.assertEqual(romano_a_entero("L"), 50, "L debe valer 50")
        self.assertEqual(romano_a_entero("C"), 100, "C debe valer 100")
        self.assertEqual(romano_a_entero("D"), 500, "D debe valer 500")
        self.assertEqual(romano_a_entero("M"), 1000, "M debe valer 1000")
    
    def test_no_mas_tres_simbolos_seguidos(self):
        self.assertEqual(romano_a_entero("IIII"), "ERROR: no puedes tener mas de tres veces seguidas el mismo simbolo")
    
    def test_no_repetir_letras_con_valor_cinco(self):
        self.assertEqual(romano_a_entero("VV"), "ERROR: tipo no 5 repetidos")
        self.assertEqual(romano_a_entero("LL"), "ERROR: tipo no 5 repetidos")
        self.assertEqual(romano_a_entero("DD"), "ERROR: tipo no 5 repetidos")


unittest.main()
