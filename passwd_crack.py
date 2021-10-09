import hashlib


def main():
    frase = input('Informe a frase/palavra a ser criptografada: ')
    frase_encoded = frase.encode()
    resultado = hashlib.md5(frase_encoded)
    print(f'Palavra Original: {frase}')
    print(f'Palavra Criptografada: {resultado}')
    print(f'Equivalente em hexadecimal {resultado.hexdigest()}')


if __name__ == '__main__':
    main()
