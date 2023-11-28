# calculadora que recebe dois valores e realiza a operação pedida

operacoes = ['1 - Adição', 
   '2 - Subtração', 
   '3 - Multiplicação', 
   '4 - Divisão',
   '5 - Potência']
continua = True
resultado = 0
contador = 0
valor = 0

def adicao(valor1, valor2):
  return valor1 + valor2


def subtracao(valor1, valor2):
  return valor1 - valor2


def multiplicacao(valor1, valor2):
  return valor1 * valor2


def divisao(valor1, valor2):
  return valor1 / valor2


def potenciacao(valor1, valor2):
  return valor1 ** valor2

while(continua):
  operacao_valida = True
  
  if (contador == 0):
    valor = float(input('Digite o valor: '))
    resultado = valor
  
  for i in operacoes:
    print(i)
  operacao = float(input('Digite qual operação deseja realizar: '))

  contador =+ 1

  if (contador != 0):
    valor = float(input(' \nDigite o valor: '))

  match operacao:
    case 1:
      resultado = adicao(resultado, valor)
    case 2: 
      resultado = subtracao(resultado, valor)
    case 3:
      resultado = multiplicacao(resultado, valor)
    case 4: 
      resultado = divisao(resultado, valor)
    case 5:
      resultado = potenciacao(resultado, valor)
    case _:
      operacao_valida = False
      print('Operação inválida!\n')
  
  if (operacao_valida and contador != 0):
    print(f'\nResultado: {resultado}\n')