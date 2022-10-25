def busqueda_binaria(lista, x):
    """Búsqueda binaria
    Precondición: lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """

    # Busca en toda la lista dividiéndola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.

    izq = 0 # izq guarda el índice inicio del segmento
    der = len(lista) -1 # der guarda el índice fin del segmento

    # un segmento es vacío cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = int((izq+der)/2)

        print ("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)

        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio

        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio-1

        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento

    # salió del ciclo de manera no exitosa: el valor no fue encontrado
    return -1
lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
busqueda_binaria(lista, 67)
