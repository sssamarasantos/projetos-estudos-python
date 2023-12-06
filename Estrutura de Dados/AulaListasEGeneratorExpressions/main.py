# Lista e Generator Expression
  # - uma forma mais rápida para listas e relacionados
  # - menos memória alocada
  # - valores em bytes
  # - listas na casa do mi/bi +

from sys import getsizeof

numeros = [numero + 1 for numero in range(100000)]
# print(numeros)
print(type(numeros)) #<class 'list'>
print(getsizeof(numeros)) 
#920 bytes - com 100
#8856 bytes - com 1000
#85176 bytes - com 10000
#800984 bytes - com 100000

print("----------------")

numerosG = (numero + 1 for numero in range(100000))
# print(list(numeros))
print(type(numerosG)) #<class 'generator'>
print(getsizeof(numerosG)) 
#104 bytes - com 100
#104 bytes - com 1000
#104 bytes - com 10000
#104 bytes - com 100000