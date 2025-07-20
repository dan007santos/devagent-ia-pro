#!/usr/bin/env python3
"""
DevAgent IA Pro - Script de Teste
Testa todas as funcionalidades do sistema
"""

import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.tools import *

def teste_ferramentas():
    """Testa todas as ferramentas disponíveis"""
    print("🧪 TESTANDO FERRAMENTAS DO DEVAGENT IA PRO")
    print("=" * 50)
    
    # Teste Telegram
    print("\n🤖 Testando Telegram:")
    resultado = conectar_telegram("123456789:ABCDEF...")
    print(resultado)
    
    # Teste Binance
    print("\n📈 Testando Binance:")
    resultado = conectar_binance("test_api_key", "test_secret")
    print(resultado)
    
    # Teste geração de imagem
    print("\n🎨 Testando Geração de Imagem:")
    resultado = gerar_imagem("Um robô futurista programando")
    print(resultado)
    
    # Teste YouTube
    print("\n📺 Testando YouTube:")
    resultado = publicar_youtube(
        "DevAgent IA Pro - Demo", 
        "Demonstração do agente autônomo",
        "/path/to/video.mp4"
    )
    print(resultado)
    
    # Teste análise de mercado
    print("\n📊 Testando Análise de Mercado:")
    resultado = analisar_mercado("BTCUSDT", "1h")
    print(resultado)
    
    # Teste configurações
    print("\n⚙️ Testando Configurações:")
    config = {
        "nome": "DevAgent Config",
        "versao": "1.0",
        "funcionalidades": ["codigo", "telegram", "trading", "imagens"]
    }
    resultado = salvar_configuracao("teste", config)
    print(resultado)
    
    resultado = carregar_configuracao("teste")
    print(resultado)

def main():
    """Função principal"""
    print("🚀 INICIANDO TESTES DO DEVAGENT IA PRO")
    print("Data/Hora:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    try:
        teste_ferramentas()
        
        print("\n\n✅ TODOS OS TESTES CONCLUÍDOS!")
        print("Para usar o DevAgent, execute: streamlit run frontend/app.py")
        
    except Exception as e:
        print(f"\n❌ ERRO DURANTE OS TESTES: {str(e)}")

if __name__ == "__main__":
    main()
