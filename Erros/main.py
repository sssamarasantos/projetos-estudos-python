# Erro
  # - excelente para testes
  # - o tipo do except sempre tem que ser o esperado (IndexError, KeyError, TypeError, ValueError, NameError, SyntaxError, IndentationError,)
  # try - código que pode gerar erro
  # except - exceção caso o erro aconteça
  # else - sempre que o try não gerar erro
  # finally - mesmo que o try ou o except gerar erro, o finally é executado

try:
  lista = [1, 2, 3]
  print(lista[4])
except IndexError:
  print('Index não encontrado')

print("----------------------------")

try:
  idade = int(input('Digite sua idade: '))
  print(idade)
except ValueError:
  print('Valor inválido')
else:
  print('Valor válido')
finally:
  print('Fim!!!')
