import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# importa dataframe
wine_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')

wine_data.head()

# verifica linhas duplicadas no dataset e deleta (as duplicatas)
wine_data[wine_data.duplicated()]
wine_data.drop_duplicates(keep='first', inplace=True)

# gerando gráficos

## distribuição da acidez volátil por qualidade do vinho

filtered_wine_data_volatile_acidity = wine_data[['volatile acidity', 'quality']].groupby('quality').agg(np.average)

sns.catplot(data=filtered_wine_data_volatile_acidity, kind='bar', x='quality', y='volatile acidity', hue='quality')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Qualidade')
plt.ylabel('Acidez Volátil')
plt.title('Distribuição | Acidez Volátil x Qualidade')
plt.show()

## distribuição do teor alcoólico por qualidade do vinho
filtered_wine_data_alcohol = wine_data[['alcohol', 'quality']].groupby('quality').sum()

sns.catplot(data=filtered_wine_data_alcohol, kind='bar', x='quality', y='alcohol', hue='quality')
sns.despine(bottom=True, left=True)
plt.tick_params(axis='y', labelsize=0, length=0)
plt.xlabel('Qualidade')
plt.ylabel('Teor Alcoólico')
plt.title('Distribuição | Teor Alcoólico x Qualidade do Vinho')
plt.show()

# relação entre acidez volátil e teor alcoólico
sns.scatterplot(x='volatile acidity', y='alcohol', hue='alcohol', data=wine_data)
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.title('Relação Acidez Volátil x Teor Alcoólico')
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.show()

# relação entre teor alcoólico e qualidade do vinho
sns.scatterplot(x='alcohol', y='quality', hue='quality', data=wine_data)
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.title('Relação Teor Alcoólico x Qualidade')
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.show()

# relação entre acidez volátil e qualidade do vinho
sns.scatterplot(x='volatile acidity', y='quality', hue='quality', data=wine_data)
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.title('Relação Acidez Volátil x Qualidade')
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.show()