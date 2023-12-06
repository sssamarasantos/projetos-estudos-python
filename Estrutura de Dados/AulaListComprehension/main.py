# List Comprehension
  # - mais simples de escrever
  # - utilizado quando precisamos criar uma nova lista a partir de uma existente
  # - [expressao for item in lista]

frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia', 'melão']
#frutas2 = []

#for fruta in frutas:
#  if 'm' in fruta:
#    frutas2.append(fruta)

frutas2 = [fruta for fruta in frutas if 'm' in fruta]
print(frutas2) #['maçã', 'melancia', 'melão']
print("---------------------------------")

numeros = [1,2,3,3,4,5,6,7,8,9,10]
#numeros2 = []
#for numero in numeros:
#  numeros2.append(numero * 2)

numeros2 = [numero * 2 for numero in numeros]

print(numeros2) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]