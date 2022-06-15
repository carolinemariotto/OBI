#Exercício com MATRIZ -> XADREZ <- OBI 2018

linhas = int(input())
colunas = int(input())

#se linhas e colunas são pares
if (linhas %2 == 0) and (colunas %2 == 0):
    print("1") #imprimi 1= BRANCO

#e se linhas e colunas são impares 
elif (linhas %2 != 0) and (colunas %2 != 0):
    print("1") #imprimi 1 => BRANCO
    
else:
    print("0")