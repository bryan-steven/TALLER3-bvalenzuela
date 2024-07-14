import sys
sys.path.append('C:\\Users\\User\\Desktop\\Backend Python\\Unidad 2\\Taller 3\\models')

import unittest
from models.boa_constrictor import Boa_Constrictor

boa_1 = Boa_Constrictor(nombre="Mamba", peso=12.3, edad=3, pais_origen="América Central", impuestos=75.0)
        
class TestBoaConstrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        self.assertEqual(boa_1.hacer_sonido(), "¡Tsss!")
        
    def test_calcular_flete(self):
        self.assertEqual(boa_1.calcular_flete(), 922.5)