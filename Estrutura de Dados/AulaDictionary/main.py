# Dicionários
#   - utiliza index no formato keys e values
#   - aceita todos os tipos de dados

aluno = {'nome': 'Samara', 'idade': 22, 'aprovado': True}

print('dicionários')
print(aluno)  #{'nome': 'Samara', 'idade': 22, 'aprovado': True}
print(aluno['nome'])  #Samara
print('-------------------------------------')

print('manipulação')
aluno['nome'] = 'Samara Santos'
print(aluno['nome'])  #Samara Santos

aluno.update({'endereço': 'Rua Santo Antônio de Pádua', 'numero': '362'})
print(
    aluno
)  #{'nome': 'Samara Santos', 'idade': 22, 'aprovado': True, 'endereço': 'Rua Santo Antônio de Pádua', 'numero': '362'}

print(aluno.get('endereço'))  #Rua Santo Antônio de Pádua
print(aluno.get('telefone'))  #None
print(aluno.get('telefone', 'Não existe'))  #Não existe

del aluno['endereço']
del aluno['numero']
print(
    aluno
)  #{'nome': 'Samara Santos', 'idade': 22, 'aprovado': True}

print(len(aluno)) #4
print('-------------------------------------')

print('looping')
for x in aluno: # igual a aluno.keys()
  print('key: ', x)
# print das keys
print('*******************************')
for x in aluno.values():
  print('value: ', x)
# print das values
print('*******************************')
for x in aluno.items():
  print(x)
# print das keys e values em tuples
print('*******************************')
for keys, values in aluno.items():
  print(f'{keys} : {values}')
# print das keys e values
print('-------------------------------------')

print('com listas')
aluno.update({'materias': ['Português', 'Matemática', 'Geografia']})
print(aluno) #{'nome': 'Samara Santos', 'idade': 22, 'aprovado': True, 'materias': ['Português', 'Matemática', 'Geografia']}
print(aluno.items()) #dict_items([('nome', 'Samara Santos'), ('idade', 22), ('aprovado', True), ('materias', ['Português', 'Matemática', 'Geografia'])])
print(aluno.keys()) #dict_keys(['nome', 'idade', 'aprovado', 'materias'])
print(aluno.values()) #dict_values(['Samara Santos', 22, True, ['Português', 'Matemática', 'Geografia']])
print('-------------------------------------')