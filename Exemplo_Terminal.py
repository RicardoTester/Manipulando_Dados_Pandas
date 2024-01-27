import pandas as pd
 

# Conceito de DataFrame: estrutura de dados tabular bidimensional.
# DataFrames são a estrutura central do Pandas. Eles são semelhantes a tabelas de banco de
# dados ou planilhas, com linhas e colunas. 
# DataFrames permitem organizar, filtrar e manipular dados de maneira eficiente.


# Criando um DataFrame a partir de um dicionário

data = {'Nome':['Ricardo', 'Celia', 'Joao', 'Leandro', 'Fabio'],
    'Idade':[34, 71, 75, 14, 28]}

df = pd.DataFrame(data)
print(df)

      Nome  Idade
0  Ricardo     34
1    Celia     71
2     Joao     75
3  Leandro     14
4    Fabio     28


# Series: DataFrames Unidimensionais
# Entendendo o conceito de Series: estrutura unidimensional semelhante a um array ou
# coluna de uma planilha.
# Series são estruturas unidimensionais que armazenam dados, semelhantes a colunas de uma planilha. 
# Elas são frequentemente usadas para representar uma única variável.

#Criando uma series a partir de uma lista
idade = pd.Series([34, 71, 75, 14, 28])

print(idade)

0    34
1    71
2    75
3    14
4    28
dtype: int64

#Acessando elementos de uma Series
primeira_idade = idade[0]

print(primeira_idade)

34

# OPERAÇÕES BÁSICAS COM DATAFRAMES E SERIES:
#Compreensão dos tipos de dados (dtypes) em um DataFrame. Uso do método describe()
#para obter estatísticas descritivas. Aplicação de funções básicas como mean(), sum() e outras em colunas.

#Verificando os tipos de dados das colunas
tipos_de_dados = df.dtypes

print(tipos_de_dados)

Nome     object
Idade     int64
dtype: object

#Obtendo estatísticas descritivas
estatisticas = df.describe()

print(estatisticas)

           Idade
count   5.000000
mean   44.400000
std    27.134848
min    14.000000
25%    28.000000
50%    34.000000
75%    71.000000
max    75.000000

#Calculando a média das idades
media_idade = idade.mean()

print(media_idade)

44.4



# ÍNDICES DO DATAFRAMES:
#Explicação sobre o conceito de índices e como eles são usados no Pandas. 
#Acesso a valores específicos usando índices e labels de colunas. Renomeando índices com o método
#rename(). Excluindo índices usando drop().


# Acessando valores específicos usando o índice
valor_ricardo = df.loc['Ricardo', 'Idade']

print(valor_ricardo)

34

# Renomeando um índice
df.rename(index={'Ricardo': 'Richard'}, inplace=True)

print(df.rename)

Nome          
Richard     34
Celia       71
Joao        75
Leandro     14
Fabio       28

# Excluindo um índice
df.drop('Richard', inplace=True)

print(df.drop)

Nome          
Celia       71
Joao        75
Leandro     14
Fabio       28



# EXIBIÇÃO E MANIPULAÇÃO DE COLUNAS:

#Acessando colunas por nome.
idades = df['Idade']

print(idades)

Name: Idade, dtype: int64

#Realizando slices de intervalos
intervalo = df[1:5]

print(intervalo)

Nome     Idade  
Joao        75
Leandro     14
Fabio       28


# LIDANDO COM DADOS AUSENTES E NULOS:

#Identificação de valores nulos usando isna().
#Preenchimento com fillna().
#Criando um DataFrame com dados ausentes
dados = {'Nome': ['Ricardo', 'Celia', 'Joao', 'Leandro', 'Fabio'],
         'Idade': [None, 71, 75, 14, 28]}
df_ausente = pd.DataFrame(dados)

print(df_ausente)

      Nome  Idade
0  Ricardo    NaN
1    Celia   71.0
2     Joao   75.0
3  Leandro   14.0
4    Fabio   28.0

#Verificando valores nulos
valores_nulos = df_ausente.isna()

print(valores_nulos)

    Nome  Idade
0  False   True
1  False  False
2  False  False
3  False  False
4  False  False

#Preenchendo valores nulos com a média
df_ausente['Idade'].fillna(df_ausente['Idade'].mean(), inplace=True)

print(df_ausente)

      Nome  Idade
0  Ricardo   47.0
1    Celia   71.0
2     Joao   75.0
3  Leandro   14.0
4    Fabio   28.0



# Operações com Colunas e Transformações
#Adição de novas colunas baseadas em operações com colunas existentes. Aplicação de
#funções a elementos de uma coluna usando apply(). Realização de operações vetorizadas
#entre colunas.


#Aplicando uma função a uma coluna
def classificar_idade(idade):
    if idade <30:
        return 'Jovem'
    else: 
        return 'Adulto'

df['Classificação'] = df['Idade'].apply(classificar_idade)

print(df)

      Nome  Idade Classifica��o
0  Ricardo     34        Adulto
1    Celia     71        Adulto
2     Joao     75        Adulto
3  Leandro     14         Jovem
4    Fabio     28         Jovem

#Realizando uma operação vetorizada
df['Idade_dobrada'] = df['Idade'] * 2

print(df)
         
Nome     Idade  Idade_quadrado Classifica��o  Idade_dobrada                                                 
Celia       71            5041        Adulto            142
Joao        75            5625        Adulto            150
Leandro     14             196         Jovem             28
Fabio       28             784         Jovem             56
