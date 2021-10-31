def duplicadosOrdenado(lista):
    for i in range(len(lista)-2):
        if(i==len(lista)):
            break
        if(lista[i]==lista[i+1] or lista[i]==lista[i-1]):
            del lista[i]

    return lista

def main():
    lista = [1,2,3,3,3,4,5,6,6,7,7]
    print(duplicadosOrdenado(lista))

main()
