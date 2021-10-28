def negativos(lista):
    listaNueva = []

    for i in lista:
        if i < 0:
            listaNueva.append(i)
    
    return listaNueva

def main():
    lista = [-3,-1,0,5,4,-15]

    print("La lista sin los números negativos es", negativos(lista))

main()
