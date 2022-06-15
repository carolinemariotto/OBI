nota1 ,nota2= input().split()
nota1 = float(nota1)
nota2 = float(nota2)


media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print ('Aprovado')
elif media < 7 and media >= 4:
    print ('Recuperacao')
else:
    print ('Reprovado')

