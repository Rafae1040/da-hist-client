# 1 - Importar a base de dados

import pandas as pd
import seaborn as sns

tabela = pd.read_csv("telecom_users.csv")

# 2 - Visualizar a Base de Dados

tabela = tabela.drop('Unnamed: 0', axis=1)

tabela.head()

#   Entender quais informações estão disponíveis
#   Descobrir as falhas na base de dados

# 3 - Tratamentos de Dados 

# Valores que estão reconhecidos de forma errada

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Deletando as colunas vazias

tabela = tabela.dropna(how="all", axis=1)

# Deletando as linhas vazias

tabela = tabela.dropna(how="any", axis=0)

tabela.info()

# 4 - Analise Inicial

# Como estão os nossos cancelamentos?

# Primeiro vamos renomear a coluna Churn para Cancelamento

tabela = tabela.rename(columns={'Churn': 'Cancelamento'})


tabela['Cancelamento'].value_counts()
tabela['Cancelamento'].value_counts(normalize=True).map("{:.1%}".format)

# 5 - Analise Completa

# Comparar cada coluna da minha tabela com a coluna de cancelamento

with sns.axes_style('whitegrid'):

  grafico = sns.pairplot(data=tabela, hue="Cancelamento", palette="pastel")
