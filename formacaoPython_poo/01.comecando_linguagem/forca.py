
def jogar():
    print('*********************************\n'
        f'{"Bem vindo ao jogo de Forca!":^34}\n'
        '*********************************')

    palavra_secreta = 'banana'
    acertou = enforcou = False

    while not acertou and not enforcou:

        chute = input('Digite uma letra: ')

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra {letra} na posição {index}')
            index += 1

        print('Jogando ...')

    print('Fim do jogo!')

if (__name__ == '__main__'):
jogar()
