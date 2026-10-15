import streamlit as st
import os

LINK_MORANGO = "https://www.alimentosindustrializados.com.br/wp-content/uploads/2023/04/sorvete-scaled.jpg"
LINK_CHOCOLATE = "https://conteudo.imguol.com.br/c/entretenimento/51/2023/06/03/sorvete-de-batata-da-suecia-1685820919014_v2_450x600.jpg"
LINK_CHICLETE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvB1IJLUp0wJhMQWPtlUNWShCZeEOJI--KT_3K3MUcF1CLX1crBpJS7XDu&s=10"
LINK_ACAI_TRADICIONAL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBmuZMQ9xNIFudyDb_befQ6ckSWx2yU_eHNLY6IJDkijThZVtUPPQ4CUw&s=10"
LINK_PURA_COM_FRUTAS = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqJDRgw7Frjov1nOLAYwr3ywTOo9M_ATlF9Jv7gAFgFw5Nwk8HyTfHR5cv&s=10"
LINK_CREMES = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSN3IXnKUxlyvH8f3HO0aYUNKKCEltnQGR-Ru4XwaAfOw&s"
LINK_COM_MOUSSE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_AR8wqCeio5vHMA98fkV2wWE4PAidEmGx-b8fJeo7wyiwePANxOo7w7E&s=10"
LINK_BRINDE_EXTRA = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2GblQF_dYXIYxCANlDiAUKpW05SVp55FkIKTfe6fTrZgdBEj4Pm45bns&s=10"

TABELA_PRECOS = {
    "🍫 Chocolate": 8.50,
    "🍓 Morango": 8.00,
    "🍬 Chiclete": 7.50,
    "🍇 Açaí Tradicional": 12.00,
    "🍒 Pura com Frutas": 14.00,
    "🍦 Cremes": 8.00,
    "🍮 Com Mousse": 9.50
}

st.set_page_config(
    page_title="BALP Sorveteria - Painel",
    page_icon="🍦",
    layout="wide"
)


