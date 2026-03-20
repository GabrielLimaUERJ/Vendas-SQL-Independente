import streamlit as st
import pandas as pd

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="Análise de Vendas", layout="wide")
st.title("📊 App de Análise de Vendas")

# -------------------------------
# UPLOAD DO ARQUIVO
# -------------------------------
arquivo = st.file_uploader("📂 Faça upload do arquivo CSV", type=["csv"])

if arquivo is None:
    st.warning("Por favor, envie um arquivo CSV para continuar.")
    st.stop()

df = pd.read_csv(arquivo)

# -------------------------------
# FORMATADORES
# -------------------------------
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_percentual(valor):
    return f"{valor*100:.1f}%"

# -------------------------------
# MENU
# -------------------------------
opcao = st.selectbox("Escolha uma análise:", [
    "Receita por categoria",
    "Lucro por categoria",
    "Produtos com prejuízo",
    "Desconto vs lucro",
    "Top clientes",
    "Clientes com prejuízo",
    "Vendas por região",
    "Produtos mais vendidos",
    "Ticket médio por cliente"
])

# -------------------------------
# CONTROLE TOP N (somente onde faz sentido)
# -------------------------------
usar_top = opcao in ["Top clientes", "Produtos mais vendidos"]

if usar_top:
    top_n = st.slider("Quantidade de resultados (Top N)", 5, 50, 10)

# -------------------------------
# ANÁLISES
# -------------------------------
if opcao == "Receita por categoria":
    resultado = df.groupby("category")["sales"].sum().sort_values(ascending=False).reset_index()
    resultado.columns = ["Categoria", "Receita"]

elif opcao == "Lucro por categoria":
    resultado = df.groupby("category")["profit"].sum().sort_values(ascending=False).reset_index()
    resultado.columns = ["Categoria", "Lucro"]

elif opcao == "Produtos com prejuízo":
    resultado = df.groupby("product_name")["profit"].sum().reset_index()
    resultado = resultado[resultado["profit"] < 0].sort_values("profit")
    resultado.columns = ["Produto", "Lucro"]

elif opcao == "Desconto vs lucro":
    resultado = df.groupby("discount").agg(
        Quantidade=("discount", "count"),
        Lucro_Medio=("profit", "mean")
    ).reset_index()
    resultado.columns = ["Desconto", "Quantidade", "Lucro_Medio"]

elif opcao == "Top clientes":
    resultado = df.groupby("customer_name")["sales"].sum().sort_values(ascending=False).reset_index()
    resultado.columns = ["Cliente", "Receita"]
    if usar_top:
        resultado = resultado.head(top_n)

elif opcao == "Clientes com prejuízo":
    resultado = df.groupby("customer_name")["profit"].sum().reset_index()
    resultado = resultado[resultado["profit"] < 0].sort_values("profit")
    resultado.columns = ["Cliente", "Lucro"]

elif opcao == "Vendas por região":
    resultado = df.groupby("region").agg(
        Receita=("sales", "sum"),
        Lucro=("profit", "sum")
    ).sort_values("Receita", ascending=False).reset_index()
    resultado.columns = ["Região", "Receita", "Lucro"]

elif opcao == "Produtos mais vendidos":
    resultado = df.groupby("product_name")["quantity"].sum().sort_values(ascending=False).reset_index()
    resultado.columns = ["Produto", "Quantidade"]
    if usar_top:
        resultado = resultado.head(top_n)

elif opcao == "Ticket médio por cliente":
    resultado = df.groupby("customer_name")["sales"].mean().sort_values(ascending=False).reset_index()
    resultado.columns = ["Cliente", "Ticket_Médio"]

# -------------------------------
# KPI
# -------------------------------
if "Receita" in resultado.columns:
    st.metric("💰 Receita Total", formatar_real(resultado["Receita"].sum()))

elif "Lucro" in resultado.columns:
    st.metric("📈 Lucro Total", formatar_real(resultado["Lucro"].sum()))

elif "Ticket_Médio" in resultado.columns:
    st.metric("🧾 Ticket Médio", formatar_real(resultado["Ticket_Médio"].mean()))

# -------------------------------
# FORMATAÇÃO
# -------------------------------
df_display = resultado.copy()

for col in df_display.columns:
    if col in ["Receita", "Lucro", "Ticket_Médio"]:
        df_display[col] = df_display[col].apply(formatar_real)
    elif col == "Desconto":
        df_display[col] = df_display[col].apply(formatar_percentual)

# -------------------------------
# TABELA
# -------------------------------
st.subheader("📋 Dados")
st.dataframe(df_display, use_container_width=True)

# -------------------------------
# GRÁFICOS
# -------------------------------
st.subheader("📊 Visualização")

df_chart = resultado.set_index(resultado.columns[0])

if opcao == "Desconto vs lucro":
    st.line_chart(df_chart)
else:
    st.bar_chart(df_chart)