# Função Lambda
  # - é uma função (pequena) sem nome
  # - pode ter vários argumentos mas somente uma expressão
  # - muito utilizada dentro de outras funções
  # - código mais limpo
  # - pode ser atribuido a uma variável

somar = lambda v1, v2: v1 + v2
print(somar(10, 10)) #20

def multiplicar_metade(v1, v2):
  sub = v1 - v2
  return sub * 2

print(multiplicar_metade(30, 15)) #30