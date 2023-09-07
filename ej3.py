# Diccionario de productos y precios
productos = {
    "manzana": 1.0,
    "plátano": 0.5,
    "naranja": 0.75,
    "pera": 1.2,
    "uva": 2.0
}

# Solicitar al usuario el nombre del producto y la cantidad
nombre_producto = input("Ingrese el nombre del producto: ").lower()
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

# Verificar si el producto está en el diccionario
if nombre_producto in productos:
    precio_unitario = productos[nombre_producto]
    total_pagar = precio_unitario * cantidad
    print(f"El total a pagar por {cantidad} {nombre_producto}(s) es: ${total_pagar:.2f}")
else:
    print("El producto no se encuentra disponible en el diccionario.")
