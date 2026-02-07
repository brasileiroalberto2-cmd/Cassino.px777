#!/usr/bin/env python3
"""
Cassino PX777 - Sistema de Jogos
Main entry point para o cassino
"""

from jogos import Roleta, Blackjack, SlotMachine, Dados


def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*60)
    print("🎰 BEM-VINDO AO CASSINO PX777 🎰")
    print("="*60)
    print("\nEscolha um jogo:")
    print("1. 🎰 Roleta")
    print("2. 🃏 Blackjack (21)")
    print("3. 🎰 Caça-níqueis (Slot Machine)")
    print("4. 🎲 Dados")
    print("5. 📋 Ver Histórico")
    print("6. 💰 Ver Saldo")
    print("7. ❌ Sair")
    print("="*60)


def jogar_roleta(jogo):
    """Interface para jogar roleta"""
    print("\n🎰 ROLETA 🎰")
    print("Tipos de aposta:")
    print("1. Número específico (paga 35:1)")
    print("2. Cor (vermelho/preto) (paga 2:1)")
    print("3. Par/Ímpar (paga 2:1)")
    
    try:
        tipo = input("\nEscolha o tipo de aposta (1-3): ")
        aposta = float(input("Valor da aposta: R$ "))
        
        if tipo == '1':
            numero = int(input("Escolha um número (0-36): "))
            if 0 <= numero <= 36:
                jogo.jogar(aposta, 'numero', numero)
            else:
                print("❌ Número inválido!")
        elif tipo == '2':
            cor = input("Escolha a cor (vermelho/preto): ").lower()
            if cor in ['vermelho', 'preto']:
                jogo.jogar(aposta, 'cor', cor)
            else:
                print("❌ Cor inválida!")
        elif tipo == '3':
            paridade = input("Escolha (par/impar): ").lower()
            if paridade in ['par', 'impar']:
                jogo.jogar(aposta, 'par_impar', paridade)
            else:
                print("❌ Opção inválida!")
        else:
            print("❌ Tipo de aposta inválido!")
    except ValueError:
        print("❌ Valor inválido!")


def jogar_blackjack(jogo):
    """Interface para jogar blackjack"""
    print("\n🃏 BLACKJACK (21) 🃏")
    try:
        aposta = float(input("Valor da aposta: R$ "))
        jogo.jogar(aposta)
    except ValueError:
        print("❌ Valor inválido!")


def jogar_slot(jogo):
    """Interface para jogar caça-níqueis"""
    print("\n🎰 CAÇA-NÍQUEIS 🎰")
    print("Símbolos e multiplicadores:")
    print("🍒 = 2x | 🍋 = 3x | 🍊 = 4x | 🍇 = 5x")
    print("⭐ = 10x | 💎 = 20x | 7️⃣ = 50x")
    try:
        aposta = float(input("\nValor da aposta: R$ "))
        jogo.jogar(aposta)
    except ValueError:
        print("❌ Valor inválido!")


def jogar_dados(jogo):
    """Interface para jogar dados"""
    print("\n🎲 DADOS 🎲")
    print("Adivinhe a soma dos dois dados (2-12)")
    print("Acerto exato: paga 10:1")
    print("Diferença de 1: paga 2:1")
    try:
        aposta = float(input("\nValor da aposta: R$ "))
        palpite = int(input("Seu palpite (2-12): "))
        jogo.jogar(aposta, palpite)
    except ValueError:
        print("❌ Valor inválido!")


def main():
    """Função principal"""
    print("\n🎰 Cassino PX777 - Bet-px-777 🎰")
    
    try:
        saldo_inicial = float(input("Digite seu saldo inicial (padrão R$ 1000): ") or 1000)
    except ValueError:
        saldo_inicial = 1000
    
    # Criar instâncias dos jogos (todos compartilham o mesmo saldo)
    jogos_dict = {
        '1': Roleta(saldo_inicial),
        '2': Blackjack(saldo_inicial),
        '3': SlotMachine(saldo_inicial),
        '4': Dados(saldo_inicial)
    }
    
    # Sincronizar saldo entre todos os jogos
    jogo_atual = jogos_dict['1']
    
    while True:
        exibir_menu()
        escolha = input("\nSua escolha: ").strip()
        
        if escolha == '7':
            print("\n👋 Obrigado por jogar no Cassino PX777!")
            print(f"💰 Saldo final: R$ {jogo_atual.saldo:.2f}")
            if jogo_atual.saldo > saldo_inicial:
                lucro = jogo_atual.saldo - saldo_inicial
                print(f"🎉 Você saiu com lucro de R$ {lucro:.2f}!")
            elif jogo_atual.saldo < saldo_inicial:
                perda = saldo_inicial - jogo_atual.saldo
                print(f"😔 Você teve uma perda de R$ {perda:.2f}")
            else:
                print("🤝 Você saiu empatado!")
            break
        
        elif escolha == '5':
            jogo_atual.exibir_historico()
        
        elif escolha == '6':
            jogo_atual.exibir_saldo()
        
        elif escolha in jogos_dict:
            # Sincronizar saldo antes de jogar
            for jogo in jogos_dict.values():
                jogo.saldo = jogo_atual.saldo
                jogo.historico = jogo_atual.historico
            
            if escolha == '1':
                jogar_roleta(jogos_dict['1'])
            elif escolha == '2':
                jogar_blackjack(jogos_dict['2'])
            elif escolha == '3':
                jogar_slot(jogos_dict['3'])
            elif escolha == '4':
                jogar_dados(jogos_dict['4'])
            
            # Atualizar jogo atual para manter o saldo sincronizado
            jogo_atual = jogos_dict[escolha]
        
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        if jogo_atual.saldo <= 0:
            print("\n💸 Seu saldo acabou! Game Over!")
            print("Obrigado por jogar no Cassino PX777!")
            break


if __name__ == "__main__":
    main()
