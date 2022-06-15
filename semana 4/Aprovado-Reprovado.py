a, b = input().split()

a = float(a)
b = float(b)
notas = ((a + b)/2)

if (notas >= 7 ):
	print("Aprovado")
	
elif (notas < 7 and notas == 4 ):
	print("Recuperação")
	
else :
	print ("Reprovado")
	