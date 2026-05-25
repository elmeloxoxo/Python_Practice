from abc import ABC, abstractmethod
import math 

class Forma(ABC):
    #Constructor de clase abstracta
    def __init__(self,nombre):
        self.nombre = nombre
        pass

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Cuadrado(Forma):
    def __init__(self,lado):
        super().__init__("Cuadrado")
        self.lado = lado
    
    def calcular_area(self):
        return self.lado **2

    def calcular_perimetro(self):
        return 4 * self.lado 
    
class Circulo(Forma):
    def __init__(self,radio):
        super().__init__("Circulo")
        self.radio = radio
    
    def calcular_area(self):
        return f"el area del Circulo es : {math.pi * (self.radio ** 2):.2f} m**2" 

    def calcular_perimetro(self):
        return f"el perimetro es {2 * math.pi * self.radio:.2f} m"  
    

c = Circulo(62)
print(c.radio)

print(c.calcular_area())

print(c.calcular_perimetro())
