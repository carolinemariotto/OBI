repouso = int(input())
atual = int(input())
capacidade = int(input())

if atual > 3 * repouso or capacidade < 95:
    print("diminuir")
    
elif atual < 2 * repouso or capacidade > 97:
    print("aumentar")
    
else:
    print("manter")

