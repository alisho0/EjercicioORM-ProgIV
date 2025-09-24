# main.py

from models import GestorInventario, Producto

def menu_principal():
    gestor = GestorInventario()
    print("--- Sistema de gestión de inventario interactivo ---")

    while True:
        print("\nOpciones:")
        print("1. Mostrar todos los productos")
        print("2. Buscar productos por nombre")
        print("3. Buscar producto por ID")
        print("4. Actualizar cantidad de un producto")
        print("5. Agregar un nuevo producto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("\n--- Listado de productos ---")
            productos = gestor.todos()
            if productos:
                for p in productos:
                    print(p)
            else:
                print("El inventario está vacío.")

        elif opcion == '2':
            nombre_a_buscar = input("Ingresa el nombre del producto a buscar: ")
            producto_encontrado = gestor.filtrar_por_nombre(nombre_a_buscar)
            if producto_encontrado:
                print(producto_encontrado)
            else:
                print(f"No se encontraron productos con el nombre '{nombre_a_buscar}'.")

        elif opcion == '3':
            try:
                id_a_buscar = input("Ingresa el ID del producto a buscar: ")
                producto_encontrado = gestor.obtener_por_id(id_a_buscar)
                if producto_encontrado:
                    print(producto_encontrado)
                else:
                    print(f"No se encontró ningún producto con el ID {id_a_buscar}.")
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == '4':
            try:
                id_a_actualizar = input("Ingresa el ID del producto a actualizar: ")
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                gestor.actualizar_cantidad(id_a_actualizar, nueva_cantidad)
            except ValueError:
                print("Error: El ID y la cantidad deben ser números enteros.")

        elif opcion == '5':
            try:
                nuevo_id = input("Ingresa el ID del nuevo producto: ")
                nuevo_nombre = input("Ingresa el nombre: ")
                nueva_cantidad = input("Ingresa la cantidad: ")
                nuevo_precio = input("Ingresa el precio: ")
                
                nuevo_producto = Producto(nuevo_id, nuevo_nombre, nueva_cantidad, nuevo_precio)
                gestor.guardar_producto(nuevo_producto)
            except ValueError:
                print("Error: El ID, cantidad y precio deben ser valores numéricos.")

        elif opcion == '6':
            print("Saliendo del sistema...")
            break 

        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")


if __name__ == "__main__":
    menu_principal()