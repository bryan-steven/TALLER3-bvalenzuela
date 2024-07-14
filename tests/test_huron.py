import sys
sys.path.append('C:\\Users\\User\\Desktop\\Backend Python\\Unidad 2\\Taller 3\\models')

import unittest
from models.huron import Huron

huron_1 = Huron(nombre="Huroncito", peso=1.5, edad=2, pais_origen="Colombia", impuestos=0.1)

class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self):
        self.assertEqual(huron_1.hacer_sonido(),"¡Eek Eek!")
        
    def test_calcular_flete(self):
        self.assertEqual(huron_1.calcular_flete(),0.15000000000000002)