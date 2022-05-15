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


#printa os primos assim que os encontra e não os guarda, sendo mais rápido
def printar_primos(quantidade):
    if quantidade >= 1:

        #recebimento de valor inicial para polpar tempo
        primos=1
        identador=3  #variavel que será verificado se é primo

        #mensagens para diferentes quantidades
        if quantidade==1:
            print("O primeiro número primo é: 2")
        else:
            print(f"Os {quantidade} primeiros primos são: 2",end=" ")
            
        #bloco para encontrar os 'n' primeiros primos
        while True:
            

            #laçao para verificar os primos
            for x in range(3,identador,2):      
                if(identador%x==0):  #verificacao se é um divisor
                    laco_concluido=False  #laço não concluido
                    break  #quebra de laço quando encontra o primeiro divisor

            #printa o número primo caso tenha concluido o laço
            else:
                print(f"{identador}",end="")
                primos+=1
                
                #bloco que verifica se ainda tem primos a serem encontrados
                if(primos ==quantidade):
                    break
                else:
                    #coloca ',' ao final da linha caso ainda tenha mais primos para serem encontrados
                    print(", ",end="")
            identador+=2  #incrementação de 2 em 2 para pular os pares

        
    else:
        print(f"Valor {quantidade} não é um valor válido!")





#função que retorna lista com os 'n' primeiros primos e os retorna
def retornar_primos(quantidade):
    
    if quantidade >= 1:        
        #recebimento de valor inicial para polpar tempo
        primos=[2]
        identador=3  #variavel que será verificado se é primo

        #bloco para encontrar os 'n' primeiros primos
        while len(primos)!=quantidade:                   
            for x in range(3,identador,2):      
                if(identador%x==0):  #verificacao se é um divisor
                    laco_concluido=False  #laço não concluido
                    break  #quebra de laço quando encontra o primeiro divisor
            else:
                primos.append(identador)
            identador+=2  #incrementação de 2 em 2 para pular os pares

        return primos
    else:
        print(f"Quantidade {quantidade} invalida!")
        return 0 #retorno para a funcao não dar erro

#função propria para printar os números primos, printa eles de forma rápida
printar_primos(quantidade)

print("\n")
print("_"*10)


#função propria para retornar uma lista com os 'n' primeiros primos, quando usado para printar acaba sendo mais lendo
primos=retornar_primos(quantidade)
print(f"Os numeros primos são:")
for numero in primos:
    print(f"{numero}",end=", ")
          
