from gestion_contactos import GestionContactos

class AppContactos:
    
    def __init__(self):
        self.gestion_contactos = GestionContactos()
        
        
            
    def mostrar_menu(self):
        mostrar = True
        print(f'''**** Bienvenido ****
              1. Agregar contacto
              2. Mostrar todos los contactos
              3. Buscar un contacto
              4. Eliminar un contacto
              5. Salir del menú''')
        opcion = int(input('Seleccione una opción (1-5): '))
        
        
        if opcion == 1:
            self.gestion_contactos.agregar_contacto()
        elif opcion == 2:
            self.gestion_contactos.listar_contactos()
        elif opcion == 3:
            self.gestion_contactos.buscar_contacto()
        elif opcion == 4:
            self.gestion_contactos.eliminar_contacto()
        elif opcion == 5:
           print('Nos vemos pronto!')
           mostrar = None
        else: 
            print('Por favor, ingresa un valor válido.')

        if mostrar:
            self.mostrar_menu()

if __name__ == '__main__':
    app_contactos = AppContactos()
    app_contactos.mostrar_menu()



