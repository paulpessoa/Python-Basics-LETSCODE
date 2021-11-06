from typing_extensions import Unpack


nomes_paises = ['brasil', 'acanada', 'china', 'argentina', 'japao']
print (nomes_paises)

print('tamanho da lista', len(nomes_paises))

print('Pais', nomes_paises[4])

print('pais', nomes_paises[-1])
nomes_paises[4] = 'Colombia'
print(nomes_paises)


listas_capitais = []

listas_capitais.append('Brasilia')
listas_capitais.append('Buenos Aires')
listas_capitais.append('Pequim')
listas_capitais.append('Bogotá')
print(listas_capitais)


listas_capitais.insert(2, 'Paris')
print(listas_capitais)

listas_capitais.remove('Buenos Aires')
print(listas_capitais)

removido = listas_capitais.pop(2)
print(listas_capitais, removido)







nomes_paises = ('brasil', 'argentina', 'canada', 'japao')
print(nomes_paises, type(nomes_paises))

nomes_paises = 'brasil', 'argentina', 'canada', 'japao'
print(nomes_paises, type(nomes_paises))


nome_estado = 'sao paulo',
print(nome_estado, type(nome_estado))


len(nomes_paises)

nomes_paises[0]

b, a, c, ca, j = nomes_paises

print(b, c, j)