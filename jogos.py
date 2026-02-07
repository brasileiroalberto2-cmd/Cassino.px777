"""
Cassino PX777 - Jogos de Cassino
Sistema de jogos de cassino com diversos jogos populares
"""

import random
import time


class Jogos:
    """Classe principal para gerenciar jogos de cassino"""
    
    def __init__(self, saldo_inicial=1000):
        self.saldo = saldo_inicial
        self.historico = []
    
    def adicionar_historico(self, jogo, aposta, resultado, ganho):
        """Adiciona uma jogada ao histórico"""
        self.historico.append({
            'jogo': jogo,
            'aposta': aposta,
            'resultado': resultado,
            'ganho': ganho,
            'saldo': self.saldo
        })
    
    def exibir_saldo(self):
        """Exibe o saldo atual"""
        print(f"\n💰 Saldo atual: R$ {self.saldo:.2f}")
        return self.saldo
    
    def exibir_historico(self):
        """Exibe o histórico de jogadas"""
        if not self.historico:
            print("\n📋 Nenhuma jogada registrada ainda.")
            return
        
        print("\n📋 Histórico de Jogadas:")
        print("-" * 80)
        for i, jogada in enumerate(self.historico[-10:], 1):
            resultado_emoji = "✅" if jogada['ganho'] > 0 else "❌"
            print(f"{resultado_emoji} {jogada['jogo']}: Aposta R$ {jogada['aposta']:.2f} | "
                  f"Resultado: {jogada['resultado']} | Ganho: R$ {jogada['ganho']:.2f} | "
                  f"Saldo: R$ {jogada['saldo']:.2f}")


class Roleta(Jogos):
    """Jogo de Roleta"""
    
    NUMEROS = list(range(0, 37))  # 0 a 36
    VERMELHOS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    PRETOS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    
    def jogar(self, aposta, tipo_aposta, valor_aposta):
        """
        Joga roleta
        tipo_aposta: 'numero' (paga 35:1), 'cor' (paga 2:1), 'par_impar' (paga 2:1)
        valor_aposta: número específico, 'vermelho', 'preto', 'par', 'impar'
        """
        if aposta > self.saldo:
            print("❌ Saldo insuficiente!")
            return False
        
        numero_sorteado = random.choice(self.NUMEROS)
        cor = 'verde' if numero_sorteado == 0 else ('vermelho' if numero_sorteado in self.VERMELHOS else 'preto')
        paridade = 'par' if numero_sorteado % 2 == 0 else 'impar'
        
        print(f"\n🎰 Girando a roleta...")
        time.sleep(1)
        print(f"🎯 Número sorteado: {numero_sorteado} ({cor})")
        
        ganhou = False
        multiplicador = 0
        
        if tipo_aposta == 'numero' and valor_aposta == numero_sorteado:
            ganhou = True
            multiplicador = 35
        elif tipo_aposta == 'cor' and valor_aposta == cor:
            ganhou = True
            multiplicador = 2
        elif tipo_aposta == 'par_impar' and valor_aposta == paridade and numero_sorteado != 0:
            ganhou = True
            multiplicador = 2
        
        if ganhou:
            ganho = aposta * multiplicador
            self.saldo += ganho
            print(f"🎉 Parabéns! Você ganhou R$ {ganho:.2f}!")
            self.adicionar_historico('Roleta', aposta, f"{numero_sorteado} ({cor})", ganho)
        else:
            self.saldo -= aposta
            print(f"😔 Você perdeu R$ {aposta:.2f}")
            self.adicionar_historico('Roleta', aposta, f"{numero_sorteado} ({cor})", -aposta)
        
        self.exibir_saldo()
        return ganhou


