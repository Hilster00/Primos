import os

#laco para tratamento de erro
while True:
    #trata valores válidos
    try:
        
        #recebimento e cast de valores
        quantidade=input("Digite a quantidade de números primos desejados:")
        quantidade=int(float(quantidade))

        #verificação se o valor corresponde a uma quantidade válida
        if quantidade >= 1:
            break
        else:
            print(f"Valor {quantidade} não está no intervalo valido")
    #bloco para valores não numericos
    except:
        os.system("cls")
        print(f"Valor {quantidade} não é um número valido")

#recebimento de valor inicial para polpar tempo
primos=[2]
identador=3  #variavel que será verificado se é primo

#bloco para encontrar os 'n' primeiros primos
while len(primos)!=quantidade:
    
    laco_concluido=True  #variavel para verificar se o laço foi concluido
    
    for x in range(3,identador):      
        if(identador%x==0):  #verificacao se é um divisor
            laco_concluido=False  #laço não concluido
            break  #quebra de laço quando encontra o primeiro divisor

    if(laco_concluido==True):
        primos.append(identador)
    identador+=2  #incrementação de 2 em 2 para pular os pares

#bloco que printa os primos na tela
os.system("cls")
print(f"Os {len(primos)} primeiros primos são:",end="")
for numero in primos:
    print(f"{numero}",end=", ")
    
    
