class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None

    def registrar_producto(self, callback):
        self.precio_de_venta = callback(self.costo, self.margen_de_venta)
        producto_info = {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'costo': self.costo,
            'cantidad': self.cantidad,
            'precio_de_venta': self.precio_de_venta
        }
        # Guarda el producto y asumo el diccionario "productos"
        productos[self.id] = producto_info

    def imprimir_producto(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, "
              f"Descripción: {self.descripcion}, Costo: {self.costo}, "
              f"Cantidad: {self.cantidad}, Precio de Venta: {self.precio_de_venta}")

    @staticmethod
    def imprimir_listado_productos():
        for producto_id, producto_info in productos.items():
            print(f"ID: {producto_info['id']}, Nombre: {producto_info['nombre']}, "
                  f"Descripción: {producto_info['descripcion']}, Costo: {producto_info['costo']}, "
                  f"Cantidad: {producto_info['cantidad']}, Precio de Venta: {producto_info['precio_de_venta']}")

# Diccionario donde se guarda los productos
productos = {}

# Esto permite ingresar los productos
def ingresar_datos_producto():
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    costo = int(input("Ingrese el costo del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    margen_de_venta = int(input("Ingrese el margen de venta del producto (porcentaje): ")) / 100.0

    return id, nombre, descripcion, costo, cantidad, margen_de_venta

# el ciclo que me permite ingresar mas productos
while True:
    producto = Producto(*ingresar_datos_producto())
    producto.registrar_producto(lambda costo, margen_de_venta: costo / (1 - margen_de_venta))
    producto.imprimir_producto()

    continuar = input("¿Desea ingresar otro producto? (y/n): ")
    if continuar.lower() != 'y':
        break

# Imprimir todo al final
Producto.imprimir_listado_productos()
