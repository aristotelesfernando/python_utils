def divide(n1, n2):
    try:
        print(n1/n2)
    except TypeError:
        print("Ambos argumentos precisam ser números")
    except ZeroDivisionError:
        print("o segundo argumentos precisam ser maior que zero")


try:
    a = int(input("Primeiro numero:"))
    b = int(input("Segundo numero:"))
    divide(a,b)
except ValueError:
    print("Um ou ambos valores não são inteiros validos...")
except:
    print("Ocorreu um erro desconhecido")
