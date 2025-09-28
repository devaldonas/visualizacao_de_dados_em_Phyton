# visualizacao_de_dados_em_Phyton
Analise de dados de vendas do último ano para identificar padrões e insights para melhorar o desempenho. Os dados estão armazenados em um banco de dados SQLite, onde utilizo a biblioteca Pandas para manipular e analisar esses dados, além de gerar visualizações utilizando Matplotlib e Seaborn.

#Lógica Utilizada
Foi Implementado o processo ETL (Extract, Transform, Load)
1. Extração e Armazenamento de dados
Utilizei o SQLite como banco de dados embutido para armazenamento local
Criei uma estrutura tabular normalizada com tabela vendas1
Inseri dados fictícios de vendas com variáveis temporais (datas), categorias e valores
2. Transformação e Análise
Foram extraidos os dados do SQLite para um DataFrame do Pandas
#Transformações de dados:
Conversão de tipos (string para datetime)
Extração de features (mês a partir da data)
Executa agregações estratégicas:
Somas por categoria, produto e período temporal
Ordenações para identificar padrões e tendências
3. Visualização e Insights
Gerar visualizações claras e informativas usando Seaborn/Matplotlib
Implementar três perspectivas de análise:
Perspectiva de Categoria: Comparativo entre segmentos de produtos
Perspectiva Temporal: Evolução das vendas ao longo do tempo
Perspectiva de Produtos: Identificação dos itens mais relevantes
