def DecBinIterativo(q):
    result=''
    while q!=0:
        r=q%2
        result=str(r)+result
        q=q//2
    return result

def main():
    escolha=input("Número: ")
    if escolha=='':
        return
    else:
        valor=int(escolha)
        print(f"O NÚMERO {valor} EM BINÁRIO É: {DecBinIterativo(valor)}")
if __name__=="__main__":
    main()