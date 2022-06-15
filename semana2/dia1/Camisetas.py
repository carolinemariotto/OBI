
#entrada
total_de_camisas = int(input())
tamanhos = input().split(" ")
tamanhos = [int(i) for i in tamanhos]
camisas_p = int(input())
camisas_m = int(input())

#verificar se entradas estão corretas
if total_de_camisas != len(tamanhos):
  print("N")
elif total_de_camisas != (camisas_p + camisas_m):
  print("N")
elif len(tamanhos) != (camisas_p + camisas_m):
  print("N")
else:
  #entradas corretas aqui

  #checar a soma
  soma_p, soma_m = 0, 0
  for t in tamanhos:
    if t == 1:
      soma_p += 1
    elif t == 2:
      soma_m += 1

  if soma_p == camisas_p and soma_m == camisas_m:
    print("S")
  else:
    print("N")