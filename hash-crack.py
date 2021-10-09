import hashlib

pass_found = 0


def main():

    input_hash = input("Entre com a senha hasheada: ")
    pass_doc = input('Informe o caminho completo do arquivo de dicionario de senhas: ')

    try:
        pass_file = open(pass_doc, 'r')
    except:
        print('Erro!')
        print(f'O arquivo {pass_doc} não foi localizado no sistema de arquivos')
        quit()

    for word in pass_file:
        enc_word = word.encode('utf-8')
        hash_word = hashlib.md5(enc_word.strip())
        digest = hash_word.hexdigest()

        if digest == input_hash:
            print(f'Senha encontrada\nA senha é {word}')
            pass_found = 1
            break


if not pass_found:
    print(f'A senha não foi localizada no arquivo de dicionario informado')

if __name__ == '__main__':
    main()
