import streamlit as st

def criar_landing_page():
    """Landing page otimizada para conversão"""
    
    # Header hero
    st.markdown("""
    <div style="text-align: center; padding: 50px 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; margin: -1rem -1rem 2rem -1rem; border-radius: 0 0 20px 20px;">
        <h1>🤖 DevAgent IA Pro</h1>
        <h2>Gere Código Profissional em Segundos!</h2>
        <p style="font-size: 20px; margin: 20px 0;">
            De calculadoras de obra a bots do Telegram.<br>
            Sua próxima aplicação está a um clique de distância!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Demonstração rápida
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Você escreve:")
        st.code('"Criar uma calculadora para obra"', language='text')
        
    with col2:
        st.markdown("### 🚀 DevAgent entrega:")
        st.code('''class CalculadoraObra:
    def calcular_concreto(self, volume_m3):
        cimento_sacos = volume_m3 * 7
        areia_m3 = volume_m3 * 0.5
        # ... código completo e funcional''', language='python')
    
    # Benefícios
    st.markdown("---")
    st.markdown("## 🎯 Por que Desenvolvedores Escolhem o DevAgent?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### ⚡ **10x Mais Rápido**
        Gere código completo em segundos.
        Não mais horas debugando.
        """)
        
    with col2:
        st.markdown("""
        ### 🎯 **Código Inteligente**
        Templates específicos para cada necessidade.
        Calculadoras, bots, APIs prontas.
        """)
        
    with col3:
        st.markdown("""
        ### 💰 **Aumente sua Renda** 
        Entregue projetos mais rápido.
        Aceite mais clientes.
        """)
    
    # Casos de uso
    st.markdown("---")
    st.markdown("## 🛠️ O que Nossos Usuários Criam:")
    
    cases = [
        ("🏗️ Calculadoras de Obra", "Construtoras economizam 80% do tempo em orçamentos"),
        ("🤖 Bots do Telegram", "Automatize atendimento e vendas"),  
        ("📊 Sistemas de Trading", "Integração com Binance, Bybit, KuCoin"),
        ("📱 Apps Web", "Protótipos em minutos, MVPs em horas"),
        ("🔌 Integrações API", "Conecte qualquer serviço rapidamente"),
        ("🎓 Projetos Educacionais", "Ensine programação com exemplos reais")
    ]
    
    for i in range(0, len(cases), 2):
        col1, col2 = st.columns(2)
        with col1:
            title, desc = cases[i]
            st.markdown(f"**{title}**\n{desc}")
        if i + 1 < len(cases):
            with col2:
                title, desc = cases[i + 1]  
                st.markdown(f"**{title}**\n{desc}")
    
    # Depoimentos
    st.markdown("---")
    st.markdown("## 💬 O que Dizem Nossos Usuários:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        > "Economizo 5 horas por projeto. O DevAgent paga sozinho!"
        
        **João Silva** - Desenvolvedor Freelancer
        ⭐⭐⭐⭐⭐
        """)
        
    with col2:
        st.markdown("""
        > "Minha construtora agora faz orçamentos em tempo real!"
        
        **Maria Santos** - Engenheira Civil  
        ⭐⭐⭐⭐⭐
        """)
        
    with col3:
        st.markdown("""
        > "De R$ 2k para R$ 8k/mês. DevAgent mudou meu negócio!"
        
        **Pedro Costa** - Agência Digital
        ⭐⭐⭐⭐⭐
        """)
    
    # Urgência e escassez
    st.markdown("---")
    st.markdown("""
    <div style="background: #ff6b6b; color: white; padding: 20px; border-radius: 10px; text-align: center;">
        <h3>🔥 OFERTA LIMITADA - Apenas 100 Vagas!</h3>
        <p><strong>50% de desconto</strong> nos primeiros 3 meses</p>
        <p>⏰ Termina em: <strong>48 horas</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("---")
    st.markdown("### 🚀 Comece Agora - É Grátis!")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 TESTAR GRÁTIS AGORA", use_container_width=True):
            st.balloons()
            st.success("🎉 Conta criada! Você tem 5 gerações gratuitas hoje.")
            
        st.markdown("<small>✅ Sem cartão de crédito • ✅ Cancelamento a qualquer momento</small>", unsafe_allow_html=True)
    
    # FAQ
    st.markdown("---")
    st.markdown("## ❓ Perguntas Frequentes")
    
    with st.expander("🤔 Como funciona o DevAgent?"):
        st.markdown("""
        Você descreve o que quer criar em linguagem natural. 
        Nossa IA analisa e gera código completo e funcional.
        Simples assim!
        """)
        
    with st.expander("💰 Posso cancelar a qualquer momento?"):
        st.markdown("""
        Sim! Sem fidelidade, sem multa.
        Cancele quando quiser pelo painel do usuário.
        """)
        
    with st.expander("🔒 Meus códigos ficam seguros?"):
        st.markdown("""
        Absolutamente! Não armazenamos nem compartilhamos seu código.
        Tudo fica privado na sua conta.
        """)
        
    with st.expander("📞 Como é o suporte?"):
        st.markdown("""
        - **Gratuito:** Comunidade Discord
        - **Premium:** Email prioritário  
        - **Pro:** WhatsApp direto + consultoria mensal
        """)
    
    # Footer CTA
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 30px; background: #f0f2f6; border-radius: 10px;">
        <h3>🚀 Pronto para 10x sua Produtividade?</h3>
        <p>Junte-se a mais de <strong>1.000+ desenvolvedores</strong> que já transformaram seu workflow!</p>
    </div>
    """, unsafe_allow_html=True)

# Métricas de conversão
def rastrear_conversoes():
    """Rastrear métricas importantes"""
    
    # Google Analytics integration
    st.markdown("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'GA_MEASUREMENT_ID');
    </script>
    """, unsafe_allow_html=True)
    
    # Hotjar para heatmaps
    st.markdown("""
    <script>
        (function(h,o,t,j,a,r){
            h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            h._hjSettings={hjid:YOUR_HOTJAR_ID,hjsv:6};
            a=o.getElementsByTagName('head')[0];
            r=o.createElement('script');r.async=1;
            r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            a.appendChild(r);
        })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    criar_landing_page()
    rastrear_conversoes()
