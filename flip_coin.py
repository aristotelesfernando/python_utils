import random

def coin_flip():
    """0 - Cara / 1 - Coroa"""
    return random.randint(0,1)

cara_flip = 0
coroa_flip = 0

face = coin_flip()

for i in range(1,10_000):    
    c = 0
    while True:
        c = c + 1
        nface = coin_flip()
        if nface != face:
            if face == 0:
                cara_flip = cara_flip + c
            else:
                coroa_flip = coroa_flip + c
            face = nface
            break

media = (cara_flip + coroa_flip)/10_000

print(f"A média de vezes que a moeda demorou para virar a cada jogada foi {media}")

    
