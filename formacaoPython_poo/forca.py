from random import randrange


def imprime_mensagem_abertura():
    print('*********************************\n'
          f'{"Bem vindo ao jogo de Forca!":^34}\n'
          '*********************************')


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def pede_chute():
    return input(f'Digite uma letra: ').strip().upper()


def marca_chute_correto(palavras, chute, letras):
    index = 0
    for letra in palavras:
        if chute == letra:
            letras[index] = letra
        index += 1


def imprime_mensagem_ganhador():
    print('Você ganhou!')


def imprime_mensagem_perdedor():
    print('Você perdeu!')


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou = enforcou = False
    erros = 0

    while not acertou and not enforcou:

        chute = pede_chute()
        
        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor()


if __name__ == '__main__':
    jogar()
