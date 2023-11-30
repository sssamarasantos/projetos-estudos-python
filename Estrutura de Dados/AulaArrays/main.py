# Arrays
# -Usar para listas grandes (casa de mil itens)

from array import array  # importar biblioteca

letras = array('u', ['a', 'b', 'c'])
numeros_i = array('i', [1, 2, 3, 4])
numero_f = array('f', [2.5, 3.2, 8.7])

numero_f.append(1.0)
print(letras) #array('u', 'abc')
print(numeros_i) #array('i', [1, 2, 3, 4])
print(numero_f) #array('f', [2.5, 3.200000047683716, 8.699999809265137, 1.0])

letras.append('d')
print(letras) #array('u', 'abcd')