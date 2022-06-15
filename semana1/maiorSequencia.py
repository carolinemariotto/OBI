
s = input().split()
tamanho = []

i = 0
while(int(s[i])!= 0):
    tamanho.append(int(s[i]))
    i += 1
    
print(max(tamanho))