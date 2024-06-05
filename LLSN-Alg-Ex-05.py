lista=[]    
def recursiva():    
    escolha=input("VALOR: ")
    
    if escolha=='':
        return 
    else:
        valor=int(escolha)
        lista.append(valor)
        return recursiva()
recursiva()
print(f"SOMA: {sum(lista)}")