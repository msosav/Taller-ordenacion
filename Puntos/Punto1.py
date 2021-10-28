def duplicados(lista):
    for i in range(len(lista)-1):
        pos = i+1
        while pos < len(lista):
            if lista[i] == lista[pos]:
                del lista[pos]                        
            pos = pos+1
    return lista

def main():
    lista = [4,7,11,4,9,5,11,7,3,5,4]
    print(duplicados(lista))

main()
