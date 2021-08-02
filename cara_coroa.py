import random

def coin_flip():
    """Retorna randomicamente 'cara' ou 'coroa'"""
    if random.randint(0,1) == 0:
        return "cara"
    else:
        return "coroa"

def unfair_coin_flip(prob):
    if random.random() < prob:
        return "cara"
    else:
        return "coroa"
    

tt_cara = 0
tt_coroa = 0

for trial in range(10_000):
    if unfair_coin_flip(.7) == "cara":
        tt_cara = tt_cara + 1
    else:
        tt_coroa = tt_coroa + 1

media = tt_cara / tt_coroa
print(f"A proporção de 'cara' a 'coroa' é {media:.2f}")
