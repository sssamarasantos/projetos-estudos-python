# Map function e Filter function
# - muito utlizado com listas
# - aplicar uma função a um Iterable
# list() - converter em lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#def somar(x):
#  return x + 2

print('map')
somar = lambda x: x + 2

print(list(map(somar, lista))) #[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista2 = [10, 25, 29, 30, 44]

#def maior_que_25(x):
#  return x > 25

maior_que_25 = lambda x: x > 25

print(list(map(maior_que_25, lista2))) #[False, False, True, True, True]
print('-------------------------------------')
print('filter')

print(list(filter(maior_que_25, lista2))) # [29, 30, 44]