class Contacto:
    contador_id = 0
    
    def __init__(self, nombre, telefono, email):
        Contacto.contador_id += 1
        self.id = Contacto.contador_id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        return f'Id: {self.id}, Nombre:{self.nombre}, Telefono: {self.telefono}, Email: {self.email}'
    
    