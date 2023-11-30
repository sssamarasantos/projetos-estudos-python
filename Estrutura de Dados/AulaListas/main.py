# Listas

frutas = ['maçã', 'banana', 'laranja', 'melancia']
doces = ['chocolate', 'doce de leite', 'leite condensado']

print('listas - index \n')
print(frutas[0]) #maça
print(frutas[-2]) #laranja
print('--------------------------------------')

# Funções

print('funções - index \n')
frutas.append('uva') #['maçã', 'banana', 'laranja', 'melancia', 'uva']
print(frutas)
frutas.remove('melancia') #['maçã', 'banana', 'laranja', 'uva']
print(frutas)

frutas.sort()
print(frutas) #['banana', 'laranja', 'maçã', 'uva']
print('--------------------------------------')
# Concatenar listas

print('listas - concatenar \n')
tresVezesFrutas = frutas * 3
print(tresVezesFrutas) #['maçã', 'banana', 'laranja', 'melancia', 'maçã', 'banana', 'laranja', 'melancia', 'maçã', 'banana', 'laranja', 'melancia']

print(frutas + doces) #['maçã', 'banana', 'laranja', 'melancia', 'chocolate', 'doce de leite', 'leite condensado']

frutas.extend(doces) 
print(frutas) #['maçã', 'banana', 'laranja', 'melancia', 'chocolate', 'doce de leite', 'leite condensado']
print('--------------------------------------')

# Extrair variáveis

print('listas - extrair variáveis \n')
doce1, doce2, doce3 = doces
print(doce1 + ', ' + doce2 + ' e ' + doce3)

fruta1, fruta2, *outras  = frutas 
print(fruta1 + ', ' + fruta2) # maçã, melancia
print(outras) # ['banana', 'laranja']
print('--------------------------------------')

# List e Zip
print('listas - list e zip \n')
print(list('Samara')) #['S', 'a', 'm', 'a', 'r', 'a']

zip = zip(frutas, doces, strict=False)
print(list(zip)) #[('maçã', 'chocolate'), ('banana', 'doce de leite'), ('laranja', 'leite condensado')]