##exemplo 1
contador = 0

while contador < 10:
  contador += 1
  if contador == 1:
    print(contador, "item limpo")
  else:
    print(contador, "itens limpos")   

print ("fim da repeticao do bloco while")


##exemplo2
contador = 0

while True:
  if contador < 10:
    contador += 1
    if contador == 1:
      print(contador, "item limpo")
    else:
      print(contador, "itens limpos")
  else:
    break
print ("fim da repeticao do bloco while")


#exemplo3
texto = input('digite sua senha: ')
while texto != 'LetsCode':
  texto = input('Senha inválida, Tente novamente')

print('acesso permitido')



#exemplo
##exemplo 1
contador = 0

while contador < 10:
  contador += 1
  if contador == 1:
    continue
  print(contador, "itens limpos")   

print ("fim da repeticao do bloco while")
