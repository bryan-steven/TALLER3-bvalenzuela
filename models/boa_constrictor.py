from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_ratón(self):
        if self._ratones_comidos >= 10:
            raise ValueError("Demasiados Ratones!")
        else:
            self._ratones_comidos += 1
            print(f"{self._nombre} ha comido un ratón.")
            
    def obtener_ratones_comidos(self):
        return self._ratones_comidos