import random, os

# inicialização do jogo
print('| PEDRA PAPEL TESOURA |')
escolhas = ['🗿', '📄', '✁']
maquina = random.choice(escolhas)
vitoria = {
    '🗿':'✁',
    '✁':'📄',
    '📄': '🗿'
}

# interação com o usuário
print('\nOpções')
print('1 - Pedra  🗿')
print('2 - Papel  📄')
print('3 - Tesoura ✁')
jogador = int(input('\nPedra, papel, tesoura...:  '))
jogador = escolhas[jogador - 1]

# limpa o terminal
os.system("cls")

# Embate
print(f'\n\n{jogador} vs {maquina}\n\n')
if jogador == maquina:
    print('Empate...')
elif vitoria[jogador] == maquina:
    print('Você venceu!')
else:
    print('Você perdeu.')

