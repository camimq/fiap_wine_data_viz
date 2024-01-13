import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importa dataframe
wine_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')

wine_data.head()

# verifica linhas duplicadas no dataset e deleta (as duplicatas)
wine_data[wine_data.duplicated()]
wine_data.drop_duplicates(keep='first', inplace=True)

# gerando gráficos

## distribuição da acidez volátil por qualidade do vinho

### cria df com acidez volátil x qualidade 3
df_acidez_x_qualidade_3 = wine_data.loc[(wine_data['quality'])==3]
df_acidez_x_qualidade_3.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_3

#### cria gráfico de distribuição com seaborn
sns.histplot(data=df_acidez_x_qualidade_3, x='volatile acidity',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 3')
plt.show()

### cria df com acidez volátil x qualidade 4
df_acidez_x_qualidade_4 = wine_data.loc[(wine_data['quality'])==4]
df_acidez_x_qualidade_4.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_4

#### cria gráfico de distribuição
sns.histplot(data=df_acidez_x_qualidade_4, x='volatile acidity',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 4')
plt.show()

### cria df com acidez volátil x qualidade 5
df_acidez_x_qualidade_5 = wine_data.loc[(wine_data['quality'])==5]
df_acidez_x_qualidade_5.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_5

#### cria gráfico de distribuição
sns.histplot(data=df_acidez_x_qualidade_5, x='volatile acidity',
             bins=20,
             element='step',
            color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 5')
plt.show()

### cria df com acidez volátil x qualidade 6
df_acidez_x_qualidade_6 = wine_data.loc[(wine_data['quality'])==6]
df_acidez_x_qualidade_6.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_6

#### cria gráfico de distribuição
sns.histplot(data=df_acidez_x_qualidade_6, x='volatile acidity',
             bins=20,
             element='step',
            color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 6')
plt.show()

### cria df com acidez volátil x qualidade 7
df_acidez_x_qualidade_7 = wine_data.loc[(wine_data['quality'])==7]
df_acidez_x_qualidade_7.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_7

#### cria gráfico de distribuição
sns.histplot(data=df_acidez_x_qualidade_7, x='volatile acidity',
             bins=20,
             element='step',
            color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 7')
plt.show()

### cria df com acidez volátil x qualidade 8
df_acidez_x_qualidade_8 = wine_data.loc[(wine_data['quality'])==8]
df_acidez_x_qualidade_8.drop(['fixed acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis='columns', inplace=True)

df_acidez_x_qualidade_8

#### cria gráfico de distribuição
sns.histplot(data=df_acidez_x_qualidade_8, x='volatile acidity',
             bins=20,
             element='step',
            color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.title('Distribuição da Acidez Volátil | Vinhos Qualidade 8')
plt.show()

## distribuição do teor alcoólico por qualidade do vinho

### cria df com teor alcoólico x qualidade 3
df_teor_x_qualidade_3 = wine_data.loc[(wine_data['quality'])==3]
df_teor_x_qualidade_3.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_3

#### cria gráfico de distribuição
sns.histplot(data=df_teor_x_qualidade_3, x='alcohol',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 3')
plt.show()

### cria df com teor alcoólico x qualidade 4
df_teor_x_qualidade_4 = wine_data.loc[(wine_data['quality'])==4]
df_teor_x_qualidade_4.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_4

#### cria gráfico de distribuição
sns.histplot(data=df_teor_x_qualidade_4, x='alcohol',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 4')
plt.show()

### cria df com teor alcoólico x qualidade 5
df_teor_x_qualidade_5 = wine_data.loc[(wine_data['quality'])==5]
df_teor_x_qualidade_5.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_5

#### cria gráfico de distribuição
sns.histplot(data=df_teor_x_qualidade_5, x='alcohol',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 5')
plt.show()

### cria df com teor alcoólico x qualidade 6
df_teor_x_qualidade_6 = wine_data.loc[(wine_data['quality'])==6]
df_teor_x_qualidade_6.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_6

#### cria gráfico de distribuição
sns.histplot(data=df_teor_x_qualidade_6, x='alcohol',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 6')
plt.show()

### cria df com teor alcoólico x qualidade 7
df_teor_x_qualidade_7 = wine_data.loc[(wine_data['quality'])==7]
df_teor_x_qualidade_7.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_7

#### cria gráfico de distribuição
sns.histplot(data=df_teor_x_qualidade_7, x='alcohol',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 7')
plt.show()

### cria df com teor alcoólico x qualidade 8
df_teor_x_qualidade_8 = wine_data.loc[(wine_data['quality'])==8]
df_teor_x_qualidade_8.drop(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'], axis='columns', inplace=True)

df_teor_x_qualidade_8

#### cria gráfico de distribuição
sns.histplot(data=df_teor_x_qualidade_8, x='alcohol',
             bins=20,
             element='step',
             color='midnightblue')
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.title('Distribuição do Teor Alcoólico | Vinhos Qualidade 8')
plt.show()

# visualiza relação entre acidez volátil e teor alcoólico
sns.scatterplot(x='volatile acidity', y='alcohol', hue='alcohol', data=wine_data)
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.title('Relação Acidez Volátil x Teor Alcoólico')
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.show()

# visualiza relação entre teor alcoólico e qualidade do vinho
sns.scatterplot(x='alcohol', y='quality', hue='quality', data=wine_data)
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.title('Relação Teor Alcoólico x Qualidade')
plt.xlabel('Teor Alcoólico')
plt.ylabel(' ')
plt.show()

# visualiza relação entre acidez volátil e qualidade do vinho
sns.scatterplot(x='volatile acidity', y='quality', hue='quality', data=wine_data)
sns.despine(bottom=True, left=True)
plt.tick_params(axis = 'y', labelsize=0, length=0)
plt.title('Relação Acidez Volátil x Qualidade')
plt.xlabel('Acidez Volátil')
plt.ylabel(' ')
plt.show()