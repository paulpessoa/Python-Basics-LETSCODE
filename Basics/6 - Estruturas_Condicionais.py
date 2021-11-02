valor_passagem = 4.30

valor_corrida = input('Qual o valor da corrida?')

if float(valor_corrida) <= valor_passagem * 5:
  print('Pegar Corrida')
elif float(valor_corrida) <= valor_passagem * 6:
  print('Aguarde um momento, o valor pode diminuir')
else:
  print('Pegue o Onibus')
