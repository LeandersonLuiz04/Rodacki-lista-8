def mdc(a,b):
    if b==0:
        return a
    else:
        c=a%b
        return mdc(b,c)
def main():
    escolha1=input("Primeiro valor: ")
    escolha2=input("Segundo valor: ")
    if escolha1=='' or escolha2=='':
        print('ERRO')
    else:
        valor1=int(escolha1)
        valor2=int(escolha2)
        print(mdc(valor1,valor2))
if __name__=="__main__":
    main()