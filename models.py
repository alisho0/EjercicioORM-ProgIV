class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class GestorInventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
    
    def leer_inventario(self):
        try:
            with open(self.archivo, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def escribir_inventario(self, lineas):
        with open(self.archivo, 'w') as f:
            f.write(lineas)
    
    def todos(self):
        productos = []
        for linea in self.leer_inventario():
            try:
                id, nombre, cantidad, precio = linea.strip().split(',')
                productos.append(Producto(id, nombre, cantidad, precio))
            except ValueError:
                print(f'El doc no tiene la estructura pedida')
        return productos
    
    def filtrar_por_nombre(self, nombre):
        for linea in self.leer_inventario():
            if linea.strip().split(',')[1] == nombre:
                linea_array = linea.strip().split(',')
                linea_resultado = f"ID: {linea_array[0]} | Nombre: {linea_array[1]} | Cantidad: {linea_array[2]} | Precio: ${linea_array[3]}"
                return linea_resultado
        return 'No se encontró el producto'

    def obtener_por_id(self, id):
        for linea in self.leer_inventario():
            if linea.strip().split(',')[0] == id:
                linea_array = linea.strip().split(',')
                linea_resultado = f"ID: {linea_array[0]} | Nombre: {linea_array[1]} | Cantidad: {linea_array[2]} | Precio: ${linea_array[3]}"
                return linea_resultado
        return 'No se encontró el producto'
    
    def actualizar_cantidad(self, id, nueva_cantidad):
        lineas = self.leer_inventario()
        for linea in lineas:
            if linea.strip().split(',')[0] == id:
                partes = linea.strip().split(',')
                partes[2] = str(nueva_cantidad)
                nueva_linea = ','.join(partes) + '\n'
                lineas[lineas.index(linea)] = nueva_linea
                self.escribir_inventario(''.join(lineas))
                print(f'Cantidad del producto con ID {id} actualizada a {nueva_cantidad}')
                return
        print('No se encontró el producto para actualizar')
    
    def guardar_producto(self, producto):
        try:
            nuevaLinea = producto.id + "," + producto.nombre + "," + producto.cantidad + "," + producto.precio + "\n"
            for linea in self.leer_inventario():
                if linea.strip().split(',')[0] == producto.id:
                    return "El producto ya existe"
            nuevo_inventario = self.leer_inventario()
            nuevo_inventario.append(nuevaLinea)
            # print(''.join(nuevo_inventario))
            self.escribir_inventario(''.join(nuevo_inventario))
            return "Producto guardado correctamente"
        except ValueError:
            return "No se pudo escribir"