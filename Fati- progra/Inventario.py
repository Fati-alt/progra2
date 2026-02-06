class Producto():
    def __init__(self,nombre,precio_base,stock):
       self.nombre=nombre
       self.precio_base=precio_base
       self.stock=stock

    def aplicar_descuento(self,porcentaje):
        self.precio_base*=(1-porcentaje)
        print(f"El nuevo precio del producto {self.nombre} es {self.precio_base}")
     
    
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("No hay suficiente en stock")
        else:
           self.stock+=cantidad
           print(f"El nuevo stock de {self.nombre} es {self.stock}")

class Categoria():
    def __init__(self,nomb):
        self.nombre_cat=nomb
        self.lista=[]

    def agregar_producto(self,producto):
       self.lista.append(producto)
       print(f"El producto {producto.nombre} se agregó a la lista")

    def valor_total_categoria(self):
        suma=0
        for m in self.lista:
            suma+=m.precio_base*m.stock
        print(f"El precio total de la categoria {self.nombre_cat} es {suma} pesos")

class Pedido():
    def __init__(self,cliente,productos_comprados):
        self.cliente=cliente
        self.productos_comprados=productos_comprados
    def calcular_total():
        ()
        print(f"El precio de los productos elegidos mas el impuesto es{}")
