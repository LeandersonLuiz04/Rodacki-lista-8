def descompacta(lista):
    if not lista:
        return []
    valor = lista[0]
    contagem = lista[1]
    return [valor] * contagem + descompacta(lista[2:])

def main():
    
    lista_codificada = ["A", 12, "B", 4, "A", 6, "B", 1]
    print("Lista codificada:", lista_codificada)
    
    lista_descompactada = descompacta(lista_codificada)
    print("Lista descompactada:", lista_descompactada)

if __name__ == "__main__":
    main()
