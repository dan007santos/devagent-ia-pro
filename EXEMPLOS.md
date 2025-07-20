# DevAgent IA Pro - Exemplos de Uso

Este arquivo contém exemplos práticos de como usar o DevAgent IA Pro.

## 🤖 Geração de Código

### Exemplo 1: Função Python
**Prompt:** "Crie uma função que calcule o factorial de um número"

**Resultado esperado:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Teste
print(factorial(5))  # Output: 120
```

### Exemplo 2: API JavaScript
**Prompt:** "Criar uma API REST simples em JavaScript para gerenciar usuários"

**Resultado esperado:**
```javascript
const express = require('express');
const app = express();

app.use(express.json());

let users = [];

// GET todos os usuários
app.get('/users', (req, res) => {
    res.json(users);
});

// POST criar usuário
app.post('/users', (req, res) => {
    const user = { id: Date.now(), ...req.body };
    users.push(user);
    res.status(201).json(user);
});

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});
```

## 🤖 Bot do Telegram

### Exemplo: Bot de Cotações
**Prompt:** "Bot que mostra cotação do Bitcoin"

**Código gerado:**
```python
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Bitcoin", callback_data='btc')],
        [InlineKeyboardButton("📈 Ethereum", callback_data='eth')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        '🤖 Bot de Cotações\n\nEscolha uma criptomoeda:',
        reply_markup=reply_markup
    )

async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Implementar consulta de preço
    await update.message.reply_text("💰 Bitcoin: $45,230.50 USD")

def main():
    application = Application.builder().token("SEU_TOKEN_AQUI").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("preco", get_price))
    
    application.run_polling()

if __name__ == '__main__':
    main()
```

## 📈 Trading Automatizado

### Exemplo: Análise Técnica
**Resultado da análise de BTCUSDT:**
```
📊 Análise de Mercado - BTCUSDT
💰 Preço Atual: 45,230.50 USD
📈 Tendência: Bullish
📉 RSI: 65.4
📊 MACD: Positive
🎯 Recomendação: COMPRAR
```

## 🎨 Geração de Imagens

### Exemplo: Prompt para IA
**Prompt:** "Um robô futurista programando em Python"

**Resultado:**
```
🎨 Imagem gerada com sucesso!
📄 Prompt: Um robô futurista programando em Python
💾 Arquivo: imagem_gerada_20250720_001148.png
🔗 Estilo: Realista, alta resolução
```

## 📺 YouTube Automation

### Exemplo: Upload Automático
**Configuração:**
```python
titulo = "DevAgent IA Pro - Demonstração"
descricao = """
🤖 Demonstração do DevAgent IA Pro

Funcionalidades:
• Geração de código com IA
• Bots do Telegram
• Trading automatizado
• Geração de imagens

#IA #Python #Automation #DevAgent
"""

resultado = publicar_youtube(titulo, descricao, "demo_video.mp4")
```

**Resultado:**
```
📺 Vídeo publicado no YouTube com sucesso!
📝 Título: DevAgent IA Pro - Demonstração
🆔 ID do Vídeo: yt_20250720_001148
🔗 URL: https://youtube.com/watch?v=yt_20250720_001148
```

## ⚙️ Configurações Avançadas

### Exemplo: Configuração Personalizada
```json
{
  "nome": "DevAgent Config",
  "versao": "1.0",
  "funcionalidades": ["codigo", "telegram", "trading", "imagens"],
  "apis": {
    "replicate": "configurado",
    "telegram": "pendente",
    "binance": "pendente"
  },
  "configuracoes": {
    "linguagem_padrao": "Python",
    "nivel_complexidade": "Intermediário",
    "auto_save": true
  }
}
```

## 🚀 Dicas de Uso

1. **Prompts Específicos**: Seja detalhado nos prompts para melhores resultados
2. **Configure APIs**: Adicione suas chaves reais no `secrets.toml`  
3. **Teste Antes**: Use o `test_devagent.py` para verificar tudo
4. **Personalize**: Modifique os templates conforme sua necessidade
5. **Monitore**: Acompanhe os logs para debugar problemas

## 📞 Suporte

Se encontrar problemas:
1. Execute `python test_devagent.py`
2. Verifique as configurações no `.streamlit/secrets.toml`
3. Consulte os logs do Streamlit
4. Abra uma issue no GitHub

---

**DevAgent IA Pro** - Automatizando o futuro da programação! 🤖✨
