class VistaCarrito:
    def mostrar_total(self, total):
        print(f"Total: {total}")
    
    def mostrar_producto_agregado(self, producto):
        mensaje = f"Producto agregado: {producto.nombre} (${producto.precio})\n"
        print(mensaje)
        


    def mostrar_producto_eliminado(self, producto):
        mensaje = f"Producto eliminado: {producto.nombre} (${producto.precio})"
        print(mensaje)




    def mostrar_productos(self, productos):
        print("Lista de productos:")
        for producto in productos:
            mensaje = f"- {producto.nombre} (${producto.precio})"
            print(mensaje)

