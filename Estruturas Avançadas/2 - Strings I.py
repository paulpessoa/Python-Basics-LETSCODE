empresa = "Google"
print("aspas dupla: " + empresa)

empresa = 'Apple'
print("aspas simples: " + empresa)

empresa = "Let's Code"
print("aspas duplas fora e simples dentro: " + empresa)

frase = "A pessoa disse: \"hoje sextou\""
print("caracter de escape: " + frase)


empresa = "Google"
print(empresa [0])
print(empresa [:3])

nomes_cidades = "Quixada, Recife, Mossoró, Salvador, Florianópolis"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

cabecalho = "    MENU PRINCIPAL    "
print(cabecalho.strip())

nome_cidade = 'rIo DE jaNeirO'

print(nome_cidade.title())
print(nome_cidade.capitalize())
print(nome_cidade.lower())
print(nome_cidade.upper())


nome_cidade = input('Que cidade é conhecida como a cidade da Galinha Choca?')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'quixada':
    print('Tente novamente, vc sabe :)')
    nome_cidade = input('Que cidade é conhecida como a cidade da Galinha Choca?')
print('Aiii simmm, você é topzêra!')


mensagem = 'Voce viu o que Pietro falou?'
fui_citado = 'Pietro' in mensagem
print(fui_citado)