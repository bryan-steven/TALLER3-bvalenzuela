from boa_constrictor import Boa_Constrictor
from huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = []
        self.hurones = []
        self.ratones_comidos = 0
        
        self.boas.append(Boa_Constrictor(nombre="Mamba", peso=12.3, edad=3, pais_origen="América Central", impuestos=75.0))
        self.boas.append(Boa_Constrictor(nombre="Guerrera", peso=15.2, edad=4, pais_origen="América Del Sur", impuestos=52.0))
        self.hurones.append(Huron(nombre="Huroncito", peso=1.5, edad=2, pais_origen="Colombia", impuestos=0.1))
        self.hurones.append(Huron(nombre="Furrito", peso=2.1, edad=1, pais_origen="Bolivia", impuestos=0.3))

    def alimentar_boa(self, boa):
        try:
            if boa is None or boa not in self.boas:
                raise ValueError("Esta boa no existe!")
                
            if self.ratones_comidos >= 10:
                raise ValueError("La boa está llena!")
            
            boa.comer_ratón()
            self.ratones_comidos += 1
            print(f"Éxito. {boa._nombre} ha comido un ratón.")
            
        except ValueError as e:
            print(e)