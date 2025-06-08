def eliminar_duplicados_ordenar(lista):
    lista_sin_duplicados = list(set(lista))
    lista_sin_duplicados.sort()
    return lista_sin_duplicados

entrada = [4, 2, 7, 4, 2, 1, 9, 7]
resultado = eliminar_duplicados_ordenar(entrada)
print("Lista sin duplicados y ordenada:", resultado)
