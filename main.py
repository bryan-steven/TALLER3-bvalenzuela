import sys
sys.path.append('C:\\Users\\User\\Desktop\\Backend Python\\Unidad 2\\Taller 3\\models')

from models.huron import Huron

mi_huron = Huron(nombre="Huroncito", peso=1.5, edad=2, pais_origen="Argentina", impuestos=0.1)

sonido = mi_huron.hacer_sonido()
print(sonido)