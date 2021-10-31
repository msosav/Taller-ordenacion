from random import randrange

def listas():
    #Creación lista A
    A = []
    for i in range(100):
        A.append(randrange(0,100))

    #Creación lista B
    B = []
    for i in range(60):
        B.append(randrange(0,60))

    def quick_sort(lista):
        izquierda = []
        derecha = []
        centro=[] 

        if len(lista) >1:
            pivote = lista[-1] #Se pone el ultimo elemento como pivote
            for i in lista:
                if i<pivote:
                    izquierda.append(i) #Si es menor se adiciona ala izq del piv
                elif i==pivote:
                        centro.append(i) #El pivote en el centro
                else:
                        derecha.append(i) #Si es mayor a la derecha del pivote
            return quick_sort(izquierda) + centro + quick_sort(derecha)
        else:
            return lista

    print('A =', quick_sort(A))
    print("")

    print('B =', quick_sort(B))
    print("")

    C = A+B
    print('C =', quick_sort(C))

    return quick_sort(C)

def main():
    listas()

main()
