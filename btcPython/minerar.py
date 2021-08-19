from hashlib import sha256
import time


def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()


def main():
    num_bloco = 15
    transacoes = """
        Lira->Alon->10
        Alon->Joao->5
        Joao->Amanda->11
    """
    qtd_zeros = 6
    hash_anterior = "abc"
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtd_zeros)
    print(resultado)
    print(f"Tempo gasto: {(time.time() - inicio):,.2f}")


def minerar(num_bloco, transacoes, hash_anterior, qtd_zeros):
    nounce = 0
    while True:
        texto = str(num_bloco)+transacoes+hash_anterior+str(nounce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith('0'*qtd_zeros):
            return nounce, meu_hash
        nounce = nounce + 1


if __name__ == '__main__':
    main()
