import random
import time

class JogoPedraPapelTesoura:
    def __init__(self):
        #Inicialização
        self.escolhas = ['🗿', '📄', '✁']
        self.vitoria = {
            '🗿': '✁',
            '✁': '📄',
            '📄': '🗿'
        }

    def escolha_maquina(self):
        return random.choice(self.escolhas)

    def escolha_jogador(self):
        print('\nOpções:')
        print('1 - Pedra  🗿')
        print('2 - Papel  📄')
        print('3 - Tesoura ✁')
        while True:
            try:
                escolha = int(input('\nPedra, papel, tesoura...: '))
                if escolha not in [1, 2, 3]:
                    print("Por favor, escolha entre 1, 2 ou 3.")
                    continue
                return self.escolhas[escolha - 1]
            except ValueError:
                print("Entrada inválida. Digite um número entre 1 e 3.")

    def determinar_vencedor(self, jogador, maquina):
        if jogador == maquina:
            return "Empate..."
        elif self.vitoria[jogador] == maquina:
            return "Você venceu!"
        else:
            return "Você perdeu."

def cabecalho():
    print('| PEDRA PAPEL TESOURA |')

def embate(jogador, maquina, resultado):
    print(f'\n\n{jogador} vs {maquina}\n\n')
    print(resultado)

def jogar():
    jogo = JogoPedraPapelTesoura()
    
    # Mostra o cabeçalho
    cabecalho()
    
    # Obtém escolhas
    jogador = jogo.escolha_jogador()
    maquina = jogo.escolha_maquina()
    
    time.sleep(1)
    
    # Mostra o confronto e resultado
    resultado = jogo.determinar_vencedor(jogador, maquina)
    embate(jogador, maquina, resultado)

# Executa o jogo
if __name__ == "__main__":
    jogar()
