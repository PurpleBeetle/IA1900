def sumar_ventas_por_producto(ventas):
    resumen = {}
    productos = ventas['Producto']
    cantidades = ventas['Cantidad']

    for i in range(len(productos)):
        producto = productos[i]
        cantidad = cantidades[i]
        if producto in resumen:
            resumen[producto] += cantidad
        else:
            resumen[producto] = cantidad
    return resumen


ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

resultado = sumar_ventas_por_producto(ventas)
print("Ventas totales por producto:")
print(resultado)
