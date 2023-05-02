# 1 - Importar a base de dados

import pandas as pd
import seaborn as sns

tabela = pd.read_csv("telecom_users.csv")


tabela = tabela.drop('Unnamed: 0', axis=1)

tabela.head()



tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")


tabela = tabela.dropna(how="all", axis=1)

tabela = tabela.dropna(how="any", axis=0)

tabela.info()

tabela = tabela.rename(columns={'Churn': 'Cancelamento'})

tabela['Cancelamento'].value_counts()
tabela['Cancelamento'].value_counts(normalize=True).map("{:.1%}".format)

with sns.axes_style('whitegrid'):

  grafico = sns.pairplot(data=tabela, hue="Cancelamento", palette="pastel")
