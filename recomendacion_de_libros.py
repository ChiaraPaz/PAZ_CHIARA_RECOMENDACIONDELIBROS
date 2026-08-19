#Recomendación de libros 
import csv
import os

class Libro: #se arma la clase de libro con sus atributos
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
        
        
#se arma la lista de libros y se cargan desde el archivo CSV
lista_libros = []

ruta_csv = os.path.join(os.path.dirname(__file__), 'libros.csv') if '__file__' in locals() else 'libros.csv'
if not os.path.exists(ruta_csv):
    ruta_csv = 'libros.csv'

with open(ruta_csv, mode='r', encoding='utf-8-sig') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        libro = Libro(fila['titulo'], fila['autor'], fila['genero'], float(fila['puntuacion']))
        lista_libros.append(libro)

print('\n Bienvenida a tu librería virtual!')
while True: #se arma el bucle para que el usuario pueda elegir el género de libro que desea
    
    print('\n Menú:')
    print('1. Agregar un libro')
    print('2. Buscar libros por género')
    print('3. Recomendación de libro')
    print('4. Terminar conversación')
    
    opcion = input('\n Ingrese el número de la opción que desea: ')
       
    if opcion == '1':
        titulo = input('\n Ingrese el título del libro: ')
        autor = input('\n Ingrese el autor del libro: ')
        genero = input('\n Ingrese el género del libro: ')
        puntuacion = float(input('\n Ingrese la puntuación del libro (0-5): '))
        
        nuevo_libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(nuevo_libro)
        print(f'El libro "{titulo}" ha sido agregado a la lista.')
    
    elif opcion == '2':
        genero_busqueda = input('\n Ingrese el género de libro que desea buscar: ')
        libros_encontrados = [libro for libro in lista_libros if libro.genero.lower() == genero_busqueda.lower()]
        
        if libros_encontrados:
            print(f'Libros encontrados en el género "{genero_busqueda}":')
            for libro in libros_encontrados:
                print(f'- {libro.titulo} por {libro.autor} (Puntuación: {libro.puntuacion})')
        else:
            print(f'No se encontraron libros en el género "{genero_busqueda}".')
    
    elif opcion == '3':
        genero_recomendacion = input('\n Ingrese el género de libro para recibir una recomendación: ')
        libros_encontrados = [libro for libro in lista_libros if libro.genero.lower() == genero_recomendacion.lower()]
        
        if libros_encontrados:
            libro_recomendado = max(libros_encontrados, key=lambda libro: libro.puntuacion)
            print(f'Recomendación de libro en el género "{genero_recomendacion}":')
            print(f'- {libro_recomendado.titulo} por {libro_recomendado.autor} (Puntuación: {libro_recomendado.puntuacion})')
        else:
            print(f'No se encontraron libros en el género "{genero_recomendacion}".')
            
    elif opcion == '4':
        print('\n Gracias por visitar la librería virtual. ¡Hasta luego!')
        break
    
    else:
        print('\n Opción inválida. Por favor, ingrese un número del 1 al 4.')
        

