
m = int(input())
f1 = int(input())
f2 = int(input())
f3 =  m - (f1 + f2)
maiorIdade = f1

if  f2 > maiorIdade :
    maiorIdade = f2
    
if  f3 > maiorIdade :
    maiorIdade = f3
else:   
    print(maiorIdade)