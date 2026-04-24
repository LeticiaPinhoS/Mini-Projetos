import pandas as pd
import numpy as np

#Carregamento dos dados
df_pedidos = pd.read_csv("C:\\Users\\Letícia Pinho\\OneDrive\\Área de Trabalho\\Mini projetos- Recoketseat\\pedidos.csv")

#Análise exploratória

#Primeiras linhas
print(df_pedidos.head())
#últimas linhas
print(df_pedidos.tail())
#Verificando informaçoes gerais
print(df_pedidos.info())
#Verificando estatisticas
print(df_pedidos.describe())
print("-"*100)
#Criando nova coluna de Receita

df_pedidos["Receita"] = df_pedidos["Quantidade"] * df_pedidos["Preco_Unitario"]
print(df_pedidos.head())
print("-"*100)
#Tratando os valores ausentes
print(df_pedidos.isna().sum())
print("-"*100)

media_qtd = df_pedidos["Quantidade"].mean()
df_pedidos["Quantidade"].fillna(media_qtd, inplace=True)
#Remover os valores ausentes do Preço unitario
df_preco_limpo = df_pedidos.dropna(subset=["Preco_Unitario"])
print(df_preco_limpo.info())
print("-"*100)

#Agrupar os dados por item
pedidos_item = df_pedidos.groupby("Item").agg(
    Quantidade_total = ("Quantidade", "sum"),
    Receita_total = ("Receita", "sum")
)
print(pedidos_item)
print("-"*100)
#Identificando os top 5 itens mais vendidos por quantidade

itens_mais_vend = df_pedidos.sort_values(by = 'Quantidade', ascending=False)
print(itens_mais_vend.head(5))
print("-"*100)
itens_mais_vend = df_pedidos.sort_values(by="Receita", ascending=False)
print(itens_mais_vend.head(5))
print("-"*100)
#Converter a Data para o formato correto
df_pedidos["Data"] = pd.to_datetime(df_pedidos["Data"])
#Extraindo o mes de cada pedido
df_pedidos["Mes_Vendas"] = df_pedidos["Data"].dt.month
print(df_pedidos.head())
print("-"*100)
#Receita total do mes
pedidos_mes = df_pedidos.groupby("Mes_Vendas")["Receita"].sum().reset_index()
print("\nVendas por mês")
print(pedidos_mes)
print("-"*100)

df_cardapio = pd.read_csv("C:\\Users\\Letícia Pinho\\OneDrive\\Área de Trabalho\\Mini projetos- Recoketseat\\cardapio.csv")

df_merge = pd.merge(df_pedidos, df_cardapio, on= "Item", how= "left")
print(df_merge)
print("-"*100)
vendas_por_cat = df_merge.groupby("Categoria")["Receita"].sum().reset_index()
print(vendas_por_cat.head())
print("-"*100)
categoria_mais_receita = vendas_por_cat.sort_values(by ='Receita', ascending=False)
print(categoria_mais_receita.head(1))

#Filtragem avançada
df_query = df_merge.query("Categoria == 'Salgados' and Quantidade > 10")

print(df_query)
print("-"*100)

receita_total= df_merge["Receita"].sum()
print(f"A Receita total foi de: {receita_total} reais")
print("-"*100)
total_itens = df_merge["Quantidade"].sum()
print(f"O total de itens vendidos foram de {total_itens}")
print("-"*100)
ticket_medio = receita_total / total_itens
print(f"O ticket médio foi de {ticket_medio:.2f}")

#Fazendos os quartis

preco_limpo =df_pedidos["Preco_Unitario"].dropna()
qtd_limpa = df_pedidos["Quantidade"].dropna()

porcentis = [25,50,75]

print("Percentis de Preco_Unitario")
for p in porcentis:
    valor = np.percentile(preco_limpo, p)
    print(f"{p}%: {valor:.2f}")

print("\nPercentis da Quantidade")
for p in porcentis:
    valor = np.percentile(qtd_limpa,p)
    print(f"{p}%: {valor:.2f}")