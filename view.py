class VistaCarrito:
    def mostrar_total(self, total):
        print(f"Total: {total}")
    
    def mostrar_producto_agregado(self, producto):
        print(f"Producto agregado: {producto.nombre} - {producto.precio}")

    def mostrar_producto_eliminado(self, producto):
        print(f"Producto eliminado: {producto.nombre} - {producto.precio}")

    def mostrar_productos(self, productos):
        print("-------------------------------------------------------------------")
        if productos:
            print("Productos en el carrito:")
            for producto in productos:
                print(f"- {producto.nombre} - {producto.precio}")
        else:
            print("No hay productos en el carrito.")
