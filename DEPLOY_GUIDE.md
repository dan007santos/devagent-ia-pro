# Deploy no Streamlit Community Cloud

## Passos para hospedar GRATUITAMENTE:

### 1. Preparar o repositório
- Seu código já está no GitHub: https://github.com/dan007santos/devagent-ia-pro
- ✅ Já tem requirements.txt
- ✅ Já tem o app.py

### 2. Criar conta no Streamlit Cloud
1. Acesse: https://share.streamlit.io/
2. Faça login com sua conta do GitHub (dan007santos)
3. Clique em "New app"

### 3. Configurar o deploy
- Repository: dan007santos/devagent-ia-pro
- Branch: main
- Main file path: streamlit_app.py  ⬅️ IMPORTANTE: Use este arquivo!
- App URL: Você pode escolher: devagent-ia-pro.streamlit.app

### 4. Configurar secrets (variáveis privadas)
No painel do Streamlit Cloud:
- Vá em "Settings" > "Secrets"
- Cole exatamente isso:

```toml
REPLICATE_API_TOKEN = "sua-chave-replicate-aqui"
```
**SUBSTITUA** pela sua chave real que começa com r8_

### 5. Deploy automático
- O Streamlit Cloud fará o deploy automaticamente
- Seu app ficará disponível em: https://seu-app.streamlit.app
- Atualizações no GitHub são refletidas automaticamente

## ✅ VANTAGENS:
- 🆓 Totalmente GRATUITO
- 🚀 Deploy automático do GitHub  
- 🔒 Secrets seguros
- 📱 SSL automático (HTTPS)
- 🌍 CDN global
- 🔄 Auto-updates do GitHub

## 📱 Seu app ficará online em segundos!
