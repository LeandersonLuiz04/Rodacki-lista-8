def raizq(n,estimativa=1.0):
    if abs(estimativa**2-n)<=10**-12:
        return estimativa
    else:
        return raizq(n,(estimativa+n/estimativa)/2)
def main():
    escolha=input("VALOR: ")
    if escolha=="":
        return
    else:
        valor=float(escolha)
        print(f"Raiz de {valor}: {raizq(n=valor,estimativa=1.0)}")


if __name__=="__main__":
    main()
