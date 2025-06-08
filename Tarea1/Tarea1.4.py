def registrar_estudiantes():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        try:
            nota = float(input(f"Nota de {nombre}: "))
            estudiantes[nombre] = nota
        except ValueError:
            print("Por favor, ingresa una nota valida (numero).")
    return estudiantes

datos = registrar_estudiantes()
print("Datos guardados:")
print(datos)
