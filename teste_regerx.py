import re

dado = input("Informe o dados a ser validado:\t")
exp = input("informe a expressão regular: \t")

print(dado)
print(exp)

resultado = re.match(exp, dado)

print(resultado)
