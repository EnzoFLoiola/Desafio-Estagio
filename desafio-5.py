palavra = input('Digite uma palavra: ')
inversa = ''

for i in range(len(palavra) - 1, -1, -1):  
    inversa += palavra[i]

print(f'palavra original: {palavra}\n palavra inversa: {inversa}')