import pandas as pd
import numpy as np

df_vendas= pd.read_csv("C:\\Users\\Letícia Pinho\\OneDrive\\Área de Trabalho\\Mini projetos- Recoketseat\\vendas.csv")


#Primeiras linhas 
print(df_vendas.head())
print("-"*100)
#últimas linhas
print(df_vendas.tail())
print("-"*100)
#Verificando informações gerais
print(df_vendas.info())
print("-"*100)

#Verificando as estatisticas
print(df_vendas.describe())
print("-"*100)

#Criando nova coluna de Receita

df_vendas["Receita"] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]
print(df_vendas.head())
print()
print("-"*100)
#Filtrando alguns dados
print(df_vendas[["Produto", "Receita"]].head())
print("-"*100)

#Linhas onde a quantidade é maior que 20
print(df_vendas[df_vendas["Quantidade"] > 20].head())
print("-"*100)

#Utilizando loc e iloc

#Selecionar linhas e colunas por rótulo especificos

print(df_vendas.loc[df_vendas["Produto"]=="Monitor", ["ID_Venda", "Quantidade", "Preco_Unitario"]])
print("-"*100)

#Selecionar as primeiras 3 linhas e as colunas 1,2,3
print(df_vendas.iloc[0:3,1:4])
print("-"*100)

#Cálculos
#Descobrir o faturamento (Receita total)
print(f"Receita total de vendas da loja: {df_vendas["Receita"].sum():.2f}")

#Preço Médio unitario dos produtos
print(f"O preço médio unitário dos produtos é: {df_vendas["Preco_Unitario"].mean():.2f}")

#Quantidade máxima e mínima

print(f"A quantidade mínima de produtos: {df_vendas["Quantidade"].min()}")
print(f"A quantidade máxima de produtos: {df_vendas["Quantidade"].max()}")
print("-"*100)
#Simular valores ausentes no DF
df_vendas_aus = df_vendas.copy()

df_vendas_aus.loc[df_vendas_aus.sample(frac=0.05).index, "Preco_Unitario"] = np.nan
df_vendas_aus.loc[df_vendas_aus.sample(frac=0.03).index, "Quantidade"] = np.nan
#Verificar valores ausentes
print(df_vendas_aus.isna().sum())
print("-"*100)

#os 30 valores ausentes vou preencher com a média os valores nulos de quantidade
df_vendas_preenchido = df_vendas_aus.copy()
media_qtd = df_vendas_preenchido["Quantidade"].mean()
df_vendas_preenchido["Quantidade"].fillna(media_qtd, inplace=True)
print(df_vendas_preenchido.info())
print("-"*100)

#Remover os valores ausentes em preço unitário
df_vendas_limpo = df_vendas_preenchido.dropna(subset=["Preco_Unitario"])
print(df_vendas_limpo.info())
print("-"*100)

#Agrupar pro produtos e calcular quantidade e receita total por produto
vendas_por_prod = df_vendas_limpo.groupby("Produto").agg(
    Quantidade_Total = ("Quantidade", "sum"),
    Receita_Total = ("Receita", "sum")
).reset_index()
print(vendas_por_prod)
print("-"*100)
#Qual produto vendeu mais? Quem me gerou maior receita
#Ordenar o valores
produto_mais_vendido = vendas_por_prod.sort_values(by = "Quantidade_Total", ascending = False).iloc[0]
print(produto_mais_vendido)
print("-"*100)
produto_maior_receita = vendas_por_prod.sort_values(by="Receita_Total", ascending=False).iloc[0]
print(produto_maior_receita)
print("-"*100)
#Converter a coluna Data_Venda para tipo correto de data
df_vendas_limpo["Data_Venda"] = pd.to_datetime(df_vendas_limpo["Data_Venda"])


df_produtos = pd.read_csv("C:\\Users\Letícia Pinho\\OneDrive\\Área de Trabalho\\Mini projetos- Recoketseat\produtos.csv")

#Analisar as vendas por mês
df_vendas_limpo["Mes_Venda"] = df_vendas_limpo["Data_Venda"].dt.month
print(df_vendas_limpo.head())
print("-"*100)
#Agrupar por mês para calcular a receita total mes a mes
vendas_por_mes = df_vendas_limpo.groupby("Mes_Venda")["Receita"].sum().reset_index()
print("\nVendas por mês")
print(vendas_por_mes)
print("-"*100)
df_merge = pd.merge(df_vendas_limpo, df_produtos, on='Produto', how = 'left')
print(df_merge)
print("-"*100)

#Analise de vedas por categoria(Receita total)
vendas_por_cat = df_merge.groupby("Categoria")["Receita"].sum().reset_index()
print(vendas_por_cat)
print("-"*100)
print()
print("-"*100)
#Filtragem dentro do DF
print(df_merge.head())
#Filtrar por coluna (Produto, Quantidade, Receita Total)
print("-"*100)
df_colunas_filtradas = df_merge.filter(items=["Produto", "Quantidade", "Receita"])
print(df_colunas_filtradas)

print("-"*100)

#Filtragem mais avançadas (Produto: Teclado, quantidade > 10)
df_query = df_merge.query("Produto == 'Teclado' and Quantidade > 10")
print(df_query)