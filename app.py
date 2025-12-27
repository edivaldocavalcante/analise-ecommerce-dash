# ==============================
# IMPORTAÇÕES
# ==============================
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# ==============================
# LEITURA DOS DADOS
# ==============================
df = pd.read_csv("ecommerce_estatistica.csv")

# ==============================
# CRIAÇÃO DOS GRÁFICOS
# ==============================

# 1. Histograma - Distribuição de Preço
fig_hist = px.histogram(
    df,
    x="Preço",
    nbins=20,
    title="Distribuição de Preços dos Produtos"
)

# 2. Dispersão - Preço vs Quantidade Vendida
fig_scatter = px.scatter(
    df,
    x="Preço_MinMax",
    y="Qtd_Vendidos_Cod",
    title="Relação entre Preço e Quantidade Vendida",
    opacity=0.6
)

# 3. Mapa de Calor - Correlação
fig_heatmap = px.imshow(
    df.select_dtypes(include="number").corr(),
    text_auto=True,
    title="Mapa de Calor - Correlação entre Variáveis"
)

# 4. Gráfico de Barras - Top Marcas
top_marcas = df["Marca"].value_counts().head(10).reset_index()
top_marcas.columns = ["Marca", "Quantidade"]

fig_bar = px.bar(
    top_marcas,
    x="Marca",
    y="Quantidade",
    title="Top 10 Marcas Mais Frequentes"
)

# 5. Gráfico de Pizza - Distribuição por Temporada
fig_pie = px.pie(
    df,
    names="Temporada",
    title="Distribuição de Produtos por Temporada"
)

# 6. Gráfico de Densidade - Preço
fig_density = px.density_contour(
    df,
    x="Preço",
    title="Densidade de Preços"
)

# 7. Gráfico de Regressão
fig_reg = px.scatter(
    df,
    x="Preço_MinMax",
    y="Qtd_Vendidos_Cod",
    trendline="ols",
    title="Regressão: Preço vs Quantidade Vendida"
)

# ==============================
# CRIAÇÃO DA APLICAÇÃO DASH
# ==============================
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Dashboard de Análise de E-commerce",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig_hist),
        dcc.Graph(figure=fig_scatter),
        dcc.Graph(figure=fig_heatmap),
        dcc.Graph(figure=fig_bar),
        dcc.Graph(figure=fig_pie),
        dcc.Graph(figure=fig_density),
        dcc.Graph(figure=fig_reg),
    ]
)

# ==============================
# EXECUÇÃO DO SERVIDOR
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
