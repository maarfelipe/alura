print('*********************************\n'
      'Bem vindo ao jogo de Adivinhação!\n'
      '*********************************')

numero_secreto = 42

chute = int(input('Digite o seu número: '))

print(f'Você digitou {chute}')

if numero_secreto == chute:
    print('Você acertou!')
else:
    print('Você errou!')
