a = int(input())
b = int(input())
c = int(input())
caixa = [a, b, c]
caixa.sort()

h = int(input())
l = int(input())
janela = [h, l]
janela.sort()

if caixa[1] <= janela[1] and caixa[0] <= janela[0]:
    print("S")
else: 
    print("N")