class alumno:
    def __init__(self,nombre,apellido,edad,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad        
        self.nacionalidad=nacionalidad
        self.nota=""      
    
    def registrarNota(self, nota):
        self.nota=int(nota)

