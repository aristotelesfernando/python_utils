import random

def roll():
    dice_face = random.randint(1,6)
    return dice_face

res = 0
nums = [0,0,0,0,0,0]

for i in range(1,10_001):
    face = roll()
    res = res + face
    if face == 1:
        nums[0] = nums[0] + 1
    elif face == 2:
        nums[1] = nums[1] + 1
    elif face == 3:
        nums[2] = nums[2] + 1
    elif face == 4:
        nums[3] = nums[3] + 1
    elif face == 5:
        nums[4] = nums[4] + 1
    else:
        nums[5] = nums[5] + 1
    
ratio = res / 10_000
print(f"Na média o número mais sorteado foi {ratio:.0f}")

for n in range(0,5):
    print(f"o número {n+1} foi sorteado {nums[n]} vezes.")
