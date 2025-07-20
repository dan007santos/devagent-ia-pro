import streamlit as st
import stripe
import datetime
from typing import Optional

# Configuração Stripe (adicionar sua chave)
stripe.api_key = st.secrets.get("STRIPE_SECRET_KEY", "sk_test_...")

class SistemaMonetizacao:
    def __init__(self):
        self.planos = {
            "free": {
                "nome": "Gratuito",
                "preco": 0,
                "limite_diario": 5,
                "funcionalidades": ["Código básico", "5 gerações/dia"]
            },
            "premium": {
                "nome": "Premium",
                "preco": 19.90,
                "limite_diario": float('inf'),
                "funcionalidades": ["Uso ilimitado", "Todas linguagens", "Calculadoras avançadas"]
            },
            "pro": {
                "nome": "Pro", 
                "preco": 39.90,
                "limite_diario": float('inf'),
                "funcionalidades": ["Tudo Premium", "Bots Telegram", "Trading", "Suporte prioritário"]
            }
        }
    
    def verificar_plano_usuario(self, email: str) -> str:
        """Verifica o plano do usuário no banco de dados"""
        # Aqui você integraria com seu banco de dados
        # Por enquanto, simulação:
        if email in st.secrets.get("usuarios_premium", []):
            return "premium"
        elif email in st.secrets.get("usuarios_pro", []):
            return "pro"
        return "free"
    
    def verificar_limite_uso(self, email: str, plano: str) -> bool:
        """Verifica se o usuário pode usar o serviço"""
        if plano != "free":
            return True
            
        # Para usuários gratuitos, verificar limite diário
        hoje = datetime.date.today().isoformat()
        uso_key = f"uso_{email}_{hoje}"
        uso_atual = st.session_state.get(uso_key, 0)
        
        return uso_atual < self.planos["free"]["limite_diario"]
    
    def incrementar_uso(self, email: str):
        """Incrementa o contador de uso"""
        hoje = datetime.date.today().isoformat()
        uso_key = f"uso_{email}_{hoje}"
        st.session_state[uso_key] = st.session_state.get(uso_key, 0) + 1
    
    def criar_sessao_pagamento(self, plano: str, email: str) -> str:
        """Cria sessão de pagamento no Stripe"""
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'brl',
                        'product_data': {
                            'name': f'DevAgent IA Pro - {self.planos[plano]["nome"]}',
                        },
                        'unit_amount': int(self.planos[plano]["preco"] * 100),
                        'recurring': {'interval': 'month'} if plano != "free" else None,
                    },
                    'quantity': 1,
                }],
                mode='subscription' if plano != "free" else 'payment',
                success_url='https://devagent-ia-pro.streamlit.app/?success=true',
                cancel_url='https://devagent-ia-pro.streamlit.app/?canceled=true',
                customer_email=email,
                metadata={'plano': plano, 'email': email}
            )
            return session.url
        except Exception as e:
            st.error(f"Erro ao criar pagamento: {e}")
            return None

def mostrar_planos_pagamento(sistema_monetizacao):
    """Interface para seleção e pagamento de planos"""
    
    st.markdown("## 💎 Escolha seu Plano")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🆓 GRATUITO
        - 5 gerações por dia
        - Código básico
        - Suporte comunidade
        
        **R$ 0/mês**
        """)
        
    with col2:
        st.markdown("""
        ### 💎 PREMIUM
        - ✅ Uso ILIMITADO
        - ✅ Todas linguagens  
        - ✅ Calculadoras avançadas
        - ✅ Suporte prioritário
        
        **R$ 19,90/mês**
        """)
        if st.button("🚀 Assinar Premium", key="premium"):
            email = st.text_input("Seu email:", key="email_premium")
            if email:
                url = sistema_monetizacao.criar_sessao_pagamento("premium", email)
                if url:
                    st.markdown(f"[💳 Finalizar Pagamento]({url})")
    
    with col3:
        st.markdown("""
        ### 🚀 PRO
        - ✅ Tudo do Premium
        - ✅ Bots Telegram
        - ✅ Trading automático
        - ✅ Consultoria mensal
        
        **R$ 39,90/mês**
        """)
        if st.button("🔥 Assinar Pro", key="pro"):
            email = st.text_input("Seu email:", key="email_pro")
            if email:
                url = sistema_monetizacao.criar_sessao_pagamento("pro", email)
                if url:
                    st.markdown(f"[💳 Finalizar Pagamento]({url})")

def mostrar_dashboard_usuario(email: str, plano: str, sistema_monetizacao):
    """Dashboard do usuário com informações do plano"""
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👤 Seu Plano")
    st.sidebar.markdown(f"**Plano:** {sistema_monetizacao.planos[plano]['nome']}")
    
    if plano == "free":
        hoje = datetime.date.today().isoformat()
        uso_key = f"uso_{email}_{hoje}"
        uso_atual = st.session_state.get(uso_key, 0)
        limite = sistema_monetizacao.planos["free"]["limite_diario"]
        
        st.sidebar.progress(uso_atual / limite)
        st.sidebar.markdown(f"**Uso hoje:** {uso_atual}/{limite}")
        
        if uso_atual >= limite * 0.8:  # 80% do limite
            st.sidebar.warning("⚠️ Limite quase atingido!")
            st.sidebar.markdown("💎 [Upgrade para Premium](https://devagent-ia-pro.streamlit.app/?upgrade=true)")
    
    else:
        st.sidebar.markdown("✅ **Uso ilimitado**")
        st.sidebar.markdown("🎉 **Todas as funcionalidades**")

# Exemplo de uso no streamlit_app.py principal:
"""
# No início do streamlit_app.py, adicionar:

sistema_monetizacao = SistemaMonetizacao()

# Sistema de login simples
if 'email_usuario' not in st.session_state:
    st.session_state.email_usuario = None

if not st.session_state.email_usuario:
    email = st.text_input("Digite seu email para continuar:")
    if email and st.button("Entrar"):
        st.session_state.email_usuario = email
        st.rerun()
else:
    email = st.session_state.email_usuario
    plano = sistema_monetizacao.verificar_plano_usuario(email)
    
    # Mostrar dashboard do usuário
    mostrar_dashboard_usuario(email, plano, sistema_monetizacao)
    
    # No botão "Gerar Código", adicionar verificação:
    if st.button("🚀 Gerar Código"):
        if sistema_monetizacao.verificar_limite_uso(email, plano):
            sistema_monetizacao.incrementar_uso(email)
            # ... resto do código de geração
        else:
            st.error("🚫 Limite diário atingido!")
            mostrar_planos_pagamento(sistema_monetizacao)
"""
