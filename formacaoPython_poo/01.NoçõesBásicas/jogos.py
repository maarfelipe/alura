import forca
import adivinhacao


def escolhe_jogo():
    print('*********************************\n'
          f'{"Escolha o seu jogo!":^34}\n'
          '*********************************')

    jogo = int(input('[1] Forca\n'
                     '[2] Adivinhacao\n'
                     'Digite o código do jogo: '))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()
    elif jogo == 2:
        print('Jogando Adivinhacao')
        adivinhacao.jogar()


if __name__ == '__main__':
    escolhe_jogo()