st.markdown("""
<style>
@import url('https://googleapis.com');
.stApp {
    background-color: #FFFBF1 !important;
}
.block-container {
    padding: 1rem 2rem !important;
    max-width: 100% !important;
}
footer, header {
    visibility: hidden !important;
}
h1, h2, h3, p, span, div, label {
    font-family: 'Quicksand', sans-serif !important;
    color: #2D5B7B !important;
}
.header-balp {
    text-align: center;
    background-color: #A3D2E2;
    padding: 30px 20px;
    border-bottom: 6px solid #2D5B7B;
    border-radius: 20px;
    margin-bottom: 30px;
}
.logo-container {
    background: white;
    display: inline-block;
    padding: 10px 50px;
    border-radius: 50px;
    border: 3px dashed #FFB7B2;
}
.logo-title {
    font-family: 'Fredoka', sans-serif !important;
    font-size: 40px;
    font-weight: 700;
    margin: 0;
}
.logo-date {
    font-size: 11px;
    color: #666 !important;
    display: block;
    font-weight: bold;
}
.box-pagamento {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 2px solid #2D5B7B;
}
.box-sabor {
    background: #EAF5F8;
    padding: 20px;
    border-radius: 20px;
    border: 2px solid #2D5B7B;
    margin-bottom: 30px;
}
.card-png {
    background: white;
    padding: 15px;
    border-radius: 15px;
    border: 2px dashed #A3D2E2;
    text-align: center;
    margin-bottom: 15px;
    min-height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-balp">
    <div class="logo-container">
        <div class="logo-title">BALP</div>
        <span class="logo-date">desde 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)

if "perfil" not in st.session_state:
    st.session_state["perfil"] = None
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = []
if "transacao_concluida" not in st.session_state:
    st.session_state["transacao_concluida"] = False


if st.session_state["perfil"] is None:
    col_l, col_centro, col_r = st.columns([1, 1.5, 1])
    with col_centro:
        st.markdown("<h2 style='text-align: center; font-family: Fredoka;'>🔑 Acessar o Sistema</h2>", unsafe_allow_html=True)
        email_digitado = st.text_input("E-mail:", placeholder="Ex: moderador@sorveteriabalp.com")
        senha_digitada = st.text_input("Senha:", type="password", placeholder="Digite sua senha")
        
        if st.button("Entrar no Sistema", use_container_width=True):
            if email_digitado == "moderador@sorveteriabalp.com" and senha_digitada == "balp":
                st.session_state["perfil"] = "moderador"
            else:
                st.session_state["perfil"] = "cliente"
            st.rerun()
    st.stop()

st.sidebar.header("🚪 Painel de Controle")
st.sidebar.info(f"Modo Atual: {st.session_state['perfil'].capitalize()}")
if st.sidebar.button("Sair do Sistema / Deslogar"):
    st.session_state["perfil"] = None
    st.session_state["carrinho"] = []
    st.session_state["transacao_concluida"] = False
    st.rerun()

if st.session_state["perfil"] == "moderador":
    st.markdown("<h2 style='font-family: Fredoka;'>🔒 Área Restrita do Moderador</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="box-pagamento">
        <h3>Configurações Globais do Sistema</h3>
        <p>⚙️ <b>Taxa de Entrega padrão por KM:</b> R\$ 1.50</p>
        <p>⚙️ <b>Alterar Preços do Cardápio:</b> [Habilitado]</p>
        <p>⚙️ <b>Relatório Geral de Vendas:</b> [Habilitado]</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="box-sabor">', unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family: Fredoka;'>🍦 Seletor de Pedidos Dinâmico</h3>", unsafe_allow_html=True)

col_sab, col_qtd, col_btn = st.columns(3)
with col_sab:
    sabor_escolhido = st.selectbox("Selecione o sabor que deseja comprar:", list(TABELA_PRECOS.keys()))
with col_qtd:
    quantidade = st.number_input("Quantidade de itens:", min_value=1, value=1, step=1)
with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🛒 Adicionar ao Carrinho", use_container_width=True):
        preco_unit = TABELA_PRECOS[sabor_escolhido]
        st.session_state["carrinho"].append({
            "sabor": sabor_escolhido,
            "quantidade": quantidade,
            "preco_unitario": preco_unit,
            "subtotal": preco_unit * quantidade 
        })
        st.session_state["transacao_concluida"] = False
        st.rerun()

distancia_km = st.number_input("Distância para entrega (KM):", min_value=0.0, value=5.0, step=0.5)
taxa_por_km = 1.50
taxa_entrega_calculada = distancia_km * taxa_por_km
subtotal_produtos = sum(item["subtotal"] for item in st.session_state["carrinho"])
preco_total_calculado = subtotal_produtos + taxa_entrega_calculada if st.session_state["carrinho"] else 0.0

st.write(f"Preço Unitário do Sabor: R\$ {TABELA_PRECOS[sabor_escolhido]:.2f} | Valor Acumulado Total: R\$ {preco_total_calculado:.2f}")

if st.session_state["carrinho"]:
    if st.button("🗑️ Limpar Carrinho"):
        st.session_state["carrinho"] = []
        st.session_state["transacao_concluida"] = False
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)


vitrine_itens = [
    {"nome": "Sorvete de Morango", "link": LINK_MORANGO},
    {"nome": "Chocolate", "link": LINK_CHOCOLATE},
    {"nome": "Chiclete", "link": LINK_CHICLETE},
    {"nome": "Açaí Tradicional", "link": LINK_ACAI_TRADICIONAL},
    {"nome": "Pura com Frutas", "link": LINK_PURA_COM_FRUTAS},
    {"nome": "Cremes", "link": LINK_CREMES},
    {"nome": "Com Mousse", "link": LINK_COM_MOUSSE},
    {"nome": "Espaço Reserva 8", "link": LINK_BRINDE_EXTRA}
]
col_imagens, col_pagamento = st.columns(2)

with col_imagens:
    st.markdown("<h2 style='font-family: Fredoka; margin-top:0;'> Vitrine Digital Ativa</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    cols_distribuidas = [c1, c2, c3, c4, c1, c2, c3, c4]
    
    for idx, col_destino in enumerate(cols_distribuidas):
        item_atual = vitrine_itens[idx]
        with col_destino:
            if item_atual["link"]:
                st.image(item_atual["link"], caption=item_atual["nome"], use_container_width=True)
            else:
                st.markdown(f"""
                <div class="card-png">
                    🍦<br><b>{item_atual['nome']}</b><br><span style='font-size:10px; color:#999;'>Sem Imagem</span>
                </div>
                """, unsafe_allow_html=True)

# with col_pagamento:
#     st.markdown("<h2 style='font-family: Fredoka; margin-top:0;'>💳 Resumo e Finalização</h2>", unsafe_allow_html=True)
#     with st.container(border=False):
#         st.markdown('<div class="box-pagamento">', unsafe_allow_html=True)
#         st.markdown("### 🛒 Seu Carrinho")
        
#         if not st.session_state["carrinho"]:
#             st.warning("Seu carrinho está vazio. Adicione itens acima!")
#         else:
#             for item in st.session_state["carrinho"]:
#                 st.write(f"• **{item['sabor']}** (x{item['quantidade']}) - R\$ {item['subtotal']:.2f}")
        
#         st.markdown("---")
#         st.write(f"**Subtotal dos Produtos:** R\$ {subtotal_produtos:.2f}")
#         st.write(f"**Taxa de Entrega ({distancia_km} KM):** R\$ {taxa_entrega_calculada:.2f}")
#         st.markdown(f"### **Total Geral: R\$ {preco_total_calculado:.2f}**")
        

#         if not st.session_state["transacao_concluida"]:
#             forma_pagamento = st.radio("Escolha a forma de pagamento:", ["Pix", "Cartão de Crédito", "Dinheiro"])
#             if forma_pagamento == "Pix":
#                 st.info("Chave Pix CNPJ: `12.345.678/0001-99` - BALP Sorvetes LTDA.")
            
#             if st.button("🚀 Finalizar Compra e Enviar Pedido", type="primary", use_container_width=True):
#                 st.session_state["transacao_concluida"] = True
#                 st.rerun()
#         else:
#             st.success("🎉 Pedido realizado com sucesso! O motoboy já está preparando uma rota.")
#             if st.button("Criar Novo Pedido"):
#                 st.session_state["carrinho"] = []
#                 st.session_state["transacao_concluida"] = False
#                 st.rerun()
        
#         st.markdown('</div>', unsafe_allow_html=True)

with col_pagamento:
    st.markdown("<h2 style='font-family: Fredoka; margin-top:0;'>💳 Resumo e Finalização</h2>", unsafe_allow_html=True)
    with st.container(border=False):
        st.markdown('<div class="box-pagamento">', unsafe_allow_html=True)
        st.markdown("### 🛒 Seu Carrinho")
        
        if not st.session_state["carrinho"]:
            # Se o carrinho estiver vazio, mas a transação foi concluída, mostra o sucesso e o botão de reset aqui!
            if st.session_state["transacao_concluida"]:
                st.success("🎉 Pedido realizado com sucesso! O motoboy já está preparando uma rota.")
                if st.button("Criar Novo Pedido", use_container_width=True):
                    st.session_state["transacao_concluida"] = False
                    st.rerun()
            else:
                st.warning("Seu carrinho está vazio. Adicione itens acima!")
        else:
            for item in st.session_state["carrinho"]:
                st.write(f"• **{item['sabor']}** (x{item['quantidade']}) - R\$ {item['subtotal']:.2f}")
            st.markdown("---")
            st.write(f"**Subtotal dos Produtos:** R\$ {subtotal_produtos:.2f}")
            st.write(f"**Taxa de Entrega ({distancia_km} KM):** R\$ {taxa_entrega_calculada:.2f}")
            st.markdown(f"### **Total Geral: R\$ {preco_total_calculado:.2f}**")
            
            if not st.session_state["transacao_concluida"]:
                forma_pagamento = st.radio("Escolha a forma de pagamento:", ["Pix", "Cartão de Crédito", "Dinheiro"])
                if forma_pagamento == "Pix":
                    st.info("Chave Pix CNPJ: `12.345.678/0001-99` - BALP Sorvetes LTDA.")
                
                if st.button("🚀 Finalizar Compra e Enviar Pedido", type="primary", use_container_width=True):
                    st.session_state["transacao_concluida"] = True
                    st.session_state["carrinho"] = [] # Limpa o carrinho aqui para o fluxo reiniciar limpo
                    st.balloons() # O efeito roda neste momento exato
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)




# Email: moderador@sorveteriabalp.com
# senha: balp