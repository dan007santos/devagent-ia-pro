# DevAgent IA Pro

Um **agente de IA autônomo** que escreve código, cria bots, conecta a corretoras e muito mais!

## 🚀 Funcionalidades

### ✅ **Implementado e Funcionando:**
- 🤖 **Geração de Código com IA**: Múltiplas linguagens (Python, JavaScript, Java, C++, Go, Rust)
- 🔧 **Níveis de Complexidade**: Básico, Intermediário, Avançado  
- 📊 **Interface Streamlit**: Dashboard completo com estatísticas
- 🛠️ **Sistema de Ferramentas**: Telegram, Trading, Imagens, YouTube
- ⚙️ **Configurações**: Sistema de arquivos JSON para configurações
- 📈 **Análise de Mercado**: Simulação de dados técnicos
- 💬 **Sistema de Feedback**: Interface para melhorias

### 🚧 **Em Desenvolvimento:**
- 📱 **Bots do Telegram**: Criação automática com botões
- 📈 **Conexão com Corretoras**: APIs reais da Binance, Bybit, KuCoin
- 🎨 **Geração de Imagens**: Stable Diffusion integrado
- 🎥 **Upload YouTube**: Publicação automática de vídeos

### 🔮 **Próximas Versões:**
- 🧠 **Agente Autônomo**: Tomada de decisões independente
- 🔄 **Automação Completa**: Workflows automatizados  
- 📊 **Analytics Avançado**: Relatórios detalhados
- 🌐 **API REST**: Integração com outros sistemas

## 📋 Requisitos
- Python 3.8+
- Conta na OpenAI (para GPT)
- Tokens de API das corretoras (opcional)
- Token do bot Telegram (opcional)
- API do YouTube (opcional)

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/dan007santos/devagent-ia-pro.git
cd devagent-ia-pro
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves de API
```

## 🚀 Como Usar

1. **Inicie a interface web:**
```bash
streamlit run frontend/app.py
```

2. **Acesse no navegador:**
```
http://localhost:8501
```

3. **Funcionalidades disponíveis:**
   - 🤖 **Geração de Código**: Descreva o que quer e a IA gera o código
   - 🔧 **Múltiplas Linguagens**: Python, JavaScript, Java, C++, Go, Rust
   - 📊 **Níveis de Complexidade**: Básico, Intermediário, Avançado
   - 💬 **Sistema de Feedback**: Ajude a melhorar o sistema
   - 📈 **Estatísticas**: Acompanhe o uso da aplicação

## ☁️ Deploy no Streamlit Cloud

**Passo 1:** Faça upload do código no GitHub  
**Passo 2:** Acesse: https://streamlit.io/cloud  
**Passo 3:** Cole o link do seu repositório  
**Passo 4:** Defina `frontend/app.py` como caminho do app  
**Passo 5:** Adicione as variáveis de ambiente

## 🧪 Testes

Execute os testes para verificar se tudo está funcionando:

```bash
python test_devagent.py
```

Este comando testará:
- ✅ Conexão com APIs (Telegram, Binance)  
- ✅ Geração de imagens simulada
- ✅ Upload no YouTube simulado
- ✅ Análise de mercado
- ✅ Sistema de configurações
- ✅ Todas as ferramentas integradas

## 📁 Estrutura do Projeto

```
devagent-ia-pro/
├── frontend/
│   └── app.py              # Interface web (Streamlit)
├── backend/
│   ├── agents.py           # Agente autônomo
│   └── tools.py            # Ferramentas (Telegram, Binance, etc)
├── requirements.txt        # Dependências
├── README.md               # Instruções de uso
└── .streamlit/secrets.toml # Variáveis de ambiente (opcional)
```

## 🔧 Configuração

### Variáveis de Ambiente (`.streamlit/secrets.toml`)

```toml
REPLICATE_API_TOKEN = "sua-api-key-do-replicate"
TELEGRAM_BOT_TOKEN = "seu-token-do-telegram"
BINANCE_API_KEY = "sua-api-key-da-binance"
BINANCE_API_SECRET = "sua-secret-da-binance"
```

### Alternativa (.env)

```env
# OpenAI
OPENAI_API_KEY=your_openai_key

# Telegram
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# Corretoras
BINANCE_API_KEY=your_binance_key
BINANCE_SECRET_KEY=your_binance_secret
BYBIT_API_KEY=your_bybit_key
BYBIT_SECRET_KEY=your_bybit_secret
KUCOIN_API_KEY=your_kucoin_key
KUCOIN_SECRET_KEY=your_kucoin_secret

# YouTube
YOUTUBE_API_KEY=your_youtube_key

# Stable Diffusion
HUGGINGFACE_TOKEN=your_huggingface_token
```

## 🤖 Funcionalidades Detalhadas

### 1. Geração de Código
- Suporte a múltiplas linguagens
- Templates personalizáveis
- Análise de código existente

### 2. Bots do Telegram
- Interface com botões interativos
- Comandos customizáveis
- Integração com IA

### 3. Conexões com Corretoras
- Trading automatizado
- Análise de mercado
- Alertas de preço

### 4. Geração de Imagens
- Modelos Stable Diffusion
- Customização de prompts
- Múltiplos estilos

### 5. Upload YouTube
- Upload automático
- Geração de títulos e descrições
- Agendamento de publicações

## 🚨 Avisos Importantes

- Este é um software experimental
- Use com responsabilidade ao fazer trading
- Mantenha suas chaves de API seguras
- Teste em ambiente controlado primeiro

## 📝 Licença

MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request