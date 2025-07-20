from langchain.agents import initialize_agent
from langchain.chat_models import ChatReplicate
from langchain.tools import tool
import os
from .tools import conectar_telegram, conectar_binance, gerar_imagem, publicar_youtube

# Ferramenta de escrita de código
@tool
def escrever_codigo(prompt: str, linguagem: str = "Python", nivel: str = "Intermediário") -> str:
    """Escreve código com base no prompt, linguagem e nível especificados."""
    try:
        llm = ChatReplicate(
            model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
            replicate_api_token=os.getenv("REPLICATE_API_TOKEN")
        )
        
        prompt_completo = f"Gere código {linguagem} de nível {nivel} para: {prompt}. Responda apenas com o código, sem explicações."
        return llm.invoke(prompt_completo)
    except Exception as e:
        return f"Erro ao gerar código: {str(e)}"

@tool
def criar_bot_telegram(descricao: str) -> str:
    """Cria um bot do Telegram baseado na descrição."""
    codigo_bot = f"""
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Comando /start do bot'''
    keyboard = [
        [InlineKeyboardButton("🚀 Funcionalidade 1", callback_data='func1')],
        [InlineKeyboardButton("🔧 Funcionalidade 2", callback_data='func2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f'🤖 Bot criado para: {descricao}\\n\\nEscolha uma opção:',
        reply_markup=reply_markup
    )

def main():
    # Substitua YOUR_BOT_TOKEN pelo token do seu bot
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == '__main__':
    main()
"""
    return codigo_bot

@tool
def conectar_corretora(exchange: str, operacao: str) -> str:
    """Conecta com corretoras e executa operações."""
    if exchange.lower() == "binance":
        return conectar_binance("api_key", "secret_key") + f" - Operação: {operacao}"
    else:
        return f"Conexão com {exchange} - Operação: {operacao}"

@tool  
def gerar_imagem_ia(prompt: str, estilo: str = "realista") -> str:
    """Gera uma imagem usando IA."""
    return gerar_imagem(f"{prompt} - Estilo: {estilo}")

# Lista de ferramentas disponíveis
tools = [escrever_codigo, criar_bot_telegram, conectar_corretora, gerar_imagem_ia]

def criar_agente():
    """Cria e retorna um agente LangChain com todas as ferramentas."""
    try:
        llm = ChatReplicate(
            model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
            replicate_api_token=os.getenv("REPLICATE_API_TOKEN")
        )
        
        return initialize_agent(
            tools, 
            llm, 
            agent="zero-shot-react-description", 
            verbose=True,
            max_iterations=3
        )
    except Exception as e:
        print(f"Erro ao criar agente: {e}")
        return None

# Função principal para executar o agente
def executar_agente(prompt: str):
    """Executa o agente com um prompt específico."""
    agente = criar_agente()
    if agente:
        try:
            return agente.run(prompt)
        except Exception as e:
            return f"Erro na execução: {str(e)}"
    else:
        return "Erro: Não foi possível criar o agente."
