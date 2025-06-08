def mostrar_tabla_multiplicar():
    numero = int(input("Ingrese un número: "))
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

mostrar_tabla_multiplicar()
