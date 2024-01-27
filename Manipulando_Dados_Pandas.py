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



# Series: DataFrames Unidimensionais
# Entendendo o conceito de Series: estrutura unidimensional semelhante a um array ou
# coluna de uma planilha.
# Series são estruturas unidimensionais que armazenam dados, semelhantes a colunas de uma planilha. 
# Elas são frequentemente usadas para representar uma única variável.

#Criando uma series a partir de uma lista
idade = pd.Series([34, 71, 75, 14, 28])

print(idade)

#Acessando elementos de uma Series
primeira_idade = idade[0]

print(primeira_idade)


# OPERAÇÕES BÁSICAS COM DATAFRAMES E SERIES:
#Compreensão dos tipos de dados (dtypes) em um DataFrame. Uso do método describe()
#para obter estatísticas descritivas. Aplicação de funções básicas como mean(), sum() e outras em colunas.

#Verificando os tipos de dados das colunas
tipos_de_dados = df.dtypes
print(tipos_de_dados)

#Obtendo estatísticas descritivas
estatisticas = df.describe()
print(estatisticas)

#Calculando a média das idades
media_idade = idade.mean()
print(media_idade)



# ÍNDICES DO DATAFRAMES:
#Explicação sobre o conceito de índices e como eles são usados no Pandas. 
#Acesso a valores específicos usando índices e labels de colunas. Renomeando índices com o método
#rename(). Excluindo índices usando drop().

# Definindo um índice personalizado
df.set_index('Nome', inplace=True)
print(df.set_index)

# Acessando valores específicos usando o índice
valor_ricardo = df.loc['Ricardo', 'Idade']
print(valor_ricardo)

# Renomeando um índice
df.rename(index={'Ricardo': 'Richard'}, inplace=True)
print(df.rename)

# Excluindo um índice
df.drop('Richard', inplace=True)
print(df.drop)



# EXIBIÇÃO E MANIPULAÇÃO DE COLUNAS:

#Acessando colunas por nome.
idades = df['Idade']
print(idades)

#Realizando slices de intervalos
intervalo = df[1:5]

print(intervalo)



# LIDANDO COM DADOS AUSENTES E NULOS:

#Identificação de valores nulos usando isna().
#Preenchimento com fillna().
#Criando um DataFrame com dados ausentes
dados = {'Nome': ['Ricardo', 'Celia', 'Joao', 'Leandro', 'Fabio'],
         'Idade': [None, 71, 75, 14, 28]}
df_ausente = pd.DataFrame(dados)
print(df_ausente)

#Verificando valores nulos
valores_nulos = df_ausente.isna()
print(valores_nulos)

#Preenchendo valores nulos com a média
df_ausente['Idade'].fillna(df_ausente['Idade'].mean(), inplace=True)
print(df_ausente)



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

#Realizando uma operação vetorizada
df['Idade_dobrada'] = df['Idade'] * 2
print(df)