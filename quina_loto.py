import random

numeros_in = [31, 18, 8, 52, 33, 39, 26, 58, 13, 38, 32, 57, 25, 80,
              81, 88, 98, 83, 93, 75, 78, 89, 86, 85, 65, 58, 66, 62, 69, 99]
print(f'Numeros encontradops para combinacao: {len(numeros_in)}')
quinas = list()
quina_uni = list()

i = 1

while i <= len(numeros_in):
    num_random = random.choice(numeros_in)
    if num_random not in quina_uni and num_random < 61:
        quina_uni.append(num_random)
        #print(f'adicionando {num_random}')
        #print(f'tamanho da quina é {len(quina_uni)}')
        if len(quina_uni) == 6:
            print('---------------')
            print(quina_uni)
            quinas.append(list(quina_uni))
            quina_uni.clear()
        i = i + 1

print(quinas)
