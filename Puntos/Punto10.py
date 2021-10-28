def busquedaSecuencial(unaLista, item):
    pos = 0
    encontrado = "no está"
    for i in range(len(unaLista)):
        while pos < len(unaLista[i]):
            if unaLista[i][pos] == item:
                encontrado = "si está"
                break
            else:
                pos = pos + 1
        pos  = 0
    return encontrado 

def main():
    listaPrueba = [[1,2,2,2,3,4], [1,2,3,3,4,5], [3,4,4,4,4,6], [4,5,6,7,8,9]]

    print("El número 0", busquedaSecuencial(listaPrueba, 0))
    print("El número 4", busquedaSecuencial(listaPrueba, 4))

main()
