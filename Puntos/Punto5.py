def elecciones(lista):
    listaCandidatos = {}

    for elemento in lista:
        if elemento not in listaCandidatos:
            listaCandidatos[elemento] = 1
        else:
            listaCandidatos[elemento] += 1

    votos = listaCandidatos.values()

    for candidatos in listaCandidatos:
        if listaCandidatos[candidatos]==max(votos):
            ganador = candidatos
            break
    
    return ganador

def main():
    lista = [1234,1234,12345,12345,1234,122,1222]
    print("El ganador fue", elecciones(lista))

main()
