# calculadora que recebe dois valores e realiza a operação pedida

operacoes = ['1 - Adição', 
             '2 - Subtração', 
             '3 - Multiplicação', 
             '4 - Divisão',
             '5 - Potência']
continua = True

print('Calculadora')
while(continua):
  valor1 = int(input('Digite o primeiro valor: '))
  valor2 = int(input('Digite o segundo valor: '))
  print('------------------------------------------------')
  print('Operações:')
  for i in operacoes:
    print(i)
  operacao = int(input('Digite qual operação deseja realizar: '))
  print('------------------------------------------------')
  resultado = 0
  operacao_valida = True
  
  match operacao:
    case 1:
      resultado = valor1 + valor2
    case 2: 
      resultado = valor1 - valor2
    case 3:
      resultado = valor1 * valor2
    case 4: 
      resultado = valor1 / valor2
    case 5:
      resultado = valor1 ** valor2
    case _:
      operacao_valida = False
      print('Operação inválida!\n')
  
  if (operacao_valida):
    print(f'Resultado: {resultado}\n')
  
  calcular_novamente = input('Calcular novamente? (s/n)\n')
  print('================================================')
  if (calcular_novamente == 's'):
    continua = True
  elif (calcular_novamente == 'n'):
    continua = False