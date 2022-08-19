from hashlib import sha256
import time


def ap_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest


def mine_bitcoin(num_bloco, tran, hash_ant, qtde_0):
    nonce = 0
    while True:
        texto = str(str(num_bloco) + tran + hash_ant + str(nonce))
        print(f'este é o texto bugado{texto}')
        meu_hash = ap_sha256(texto)
        if meu_hash.startswith():
            return nonce, meu_hash
        nonce += 1


if __name__ == "__main__":
    num_bloco = 15
    trans = """Alon->Rafael->10
                Rafael->Pedro->5
                Pedro->Alef->11"""
    quant_0 = 4
    hash_anterior = "abc"
    result = mine_bitcoin(num_bloco, trans, hash_anterior, quant_0)
    print(result)
