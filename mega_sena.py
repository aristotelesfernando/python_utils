import random

numeros_in = range(1, 61)
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
