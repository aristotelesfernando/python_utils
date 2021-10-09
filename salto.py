limit = 1500
salto = 30
c = 0
x = 1

while salto < limit:
    if salto > 1000:
        c = c + 1
    salto = salto  + x
    x = x + 1

print(c)
