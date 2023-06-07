import os
import sys
import csv
# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar la ruta al PYTHONPATH
sys.path.append(current_dir)

# Importar el módulo ControladorCarrito desde controller
from controller import ControladorCarrito

def mostrar_menu():
    print("1. Agregar producto")
    print("2. Eliminar producto por nombre")
    print("3. Mostrar todos los productos")
    print("0. Salir")

def agregar_producto(controlador):
    print("-------------------------------------------------------------------")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    controlador.agregar_producto(nombre, precio)
    print("Producto agregado con éxito.")

def eliminar_producto(controlador):
    print("-------------------------------------------------------------------")
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if controlador.eliminar_producto(nombre):
        print("Producto eliminado con éxito.")
    else:
        print("El producto no existe en el carrito.")

def guardar_datos(controlador):
    data = controlador.obtener_lista_productos()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data.csv')

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for product in data:
            writer.writerow([product.nombre, product.precio])

def main():
    controlador = ControladorCarrito()
    print("-------------------------------------------------------------------")
    print("Probando agregar productos")
    print("-------------------------------------------------------------------")
    nombre="Pantalon"
    precio=5000
    controlador.agregar_producto(nombre,precio)
    print("Producto agregado con éxito.")
    print("-------------------------------------------------------------------")
    nombre="Remera"
    precio=4500
    controlador.agregar_producto(nombre,precio)
    print("Producto agregado con éxito.")
    print("-------------------------------------------------------------------")
    nombre="Medias"
    precio=3000
    controlador.agregar_producto(nombre,precio)
    print("Producto agregado con éxito.")
    print("-------------------------------------------------------------------")
    print("-------------------------------------------------------------------")
    print("Mostrar productos")
    print("-------------------------------------------------------------------")
    controlador.mostrar_productos()
    print("-------------------------------------------------------------------")
    print("Probando Eliminar productos")
    print("-------------------------------------------------------------------")
    print("Eliminamos el pantalon de la lista de productos")
    nombre="Pantalon"
    if controlador.eliminar_producto(nombre):
        print("Producto eliminado con éxito.")
    else:
        print("El producto no existe en el carrito.")
    print("-------------------------------------------------------------------")
    print("Mostrar productos")
    print("-------------------------------------------------------------------")
    controlador.mostrar_productos()
    print("-------------------------------------------------------------------")
    print("Probando el bucle")
    print("-------------------------------------------------------------------")
    nombre="Gorra"
    precio=1500
    controlador.agregar_producto(nombre,precio)
    guardar_datos(controlador)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(controlador)
        elif opcion == "2":
            eliminar_producto(controlador)
        elif opcion == "3":
            controlador.mostrar_productos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
