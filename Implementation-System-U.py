from abc import ABC,abstractmethod

class Persona (ABC):
    def __init__(self,nombre,dni,edad):
        self.nombre = nombre
        self.__dni = dni
        self.edad = edad
    
    @property
    def dni (self):
        return self.__dni

    @dni.setter
    def dni(self,valor):
        if not isinstance(valor,str) or len(valor) != 8 or not valor.isdigit():
            raise ValueError (f"Dni Invalido: '{valor}' debe ser de 8 digitos")
        self.__dni = valor

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni}) - {self.rol}"

    def __eq__(self,otro):
        if not isinstance(otro,Persona):
            return False
        return self.dni == otro.dni

    def __repr__(self):
        return f"{type(self).__name__} ('{self.nombre}','{self.dni}','{self.edad}')"

    @abstractmethod
    def rol (self): 
        pass

    def presentarte(self):
        return f"Soy {self.nombre} , {self.rol()}"
    
class Estudiante(Persona):
    def __init__(self,nombre,dni,edad,codigo,carrera,ciclo):
        super().__init__(nombre,dni,edad)
        self.codigo = codigo
        self.carrera = carrera
        self.ciclo = ciclo


    def rol(self):
        return f"Mi nombre es {self.nombre} soy Estudiante de {self.carrera}"

class Docente(Persona):
    Categorias_Aceptadas = ("Auxiliar","Asociado","Principal")
    sueldo_base = {"Auxiliar":2500 , "Asociado":3500 , "Principal": 5000}

    def __init__(self,nombre,dni,edad,especialidad,categoria,horas_clase):
        super().__init__(nombre,dni,edad)
        #Si la categoria no se encuentra en la tupla aceptada entonces no procede con el valor
        if categoria not in self.Categorias_Aceptadas :
            raise ValueError(f"Categoria invalida: '{categoria}' ")

        self.especialidad = especialidad
        self.categoria = categoria #Solo aceptar Auxiliar Asociado o Principal
        self.horas_clase = horas_clase
    
    def calcular_sueldo (self):
        base = self.sueldo_base[self.categoria]
        bono_horas = self.horas_clase * 50
        return base + bono_horas
    
    def rol (self):
        return f"Docente de {self.categoria} de {self.especialidad}"
    
class DocenteInvestigador(Docente):

    bono_por_publicacion = 200

    def __init__(self,nombre,dni,edad,especialidad,categoria,horas_clase,publicaciones):
        super().__init__(nombre,dni,edad,especialidad,categoria,horas_clase)
        self.publicaciones = publicaciones
    
    def calcular_sueldo(self):
        sueldo_docente = super().calcular_sueldo()
        bono_investigacion = self.bono_por_publicacion * self.publicaciones
        return sueldo_docente + bono_investigacion
    
    def rol(self):
        return f"Docente Investigador de {self.especialidad} || {self.publicaciones} pub."
    
if __name__ == "__main__":

    # ═══════════════════════════════════════════════════════════════
    #  PROGRAMA DE PRUEBA
    # ═══════════════════════════════════════════════════════════════
    personal = [
        Estudiante("Lucas mori", "11111111", 20, "2026001", "Ing. Sistemas", 4),
        Estudiante("Banny Dad", "22222222", 19, "2026002", "Ing. Sistemas", 2),
        Docente("Richard Albiño", "33333333", 35, "Fisica Electronica", "Asociado", 20),
        Docente("Juan Verme", "44444444", 50, "Base de Datos", "Principal", 16),
        DocenteInvestigador("María Sánchez", "55555555", 42,"Inteligencia Artificial", "Asociado", 12, 8),
    ]

    print("� Personal de la Unap\n")
    for p in personal:
        print(f" •  {p.presentarte()}")

    #Filtrar y Calcular plantilla
    docentes = [p for p in personal if isinstance (p,Docente)]
    for d in docentes :
        print(f"\n {d.nombre}: S/.{d.calcular_sueldo():,.2f} - {d.rol()}")
    total_planilla = sum(d.calcular_sueldo() for d in docentes)
    print (f"\n TOTAL: S/. {total_planilla:,.2f}")

    #Verificar __eq__
    print(f"\n🔍 ¿Ana == Ana? {personal[0] == personal[0]}")    
    print(f"🔍 ¿Ana == Luis? {personal[0] == personal[1]}")     
    
    print ("\nValidacion de Dni: ")
    try: 
         Estudiante("Test", "123", 20, "X", "Test", 1)
    except ValueError as e:
        print(f"Error esperado : {e}")

     #Verificar validación de categoría
    print("\nValidación de categoría:")
    try:
        Docente("Test", "99999999", 30, "Test", "Supremo", 10)
    except ValueError as e:
        print(f"  Error esperado: {e}")

    # Verificar que no se puede instanciar Persona
    print("\nClase abstracta:"
    )
    try:
        Persona("Test", "99999998", 25)
    except TypeError as e:
        print(f"  Error esperado: {e}")
    






