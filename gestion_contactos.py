
from contacto import Contacto
import os.path

class GestionContactos:
        
        nombre_archivo = "lista_contactos.txt"
        
        def __init__(self):
            self.contactos = []
            if os.path.isfile(self.nombre_archivo):
                self.contactos = self.obtener_contactos_archivo()
            else: 
                self.agregar_ejemplos()
                
            
        def agregar_ejemplos(self):
            ejemplos = [
                Contacto("Alcides", "675304234","alcidescon@gmailcom" ),
                Contacto("Roberto", "722181442","roberxiri@gmail.com" ),
                Contacto("Facundo", "692916064","facuscrollinic@gmail.com")
            ]
            
            with open(self.nombre_archivo, 'a') as archivo:
                for ejemplo in ejemplos:
                    archivo.write(f'{ejemplo.id}, {ejemplo.nombre},{ejemplo.telefono},{ejemplo.email}\n')
                    
                
            
        def obtener_contactos_archivo(self):
            contactos_archivo = []
            try:
                with open(self.nombre_archivo, 'r') as archivo:
                    for line in archivo:
                        id, nombre, telefono, email = line.strip().split(',')
                        contacto = Contacto(nombre, telefono, email)
                        contactos_archivo.append(contacto)
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            
            return contactos_archivo
                
                
            
        def agregar_contacto(self):
            try:
                nombre = input('Nombre de contacto a agregar: ')
                telefono = input('Telefono de contacto a agregar: ')
                email = input('Email de contacto a agregar: ')
                nuevo_contacto = Contacto(nombre, telefono, email)
                if "@" and "." in email:
                    with open(self.nombre_archivo, 'a') as archivo:
                        archivo.write(f'{nuevo_contacto.id}, {nuevo_contacto.nombre}, {nuevo_contacto.telefono}, {nuevo_contacto.email}\n')
                    print(f'Nuevo contacto agregado: {nuevo_contacto}')
                else: 
                    print('--------------------------------------')
                    print('El campo de email debe contener "@" y "." ')
                    print('--------------------------------------')
            
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
        def listar_contactos(self):
            try:
                with open(self.nombre_archivo, 'r') as archivo:
                    print(archivo.read())
                    
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
        
        def buscar_contacto(self):
            contacto_encontrado = None
            usuario_buscado = input('Introduce el nombre del contacto a buscar: ').lower()
            try:
                for contacto in self.contactos:
                    if usuario_buscado in contacto.nombre.strip().lower():
                        contacto_encontrado = contacto

                if contacto_encontrado:
                    print('*** Usuario encontrado ***')
                    print(contacto_encontrado)
                else:
                    print('*** Usuario no encontrado ***')
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
                
        def eliminar_contacto(self):
            contacto_a_eliminar = input('Introduce el nombre del contacto a eliminar: ')
            try:
                with open(self.nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    
                with open(self.nombre_archivo, 'w') as archivo:
                    for linea in lineas:
                        if contacto_a_eliminar not in linea:
                            archivo.write(linea)
                    print('***--- Contacto eliminado ---***')
                    print(f'Se ha eliminado el contacto: {contacto_a_eliminar}')
                  
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            
        
        