print('*********************************\n'
      'Bem vindo ao jogo de Adivinhação!\n'
      '*********************************')

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print('Acertou!')
    else:
        if maior:
            print('Errou! Seu chute foi maior que o número secreto.')
        elif menor:
            print('Errou! Seu chute foi mnor que o número secreto.')

print('Fim do jogo!')
