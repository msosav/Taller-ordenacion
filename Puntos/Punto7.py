import timeit

def negativos(lista):
    listaNueva = []

    for i in lista:
        if i < 0:
            listaNueva.append(i)
    
    return listaNueva

def main():
    start = timeit.timeit()

    lista = [-3,-1,-15,-16,-17,-15]

    print("La lista sin los números negativos es", negativos(lista))

    print(start)


main()