class Blackjack(Jogos):
    """Jogo de Blackjack (21)"""
    
    CARTAS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    VALORES = {
        'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10, 'K': 10
    }
    
    def calcular_pontos(self, mao):
        """Calcula os pontos de uma mão"""
        pontos = sum(self.VALORES[carta] for carta in mao)
        # Ajusta valor do Ás se necessário
        ases = mao.count('A')
        while pontos > 21 and ases > 0:
            pontos -= 10
            ases -= 1
        return pontos
    
    def jogar(self, aposta):
        """Joga Blackjack"""
        if aposta > self.saldo:
            print("❌ Saldo insuficiente!")
            return False
        
        # Distribuir cartas iniciais
        mao_jogador = [random.choice(self.CARTAS), random.choice(self.CARTAS)]
        mao_dealer = [random.choice(self.CARTAS), random.choice(self.CARTAS)]
        
        print(f"\n🃏 Suas cartas: {mao_jogador} = {self.calcular_pontos(mao_jogador)} pontos")
        print(f"🎴 Carta visível do dealer: {mao_dealer[0]}")
        
        # Jogador joga
        while self.calcular_pontos(mao_jogador) < 21:
            acao = input("\nDeseja (c)omprar carta ou (p)arar? ").lower()
            if acao == 'c':
                nova_carta = random.choice(self.CARTAS)
                mao_jogador.append(nova_carta)
                print(f"🃏 Nova carta: {nova_carta}")
                print(f"🃏 Suas cartas: {mao_jogador} = {self.calcular_pontos(mao_jogador)} pontos")
            else:
                break
        
        pontos_jogador = self.calcular_pontos(mao_jogador)
        
        if pontos_jogador > 21:
            print(f"💥 Você estourou com {pontos_jogador} pontos!")
            self.saldo -= aposta
            self.adicionar_historico('Blackjack', aposta, f"Estourou ({pontos_jogador})", -aposta)
            self.exibir_saldo()
            return False
        
        # Dealer joga
        print(f"\n🎴 Cartas do dealer: {mao_dealer} = {self.calcular_pontos(mao_dealer)} pontos")
        while self.calcular_pontos(mao_dealer) < 17:
            nova_carta = random.choice(self.CARTAS)
            mao_dealer.append(nova_carta)
            print(f"🎴 Dealer compra: {nova_carta}")
            print(f"🎴 Cartas do dealer: {mao_dealer} = {self.calcular_pontos(mao_dealer)} pontos")
            time.sleep(0.5)
        
        pontos_dealer = self.calcular_pontos(mao_dealer)
        
        # Determinar vencedor
        if pontos_dealer > 21:
            print(f"🎉 Dealer estourou! Você ganhou R$ {aposta:.2f}!")
            self.saldo += aposta
            self.adicionar_historico('Blackjack', aposta, f"Vitória ({pontos_jogador} vs {pontos_dealer})", aposta)
            ganhou = True
        elif pontos_jogador > pontos_dealer:
            print(f"🎉 Você venceu com {pontos_jogador} pontos! Ganhou R$ {aposta:.2f}!")
            self.saldo += aposta
            self.adicionar_historico('Blackjack', aposta, f"Vitória ({pontos_jogador} vs {pontos_dealer})", aposta)
            ganhou = True
        elif pontos_jogador == pontos_dealer:
            print(f"🤝 Empate com {pontos_jogador} pontos!")
            self.adicionar_historico('Blackjack', aposta, f"Empate ({pontos_jogador})", 0)
            ganhou = None
        else:
            print(f"😔 Dealer venceu com {pontos_dealer} pontos. Você perdeu R$ {aposta:.2f}")
            self.saldo -= aposta
            self.adicionar_historico('Blackjack', aposta, f"Derrota ({pontos_jogador} vs {pontos_dealer})", -aposta)
            ganhou = False
        
        self.exibir_saldo()
        return ganhou


class SlotMachine(Jogos):
    """Jogo de Caça-níqueis"""
    
    SIMBOLOS = ['🍒', '🍋', '🍊', '🍇', '⭐', '💎', '7️⃣']
    VALORES = {
        '🍒': 2,
        '🍋': 3,
        '🍊': 4,
        '🍇': 5,
        '⭐': 10,
        '💎': 20,
        '7️⃣': 50
    }
    
    def jogar(self, aposta):
        """Joga caça-níqueis"""
        if aposta > self.saldo:
            print("❌ Saldo insuficiente!")
            return False
        
        print("\n🎰 Girando os rolos...")
        time.sleep(1)
        
        resultado = [random.choice(self.SIMBOLOS) for _ in range(3)]
        print(f"🎰 Resultado: {' | '.join(resultado)}")
        
        # Verifica se ganhou
        if resultado[0] == resultado[1] == resultado[2]:
            simbolo = resultado[0]
            multiplicador = self.VALORES[simbolo]
            ganho = aposta * multiplicador
            self.saldo += ganho
            print(f"🎉 JACKPOT! Três {simbolo}! Você ganhou R$ {ganho:.2f}!")
            self.adicionar_historico('Slot Machine', aposta, f"{' | '.join(resultado)}", ganho)
            ganhou = True
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2]:
            ganho = aposta
            self.saldo += ganho
            print(f"✨ Dois símbolos iguais! Você ganhou R$ {ganho:.2f}!")
            self.adicionar_historico('Slot Machine', aposta, f"{' | '.join(resultado)}", ganho)
            ganhou = True
        else:
            self.saldo -= aposta
            print(f"😔 Você perdeu R$ {aposta:.2f}")
            self.adicionar_historico('Slot Machine', aposta, f"{' | '.join(resultado)}", -aposta)
            ganhou = False
        
        self.exibir_saldo()
        return ganhou


class Dados(Jogos):
    """Jogo de Dados (Craps simplificado)"""
    
    def jogar(self, aposta, palpite):
        """
        Joga dados
        palpite: número entre 2 e 12 (soma dos dois dados)
        """
        if aposta > self.saldo:
            print("❌ Saldo insuficiente!")
            return False
        
        if palpite < 2 or palpite > 12:
            print("❌ Palpite deve ser entre 2 e 12!")
            return False
        
        print("\n🎲 Jogando os dados...")
        time.sleep(1)
        
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        soma = dado1 + dado2
        
        print(f"🎲 Dados: {dado1} + {dado2} = {soma}")
        
        if soma == palpite:
            # Palpite exato paga 10:1
            ganho = aposta * 10
            self.saldo += ganho
            print(f"🎉 Acertou na mosca! Você ganhou R$ {ganho:.2f}!")
            self.adicionar_historico('Dados', aposta, f"Acertou ({soma})", ganho)
            ganhou = True
        elif abs(soma - palpite) == 1:
            # Palpite próximo paga 2:1
            ganho = aposta * 2
            self.saldo += ganho
            print(f"✨ Por pouco! Você ganhou R$ {ganho:.2f}!")
            self.adicionar_historico('Dados', aposta, f"Próximo ({soma})", ganho)
            ganhou = True
        else:
            self.saldo -= aposta
            print(f"😔 Você perdeu R$ {aposta:.2f}")
            self.adicionar_historico('Dados', aposta, f"Errou ({soma})", -aposta)
            ganhou = False
        
        self.exibir_saldo()
        return ganhou


if __name__ == "__main__":
    print("🎰 Cassino PX777 - Jogos 🎰")
    print("Este é o módulo de jogos. Execute main.py para jogar!")
