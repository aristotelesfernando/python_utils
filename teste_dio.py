i, im, f, fm = map(int, input().split())


i = i * 60 + im
f = f * 60 + fm


total = f - i if f > i else 24 * 60 + f - i


hours = total // 60
minutes = total % 60


print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
