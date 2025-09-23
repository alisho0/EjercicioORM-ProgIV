from models import GestorInventario, Producto

def probar_gestor():
    """Función que encapsula todas las pruebas del GestorInventario."""
    
    # 1. Crea una instancia del GestorInventario.
    gestor = GestorInventario()
    print("--- Sistema de gestión de inventario inicializado ---")

    # 2. Usa el método todos() para mostrar todos los productos.
    print("\n--- Listando todos los productos ---")
    productos = gestor.todos()
    for producto in productos:
        print(producto)

    # 3. Usa el método filtrar_por_nombre() para encontrar los "Teclados".
    print("\n--- Buscando productos por nombre: ---")
    nombre = gestor.filtrar_por_nombre("Laptop")
    print(nombre)

    # 4. Usa el método obtener_por_id() para encontrar un producto por su ID.
    print("\n--- Buscando producto por ID: ---")
    producto = gestor.obtener_por_id("3")
    print(producto)

    # 5. Actualiza la cantidad de un producto.
    print("\n--- Actualizando cantidad de producto ---")
    gestor.actualizar_cantidad("3", 15)

    # 6. Agrega un producto
    print("\n--- Agregar un producto ---")
    productoNuevo = Producto("4", "Monitor", "10", "200")
    gestor.guardar_producto(productoNuevo)
    # gestor.guardar_producto(producto)

# Este bloque se ejecuta solo cuando corres el script directamente
if __name__ == "__main__":
    probar_gestor()