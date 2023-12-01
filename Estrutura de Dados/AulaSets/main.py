# Sets
# -Similar a listas
# -Evita itens duplicadas
# -Não utiliza index

letras = set({'a', 'b', 'c', 'd'})
numeros1 = set({1, 2, 3, 4, 5})
numeros2 = set({4, 5, 6, 7, 8})
numeros3 = {2, 4, 6, 8, 10}

# | -> union, une as listas e remove os repetidos
# - -> difference, mostra o que não se repete
# ^ -> symmetric difference, mostra os valores únicos e não repetidos
# & -> intersection ou and, mostra os valores que se repetem

print('sets - operadores')
print(letras)  #{'b', 'a', 'c', 'd'}
print(numeros1 | numeros2)  #{1, 2, 3, 4, 5, 6, 7, 8}
print(numeros1 - numeros3)  #{1, 3, 5}
print(numeros2 & numeros3)  #{8, 4, 6}
print(numeros1 ^ numeros2 ^ numeros3)  #{1, 3, 4, 7, 10}
print('-------------------------------------')

print('sets - funções')
print(numeros1.union(letras))  #{1, 2, 3, 4, 5, 'c', 'b', 'd', 'a'}
print(numeros1.union(numeros2))  #{1, 2, 3, 4, 5, 6, 7, 8}
print(numeros1.difference(numeros3))  #{1, 3, 5}
print(numeros2.intersection(numeros3))  #{8, 4, 6}
print(numeros1.symmetric_difference(numeros2).symmetric_difference(
    numeros3))  #{1, 3, 4, 7, 10}
print('-------------------------------------')

print('sets - strings')
letras.add('e')
print(letras)  #{'d', 'c', 'b', 'e', 'a'}
letras.update(['f', 'g', 'h'])
print(letras)  #{'d', 'h', 'c', 'b', 'f', 'g', 'e', 'a'}
