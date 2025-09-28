#BLOCO 01 - Cria Banco de Dados e Insere Dados
import sqlite3
# Conectar ou criar o banco de dados SQLite
# O SQLite é um banco leve e embutido, ideal para análises locais
conexao = sqlite3.connect('dados_vendas.db')
# Criar cursor para executar comandos SQL
cursor = conexao.cursor()
# Criar tabela (caso não exista)
# A tabela possui campos para ID, data, produto, categoria e valor
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')
# Inserir dados fictícios de vendas para análise
# Os dados representam vendas ao longo de um ano (2023)
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')
# Salvar as alterações no banco de dados
conexao.commit()
#=================================================#
#BLOCO 02 - Carregar Dados no Pandas
import pandas as pd
# Carregar os dados do SQLite para um DataFrame do Pandas
# O Pandas facilita a manipulação e análise de dados tabulares
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)
# Inspeção inicial
print(df_vendas.head())
print(df_vendas.info())
print(df_vendas.describe())
#=================================================#
#BLOCO 03 - Análises de Vendas
# Total de vendas - soma de todos os valores de venda
print(" Total de Vendas:", df_vendas["valor_venda"].sum())
# Vendas por categoria - agrupa por categoria e soma os valores
print("\n Vendas por Categoria:")
print(df_vendas.groupby("categoria")["valor_venda"].sum())
# Produtos mais vendidos - agrupa por produto, soma valores e ordena decrescente
print("\n Produtos mais Vendidos:")
print(df_vendas.groupby("produto")["valor_venda"].sum().sort_values(ascending=False))
# Vendas por mês - converte data para datetime, extrai mês e agrupa por mês
df_vendas["data_venda"] = pd.to_datetime(df_vendas["data_venda"])
df_vendas["mes"] = df_vendas["data_venda"].dt.month
print("\n Vendas por Mês:")
print(df_vendas.groupby("mes")["valor_venda"].sum())
#=================================================#
#BLOCO 04 - Visualizações
import matplotlib.pyplot as plt
import seaborn as sns
# Configuração de estilo para os gráficos
sns.set_theme(style="whitegrid")
# Gráfico de barras: Vendas por categoria
plt.figure(figsize=(8,5))
sns.barplot(
data=df_vendas.groupby("categoria")["valor_venda"].sum().reset_index(),
x="categoria", y="valor_venda", palette="viridis"
)
plt.title("Vendas por Categoria")
plt.show()
# Gráfico de linha: Vendas mensais ao longo do ano
plt.figure(figsize=(10,6))
sns.lineplot(
data=df_vendas.groupby("mes")["valor_venda"].sum().reset_index(),
x="mes", y="valor_venda", marker="o", linewidth=2
)
plt.title("Vendas Mensais")
plt.show()
# Gráfico de barras: Top 5 produtos mais vendidos por valor
top5 = df_vendas.groupby("produto")["valor_venda"].sum().reset_index().sort_values(by=
"valor_venda", ascending=False).head(5)
plt.figure(figsize=(10,6))
sns.barplot(data=top5, x="produto", y="valor_venda", palette="mako")
plt.title("Top 5 Produtos Mais Vendidos")
plt.show()