
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px

# Configuração da Página
st.set_page_config(page_title="Varejo | Data App", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 1. Carregamento de Dados 
@st.cache_data
def load_data():
    try:
        url="https://raw.githubusercontent.com/NiveskZ/KEVIN_MENESES_DDF_TECH_122025/main/data/silver/sales_sample.csv"
        df = pd.read_csv(url)  
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        # Criando lista de produtos únicos
        df_prod = df[['ProductName', 'Category']].drop_duplicates().reset_index(drop=True)
        return df, df_prod
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame(), pd.DataFrame()

df_sales, df_prod = load_data()

# --- SIDEBAR ---
st.sidebar.image("https://dadosfera.ai/wp-content/uploads/2022/01/icone-base.png", width=150)
st.sidebar.title("Menu de Navegação")
menu = st.sidebar.radio("Ir para:", ["Dashboard de Vendas", "Recomendação de Produtos"])

# --- PÁGINA: DASHBOARD ---
if menu == "Dashboard de Vendas":
    st.title("Varejo Inteligente - Analytics")
    
    # Métricas de Topo
    col_m1, col_m2, col_m3 = st.columns(3)
    total_faturamento = df_sales['TotalAmount'].sum()
    total_pedidos = df_sales.shape[0]
    ticket_medio = total_faturamento / total_pedidos if total_pedidos > 0 else 0
    
    col_m1.metric("Faturamento Total", f"R$ {total_faturamento:,.2f}")
    col_m2.metric("Total de Pedidos", f"{total_pedidos}")
    col_m3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

    st.markdown("---")

    col1 = st.container()
    
    with col1:
        st.subheader("Faturamento por Categoria")

        # preparar dados
        df_sales['TotalAmount'] = pd.to_numeric(df_sales['TotalAmount'], errors='coerce').fillna(0)
        cat_rev = df_sales.groupby('Category', dropna=False)['TotalAmount'].sum().sort_values(ascending=False)

        # controles
        top_n = st.slider("Mostrar Top N categorias", min_value=5, max_value=20, value=10, step=1, key="top_n_cat")
        chart_type = st.selectbox("Tipo de gráfico", ["Barra horizontal (recomendada)", "Treemap"], key="cat_chart_type")

        # criar dataframe com Others
        top = cat_rev.head(top_n)
        others = cat_rev.iloc[top_n:].sum()
        plot_df = top.reset_index().rename(columns={'Category':'Category', 'TotalAmount':'TotalAmount'})
        if others > 0:
            plot_df = pd.concat([plot_df, pd.DataFrame([{'Category':'Others', 'TotalAmount': others}])], ignore_index=True)

        # plot
        if chart_type == "Barra horizontal (recomendada)":
            fig = px.bar(plot_df, x='TotalAmount', y='Category', orientation='h',
                        title=f"Top {top_n} Categorias por Faturamento (Others agregado)")
            fig.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(l=60, r=20, t=40, b=40))
        else:
            fig = px.treemap(plot_df, path=['Category'], values='TotalAmount',
                            title=f"Top {top_n} Categorias por Faturamento (Treemap)")

        st.plotly_chart(fig, use_container_width=True)

# --- PÁGINA: SIMILARIDADE ---
elif menu == "🔍 Recomendação de Produtos":
    st.title("🔍 Inteligência de Similaridade")
    
    if not df_prod.empty:
        # Seleção de Produto
        prod_list = df_prod['ProductName'].tolist()
        selected_prod = st.selectbox("Selecione um produto da base para encontrar similares:", prod_list)
        
        # Lógica de Similaridade (NLP)
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(df_prod['ProductName'] + " " + df_prod['Category'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Encontrar o índice do produto selecionado
        idx = df_prod[df_prod['ProductName'] == selected_prod].index[0]
        
        # Calcular scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6] # Top 5 (exclui ele mesmo)
        
        st.success(f"Produtos similares a **{selected_prod}**:")
        
        for i, score in sim_scores:
            col_a, col_b = st.columns([3, 1])
            col_a.write(f"✅ **{df_prod.iloc[i]['ProductName']}**")
            col_b.info(f"Categoria: {df_prod.iloc[i]['Category']}")
    else:
        st.warning("Base de produtos não encontrada.")

st.sidebar.markdown("---")
st.sidebar.caption("Desenvolvido para Case Técnico Dadosfera")
