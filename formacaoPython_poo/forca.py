def jogar():
    print('*********************************\n'
          f'{"Bem vindo ao jogo de Forca!":^34}\n'
          '*********************************')

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = enforcou = False
    erros = 0

    while not acertou and not enforcou:

        chute = input(f'Digite uma letra: {letras_acertadas}').strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

    print('Fim do jogo!')


if __name__ == '__main__':
    jogar()
