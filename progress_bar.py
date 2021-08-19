from tqdm import tqdm

numeros = range(1000000000)

for i in tqdm(numeros, colour = 'red', desc = 'Processando'):
    pass
