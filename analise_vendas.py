import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings


df_vendas1 = pd.read_csv("C:\\Users\\Letícia Pinho\\OneDrive\\Área de Trabalho\\Mini projetos- Recoketseat\\vendas1.csv")

#Exibindo as 5 primeiras linhas
print(df_vendas1.head())
#Exibindo o número total de registros
total_registros = len(df_vendas1)
print(f"Total de registros: {total_registros}")
#Calculando a receita total
df_vendas1["Receita_total"] = df_vendas1["quantidade"]* df_vendas1["preco_unitario"]
receita_total = df_vendas1["Receita_total"].sum()
print(f"Receita total: R${receita_total:.2f}")
#Filtrando e exibindo as categorias"Eletronicos"
filtro = df_vendas1[df_vendas1["categoria"]== "Eletrônicos"].copy()
print(f"{len(filtro)} vendas encontradas ")
print(filtro)
#Produto mais vendido
mais_vendido = df_vendas1.groupby("produto")['quantidade'].sum().idxmax()
qt_mais_vend = df_vendas1.groupby("produto")['quantidade'].sum().max()
print(f"Produto mais vendido: {mais_vendido} ({qt_mais_vend} unidades)")
#Região com maior valor de compras
receita_por_regiao = df_vendas1.groupby('regiao')['Receita_total'].sum()
regiao = receita_por_regiao.idxmax()
print(f"Região com maior receita: {regiao} R$ {receita_por_regiao[regiao]:.2f}")
print()
print("Receita por região: ")
for reg, val in receita_por_regiao.sort_values(ascending=False).items():
    print(f"{reg}: R$ {val:,.2f}")


#Visualizaçoes

receita_cat = df_vendas1.groupby('categoria')['Receita_total'].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(9, 4))
cores = sns.color_palette('Blues_d', len(receita_cat))
bars = ax.barh(receita_cat.index, receita_cat.values, color=cores, edgecolor='white')

# Adiciona os valores dentro das barras
for bar, val in zip(bars, receita_cat.values):
    ax.text(val * 0.98, bar.get_y() + bar.get_height()/2,
            f'R$ {val:,.0f}', va='center', ha='right', color='white', fontweight='bold', fontsize=9)

ax.set_title('Receita Total por Categoria', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Receita (R$)')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
ax.tick_params(axis='y', labelsize=10)
plt.tight_layout()
plt.savefig('grafico_receita_categoria.png', dpi=150, bbox_inches='tight')
plt.show()


#Evolução de vendas por mês(Gráfico de linha)
df_vendas1['mes'] = df_vendas1['data'].dt.to_period('M')
vendas_mes = df_vendas1.groupby('mes')['receita'].sum().sort_index()

fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(vendas_mes.index.astype(str), vendas_mes.values,
        marker='o', linewidth=2.5, color='steelblue', markersize=7)
ax.fill_between(vendas_mes.index.astype(str), vendas_mes.values, alpha=0.15, color='steelblue')

ax.set_title('Evolução da Receita por Mês', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Mês')
ax.set_ylabel('Receita (R$)')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig('grafico_evolucao_mensal.png', dpi=150, bbox_inches='tight')
plt.show()

#Tabela dinamica = Receita por regiao x Categoria

pivot = pd.pivot_table(
    df_vendas1,
    values='receita',
    index='regiao',
    columns='categoria',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='TOTAL'
)

# Formata os valores como moeda
pivot_fmt = pivot.applymap(lambda x: f'R$ {x:,.2f}')
pivot_fmt
nome_arquivo = 'relatorio_vendas.xlsx'

resumo_cat = df_vendas1.groupby('categoria').agg(
    receita_total=('receita', 'sum'),
    quantidade_total=('quantidade', 'sum'),
    num_vendas=('receita', 'count')
).reset_index().sort_values('receita_total', ascending=False)

with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
    df_vendas1.to_excel(writer, sheet_name='Dados Completos', index=False)
    resumo_cat.to_excel(writer, sheet_name='Resumo por Categoria', index=False)
    pivot.to_excel(writer, sheet_name='Tabela Dinamica')

print(f' Relatório exportado com sucesso: {nome_arquivo}')
print('   Abas criadas: Dados Completos | Resumo por Categoria | Tabela Dinamica')


#Resumo executivo 
print('=' * 50)
print('        RESUMO EXECUTIVO DE VENDAS')
print('=' * 50)
print(f'  Total de registros     : {len(df_vendas1)}')
print(f'  Receita total          : R$ {df_vendas1["receita"].sum():,.2f}')
print(f'  Ticket médio por venda : R$ {df_vendas1["receita"].mean():,.2f}')
print(f'  Produto mais vendido   : {mais_vendido}')
print(f'  Região top             : {regiao}')
print(f'  Categoria top          : {receita_cat.idxmax()}')
print('=' * 50)