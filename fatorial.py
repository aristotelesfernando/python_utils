number = int(input("Informe um número inteiro e positivo maior que zero: "))
if (number <= 0):
    print("O número deve ser maior que zero")
else:
    for n in range(1, (number+1)):
        res = number % n
        if res == 0:
            print(f"{n} é fatorial de {number}")
            
