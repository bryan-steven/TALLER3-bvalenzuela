from animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    def hacer_sonido(self):
        return "¡Eek Eek!"
    
    def calcular_flete(self):
        return super().calcular_flete()