import random

print('*********************************\n'
      'Bem vindo ao jogo de Adivinhação!\n'
      '*********************************')

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print('[1] Fácil\n'
      '[2] Médio\n'
      '[3] Difícil')
nivel = int(input('Digite o nível de dificuldade: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite um número entre 1 e 100: '))

    if chute < 1 or chute > 100:
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print(f'Acertou! Você fez {pontos} pontos!')
        break
    else:
        if maior:
            print('Errou! Seu chute foi maior que o número secreto.')
        elif menor:
            print('Errou! Seu chute foi menor que o número secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

print('Fim do jogo!')
