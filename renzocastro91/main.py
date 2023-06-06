from  renzocastro91.controller import ControladorCarrito

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



def main():
    controlador = ControladorCarrito()

    while True:
        print("-------------------------------------------------------------------")
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
