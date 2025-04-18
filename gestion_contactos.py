
from contacto import Contacto
import os.path
import re

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
                email = input('Email de contacto a agregar (incluye @ y .): ')
                nuevo_contacto = Contacto(nombre, telefono, email)
                if "@" and "." in email and email.strip() != "" and nombre.strip() != "" and telefono.strip() != "":
                    with open(self.nombre_archivo, 'a') as archivo:
                        archivo.write(f'{nuevo_contacto.id}, {nuevo_contacto.nombre}, {nuevo_contacto.telefono}, {nuevo_contacto.email}\n')
                    print(f'Nuevo contacto agregado: {nuevo_contacto}')
                else: 
                    print('--------------------------------------')
                    print('Asegurate de que los campos contienen información y que el formato de email sea el requerido.')
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
                        print('---------- Contacto encontrado: ----------')
                        print(contacto)
                        contacto_encontrado = True

               
                if not contacto_encontrado:
                    print('*** No existe un contacto con la información dada.***')
                
                pass

                        
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
                
        def eliminar_contacto(self, mostrar):
            self.mostrar = mostrar
            self.listar_contactos()
            print(f'''-------Eliminar contacto-------
                    ******Selecciona una opción(1-3):****** 
                    1- Por id.
                    2- Por nombre.
                    3- Por teléfono.
                    4- Por email.
                    5- Cancelar''')
            opcion = int(input('¿Qué opción desea realizar?: '))
            if opcion == 1:
                self.eliminar_por_id()
            elif opcion == 2:
                self.eliminar_por_nombre()
            elif opcion == 3:
                self.eliminar_por_telefono()
            elif opcion == 4:
                self.eliminar_por_email()
            elif opcion == 5:
                 mostrar = True
            
            
        def eliminar_por_id(self):
            id_eliminar = int(input('Por favor ingresa el id del contacto que desea eliminar: '))
            try:
                
                with open(self.nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()

                with open(self.nombre_archivo, 'w') as archivo:
                   for line in lineas:
                       id, *_ = line.strip().split(',')
                       id_int = int(id.strip())
                       if id_int != id_eliminar:
                           archivo.write(line)
                        
                            
                print(f'Id eliminada: {id_eliminar}')
                             
            
            
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
        
        def eliminar_por_nombre(self):
            nombre_eliminar = input('Por favor ingresa el nombre del contacto que desea eliminar: ')
            
            try: 
                with open(self.nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    
                print('Se han encontrado los siguientes contactos con el nombre dado: ')
                    
                with open(self.nombre_archivo, 'r') as archivo:
                    for line in lineas: 
                        _, nombre, *_ = line.strip().split(',')
                        if  (nombre_eliminar.strip()).lower() in (nombre.strip()).lower() :
                            print(line)
                    
                    self.eliminar_por_id()
                            
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')

        def eliminar_por_telefono(self):
            telefono_eliminar = int((input('Por favor ingresa el telefono del contacto que desea eliminar (sin espacios): ')).strip())
            
            try: 
                with open(self.nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    
                print('Se han encontrado los siguientes contactos con el nombre dado: ')
                    
                with open(self.nombre_archivo, 'r') as archivo:
                    for line in lineas: 
                        _, _, telefono, *_ = line.strip().split(',')
                        telefono_int = int(telefono)
                        if  telefono_int == telefono_eliminar:
                            print(line)
                    
                    self.eliminar_por_id()
                            
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')

            
            pass
        
        def eliminar_por_email(self):
            email_eliminar = input('Por favor ingresa el telefono del contacto que desea eliminar (sin espacios): ')
            
            try: 
                with open(self.nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    
                print('Se han encontrado los siguientes contactos con el nombre dado: ')
                    
                with open(self.nombre_archivo, 'r') as archivo:
                    for line in lineas: 
                        *_, email = line.strip().split(',')
                        if  (email_eliminar).strip()  in email:
                            print(line)
                    
                    self.eliminar_por_id()
                            
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            
            # try:
                
            #     # with open(self.nombre_archivo, 'r') as archivo:
            #     #     lineas = archivo.readlines()
                    
            #     # with open(self.nombre_archivo, 'w') as archivo:
            #     #     for linea in lineas:
            #     #         if contacto_a_eliminar not in linea:
            #     #             archivo.write(linea)
            #     #     print('***--- Contacto eliminado ---***')
            #     #     print(f'Se ha eliminado el siguiente "Id": {contacto_a_eliminar}')
                  
            # except Exception as e:
            #     print(f'Ha ocurrido un error: {e}')
            
        
        