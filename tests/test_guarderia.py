import sys
sys.path.append('C:\\Users\\User\\Desktop\\Backend Python\\Unidad 2\\Taller 3\\models')

import unittest
from models.guarderia import Guarderia, Boa_Constrictor

class TestGuarderia(unittest.TestCase):

    def test_alimentar_boa_no_existe(self):
        guarderia = Guarderia()
        boa_nueva = Boa_Constrictor(nombre="Cobra", peso=10.5, edad=2, pais_origen="América Del Norte", impuestos=60.0)
        resultado = guarderia.alimentar_boa(boa_nueva)
        self.assertIsNone(resultado)

    def test_ratones_comidos(self):
        guarderia = Guarderia()
        for raton in range(10):
            guarderia.alimentar_boa(guarderia.boas[0])
        resultado = guarderia.alimentar_boa(guarderia.boas[0])
        self.assertIsNone(resultado)
    
    def test_comer_raton(self):
        guarderia = Guarderia()
        resultado = guarderia.alimentar_boa(guarderia.boas[0])
        self.assertIsNone(resultado)