# calculadora que recebe dois valores e realiza a operação pedida

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
operacao = input('Digite qual operação deseja realizar: ')

if (operacao == '1'):
  soma = valor1 + valor2
  print(f'Resultado soma: {soma}')
elif(operacao == '2'):
  subtracao = valor1 - valor2
  print(f'Resultado subtração: {subtracao}')
elif(operacao == '3'):
  multiplicacao = valor1 * valor2
  print(f'Resultado multiplicação: {multiplicacao}')
elif(operacao == '4'):
  divisao = valor1 / valor2
  print(f'Resultado divisão: {divisao}')
else:
  print('Operação inválida')
