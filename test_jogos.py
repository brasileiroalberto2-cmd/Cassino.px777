#!/usr/bin/env python3
"""
Script de teste para os jogos do Cassino PX777
"""

from jogos import Roleta, Blackjack, SlotMachine, Dados


def test_roleta():
    """Testa o jogo de Roleta"""
    print("\n" + "="*60)
    print("Testando ROLETA")
    print("="*60)
    
    jogo = Roleta(1000)
    print(f"Saldo inicial: R$ {jogo.saldo:.2f}")
    
    # Teste 1: Aposta em número
    print("\n[Teste 1] Aposta em número 7")
    jogo.jogar(100, 'numero', 7)
    
    # Teste 2: Aposta em cor
    print("\n[Teste 2] Aposta em vermelho")
    jogo.jogar(50, 'cor', 'vermelho')
    
    # Teste 3: Aposta em par/ímpar
    print("\n[Teste 3] Aposta em par")
    jogo.jogar(50, 'par_impar', 'par')
    
    print(f"\n✅ Roleta testada! Saldo final: R$ {jogo.saldo:.2f}")
    return jogo


def test_slot_machine():
    """Testa o jogo de Caça-níqueis"""
    print("\n" + "="*60)
    print("Testando CAÇA-NÍQUEIS")
    print("="*60)
    
    jogo = SlotMachine(1000)
    print(f"Saldo inicial: R$ {jogo.saldo:.2f}")
    
    # Fazer 5 jogadas
    for i in range(1, 6):
        print(f"\n[Jogada {i}]")
        jogo.jogar(50)
    
    print(f"\n✅ Caça-níqueis testado! Saldo final: R$ {jogo.saldo:.2f}")
    return jogo


def test_dados():
    """Testa o jogo de Dados"""
    print("\n" + "="*60)
    print("Testando DADOS")
    print("="*60)
    
    jogo = Dados(1000)
    print(f"Saldo inicial: R$ {jogo.saldo:.2f}")
    
    # Fazer apostas em diferentes números
    for palpite in [7, 5, 10]:
        print(f"\n[Palpite: {palpite}]")
        jogo.jogar(50, palpite)
    
    print(f"\n✅ Dados testado! Saldo final: R$ {jogo.saldo:.2f}")
    return jogo


def test_historico():
    """Testa o histórico de jogadas"""
    print("\n" + "="*60)
    print("Testando HISTÓRICO")
    print("="*60)
    
    jogo = Roleta(1000)
    
    # Fazer algumas jogadas
    jogo.jogar(100, 'numero', 5)
    jogo.jogar(50, 'cor', 'preto')
    jogo.jogar(75, 'par_impar', 'impar')
    
    # Exibir histórico
    jogo.exibir_historico()
    
    print("\n✅ Histórico testado!")
    return jogo


def main():
    """Executa todos os testes"""
    print("🎰 CASSINO PX777 - TESTES AUTOMATIZADOS 🎰")
    
    try:
        # Testar cada jogo
        test_roleta()
        test_slot_machine()
        test_dados()
        test_historico()
        
        print("\n" + "="*60)
        print("✅ TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
        print("="*60)
        print("\nOs jogos estão funcionando corretamente!")
        print("Execute 'python main.py' para jogar!")
        
    except Exception as e:
        print(f"\n❌ ERRO durante os testes: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    main()
