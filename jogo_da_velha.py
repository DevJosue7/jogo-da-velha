import os

class jogador:
    def jog1(self):
        while True:
            simb = input("Bem-vindo jogador 1! Escolha seu símbolo (X ou O): ")
            if simb in ['X', 'x', 'O', 'o']:
                break
            else:
                print("Escolha somente 'X' ou 'O'")

        print("Jogador escolheu:", simb.upper())

        if simb.lower() == 'o':
            simb2 = 'x'
        else:
            simb2 = 'O'

        return simb, simb2

    def pc(self, simb2):
        print("Computador é:", simb2.upper())

    def jog2(self, simb2):
        print("Jogador 2 é:", simb2.upper())

class jogo:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def clean(self):
        SO = os.name
        if SO == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def tabujogo(self):
        i = 1
        while i <= 9:
            print("[", self.tabuleiro[(i - 1) // 3][(i - 1) % 3], "]", end="")
            if i % 3 == 0:
                print()
            i += 1

    def celjog(self, simb):
        while True:
            espaco = input("Escolha um espaço vazio e insira o valor (1-9): ")
            if espaco.isdigit():
                espaco = int(espaco)
                if 1 <= espaco <= 9:
                    l = (espaco - 1) // 3
                    co = (espaco - 1) % 3
                    if self.tabuleiro[l][co] == ' ':
                        self.tabuleiro[l][co] = simb
                        if self.verificar_vitoria(simb):
                            self.tabujogo()
                            print(f"Jogador {simb} venceu!")
                            return
                        break
                    else:
                        print("Espaço já preenchido. Escolha outro.")
                else:
                    print("Escolha um valor entre 1 e 9.")
            else:
                print("Entrada inválida. Digite um número de 1 a 9.")

    def alPC(self, simb, simb2):
        jogatu = 1

        while True:
            if jogatu == 1:
                self.celjog(simb)
                self.tabujogo()
                if self.verificar_vitoria(simb):
                    print(f"Jogador {simb} venceu!")
                    break
            else:
                self.celjog(simb2)
                self.tabujogo()
                if self.verificar_vitoria(simb2):
                    print(f"Jogador {simb2} venceu!")
                    break
            jogatu = 3 - jogatu

    def verificar_vitoria(self, simb):
        for linha in self.tabuleiro:
            if all([marcacao == simb for marcacao in linha]):
                return True

        for coluna in range(3):
            if all([self.tabuleiro[linha][coluna] == simb for linha in range(3)]):
                return True

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == simb:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == simb:
            return True

        return False

    def tabumap(self):
        i = 1
        while i <= 9:
            print("[", i, "]", end="")
            if i % 3 == 0:
                print()
            i += 1

    def altern(self, simb, simb2):
        jogatu = 1

        while True:
            if jogatu == 1:
                print("")
                print("Vez de jogador um")
                print("")
                self.celjog(simb)
                self.tabujogo()
                if self.verificar_vitoria(simb):
                    print(f"Jogador 1 venceu!")
                    break
            else:
                print("")
                print("Vez de jogador dois")
                print("")
                self.celjog(simb2)
                self.tabujogo()
                if self.verificar_vitoria(simb2):
                    print(f"Jogador 2 venceu!")
                    break
            jogatu = 3 - jogatu

    def jogar(self):
        s = 1
        recomeco = 's'

        while recomeco == 's':
            m = jogo()
            m.clean()
            m.tabumap()
            print("Placar:", s)
            nj = int(input("Quantos jogadores? "))

            if nj == 1:
                n = jogador()
                simb, simb2 = n.jog1()
                n.pc(simb2)
                print("Que comecem os jogos!")
                m.tabujogo()
                while True:
                    m.alPC(simb, simb2)
                    if m.verificar_vitoria(simb) or m.verificar_vitoria(simb2):
                        break

            if nj == 2:
                n = jogador()
                print("Dois jogadores")
                simb, simb2 = n.jog1()
                n.jog2(simb2)
                
                m.tabujogo()
                while True:
                    m.altern(simb, simb2)
                    if m.verificar_vitoria(simb) or m.verificar_vitoria(simb2):
                        break

            recomeco = input("Deseja jogar novamente? S/N ").lower()
            if recomeco != 's':
                break

if __name__ == "__main__":
    jogo_da_velha = jogo()
    jogo_da_velha.jogar()
