def DecBinRecursivo(q):
    if q==0:
        return 0
    elif q==1:
        return 1
    else:
        return str(DecBinRecursivo(q//2))+str(q%2)
    
def main():
    escolha=input("Número: ")
    if escolha=='':
        return
    else:
        valor=int(escolha)
        if valor<0:
            print("VOCÊ DIGITOU UM NÚMERO MENOR QUE ZERO!")
        else:
            print(f"O NÚMERO {valor} EM BINÁRIO É: {DecBinRecursivo(valor)}")
if __name__=="__main__":
    main()