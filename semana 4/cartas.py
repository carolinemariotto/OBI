a = int(input())
b = int(input())
c = int(input())

carta4= [a,b,c]
carta4.sort()

if carta4[0] == carta4[1]:
    print(carta4[2])
    
else:
    print(carta4[0])
    