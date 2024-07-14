from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_ratón(self):
        if self._ratones_comidos >= 20:
            raise ValueError("La boa está llena!")
        else:
            self._ratones_comidos += 1
            print("Éxito")
            
    def obtener_ratones_comidos(self):
        return self._ratones_comidos