# ************************************* DSA - Project 03 Library (Versão 1.0) *************************************
# Neste arquivo estão definidas algumas funções utilizadas no "Projeto 03" da DSA (Data Science Academy).
#

# ************************************* Importando Pacotes ou Funções *************************************
#
# Importa o pacote "numpy":
#import numpy as np

# Importa o pacote "pandas":
import pandas as pd

# Importa pacote com funções do Sistema Operacional:
import os

# O pacote "sys" permite manipulações com o sistema operacional:
import sys

# Importa função para extrair arquivos compactados no formato "zip":
from zipfile import ZipFile

# Importa o pacote "re" para trabalharmos as Expressões Regulares:
import re

# Importa o pacote "pyplot" do "matplotlib":
import matplotlib.pyplot as plt
# Importa o pacote "seaborn"
import seaborn as sns

# Path: onde estão armazenadas as classes e funções que serão utilizadas neste módulo:
LIB_PATH = os.path.join(".")

# Adicionando o diretório ao 'path' do Sistema, para podermos importar classes e funções que serão
# utilizadas neste módulo:
sys.path.append(LIB_PATH)

# Importando para este notebook, as classes e funções definidas no módulo "DataScience_Library_v1_0":
import DataScience_Library_v1_0 as dslib

# ************************************* Definindo Funções *************************************
#
# ***** Função para extrair todos os arquivos compactados em "train.zip".
#
# Define o path onde será salvo o dataset deste projeto:
SANTANDER_PATH = os.path.join("..", "Datasets")
# Define o nome completo do arquivo compactado (zip) para obtermos o dataset:
SANTANDER_ZIP_FILE = "train.csv.zip"

# Definindo a função que extrairá todos os arquivos compactados em "train.zip",
# no diretório definido em "SANTANDER_PATH".
# Este arquivo compactado definido em "SANTANDER_ZIP_FILE" contém todos os dados do nosso projeto.
def fetch_santander_dataset(santander_path=SANTANDER_PATH, santander_zip_file=SANTANDER_ZIP_FILE):
    '''
    Input:
        "santander_path": diretório (path) onde está armazenado o arquivo compactado que contém o nosso dataset.
        "santander_zip_file": nome do arquivo compactado que contém o nosso dataset.
        
    Output: None
    '''
    # Código da função:
        
    # Define o path completo onde está salvo o arquivo compactado definido em "santander_zip_file":
    zip_path = os.path.join(santander_path, santander_zip_file)
    
    # Cria uma instância da classe "ZipFile":
    santander_zip = ZipFile(file=zip_path)
    
    # Extrai todos os arquivos, salvando no diretório definido no parâmetro "santander_path":
    santander_zip.extractall(path=santander_path)
    
    # Fecha o arquivo compactado:
    santander_zip.close()
    
    # Lista os arquivos que foram descompactados em nosso diretório de trabalho:
    files_and_folders = os.listdir(path=santander_path)
    print("Files and Folders:")
    _=[print(file) for file in files_and_folders]

# ***** Função para carregar (load) o dataset do projeto.
#
# Define o path onde está salvo o dataset deste projeto:
SANTANDER_PATH = os.path.join("..", "Datasets")
# Define o nome do arquivo do nosso dataset:
SANTANDER_FILE = "train.csv"

# Definindo a função que fará a leitura do nosso dataset ("SANTANDER_FILE").
def load_santander_dataset(santander_path=SANTANDER_PATH, santander_file=SANTANDER_FILE):
    '''
    Input:
        "santander_path": diretório (path) onde está armazenado o nosso dataset.
        "santander_file": nome do arquivo onde está armazenado os dados do nosso dataset.
        
    Output:
        "df": dataframe com os dados do nosso dataset carregado.
    '''
    # Código da função:
    
    # Define o path completo onde está salvo o nosso dataset:
    file_path = os.path.join(santander_path, santander_file)
    
    # Criando uma instância para medirmos o tempo decorrido para carga (load) do nosso dataset:
    load_file_time = dslib.ElapsedTime(builder_msg=False)
    
    # Iniciando a contagem do tempo de leitura do dataset:
    msg = "Loading file: " + file_path # message of process.
    load_file_time.start(msg=msg)

    # Faz a leitura do dataset, armazenando os dados em um objeto dataframe (df):
    df = dslib.load_dataset(file_path=file_path, index_col=None, low_memory=False)

    # Alterando o nome da nossa variável target: De "TARGET" para "Satisfaction":
    df.rename(columns={'TARGET':'Satisfaction'}, inplace=True)
    print('The label "TARGET" has been replaced by the label "Satisfaction"')

    # Calculando o tempo decorrido da leitura do arquivo:
    load_file_time.end()

    # Eliminando da memória o objeto criado para contagem do tempo decorrido:
    del(load_file_time)

    return (df)

# ***** Função para carregar (load) o dataset de testes do kaggle.
#
# Define o path onde está salvo o dataset deste projeto:
KAGGLE_TEST_PATH = os.path.join("..", "Datasets")
# Define o nome do arquivo do nosso dataset:
KAGGLE_TEST_FILE = "test.csv"

# Definindo a função que fará a leitura do nosso dataset ("KAGGLE_TEST_FILE").
def load_test_dataset_kaggle(kaggle_test_path=KAGGLE_TEST_PATH, kaggle_test_file=KAGGLE_TEST_FILE):
    '''
    Input:
        "kaggle_test_path": diretório (path) onde está armazenado o nosso dataset de testes do kaggle.
        "kaggle_test_file": nome do arquivo onde está armazenado os dados do nosso dataset de testes do kaggle.
        
    Output:
        "df": dataframe com os dados do nosso dataset carregado.
    '''
    # Código da função:
    
    # Define o path completo onde está salvo o nosso dataset:
    file_path = os.path.join(kaggle_test_path, kaggle_test_file)
    
    # Criando uma instância para medirmos o tempo decorrido para carga (load) do nosso dataset:
    load_file_time = dslib.ElapsedTime(builder_msg=False)
    
    # Iniciando a contagem do tempo de leitura do dataset:
    msg = "Loading file: " + file_path # message of process.
    load_file_time.start(msg=msg)

    # Faz a leitura do dataset, armazenando os dados em um objeto dataframe (df):
    df = dslib.load_dataset(file_path=file_path, index_col=None, low_memory=False)

    # Alterando o nome da nossa variável target: De "TARGET" para "Satisfaction":
    df.rename(columns={'TARGET':'Satisfaction'}, inplace=True)
    print('The label "TARGET" has been replaced by the label "Satisfaction"')

    # Calculando o tempo decorrido da leitura do arquivo:
    load_file_time.end()

    # Eliminando da memória o objeto criado para contagem do tempo decorrido:
    del(load_file_time)

    return (df)

# ***** Função para carregar (load) o dataset de treino do projeto.
#
# Define o path onde está salvo o dataset de treinamento deste projeto:
SANTANDER_TRAIN_PATH = os.path.join(".", "Data")
# Define o nome do arquivo do nosso dataset de treinamento:
SANTANDER_TRAIN_FILE = "santander_train.csv"

# Definindo a função que fará a leitura do nosso dataset de treinamento ("SANTANDER_TRAIN_FILE").
def load_santander_train_dataset(santander_train_path=SANTANDER_TRAIN_PATH, santander_train_file=SANTANDER_TRAIN_FILE):
    '''
    Input:
        "santander_train_path": diretório (path) onde está armazenado o nosso dataset de treinamento.
        "santander_train_file": nome do arquivo onde está armazenado os dados do nosso dataset de treinamento.
        
    Output:
        "df": dataframe com os dados do nosso dataset carregado.
    '''
    # Código da função:
    
    # Define o path completo onde está salvo o nosso dataset de treinamento:
    file_path = os.path.join(santander_train_path, santander_train_file)
    
    # Criando uma instância para medirmos o tempo decorrido para carga (load) do nosso dataset de treinamento:
    load_file_time = dslib.ElapsedTime(builder_msg=False)
    
    # Iniciando a contagem do tempo de leitura do dataset de treinamento:
    msg = "Loading file: " + file_path # message of process.
    load_file_time.start(msg=msg)

    # Faz a leitura do dataset de treinamento, armazenando os dados em um objeto dataframe (df):
    df = dslib.load_dataset(file_path=file_path, index_col=None, low_memory=False)

    # Calculando o tempo decorrido da leitura do arquivo:
    load_file_time.end()

    # Eliminando da memória o objeto criado para contagem do tempo decorrido:
    del(load_file_time)

    return (df)

# ***** Função para carregar (load) o dataset de teste do projeto.
#
# Define o path onde está salvo o dataset de teste deste projeto:
SANTANDER_TEST_PATH = os.path.join(".", "Data")
# Define o nome do arquivo do nosso dataset de teste:
SANTANDER_TEST_FILE = "santander_test.csv"

# Definindo a função que fará a leitura do nosso dataset de teste ("SANTANDER_TEST_FILE").
def load_santander_test_dataset(santander_test_path=SANTANDER_TEST_PATH, santander_test_file=SANTANDER_TEST_FILE):
    '''
    Input:
        "santander_test_path": diretório (path) onde está armazenado o nosso dataset de teste.
        "santander_test_file": nome do arquivo onde está armazenado os dados do nosso dataset de teste.
        
    Output:
        "df": dataframe com os dados do nosso dataset carregado.
    '''
    # Código da função:
    
    # Define o path completo onde está salvo o nosso dataset de teste:
    file_path = os.path.join(santander_test_path, santander_test_file)
    
    # Criando uma instância para medirmos o tempo decorrido para carga (load) do nosso dataset de teste:
    load_file_time = dslib.ElapsedTime(builder_msg=False)
    
    # Iniciando a contagem do tempo de leitura do dataset de teste:
    msg = "Loading file: " + file_path # message of process.
    load_file_time.start(msg=msg)

    # Faz a leitura do dataset de teste, armazenando os dados em um objeto dataframe (df):
    df = dslib.load_dataset(file_path=file_path, index_col=None, low_memory=False)

    # Calculando o tempo decorrido da leitura do arquivo:
    load_file_time.end()

    # Eliminando da memória o objeto criado para contagem do tempo decorrido:
    del(load_file_time)

    return (df)

# ***** Função para obter o número de tipos de variáveis no padrão "var" + "num":
# ***** "var1", "var15", "var36", etc.:
#
def get_vars_type(features):
    '''
    Input:
        "features": lista com os nomes das variáveis do dataset.
    
    Output:
        "vars_num": lista ordenada dos números de cada variável.
    '''
    # Código da função:
    
    # Primeiro vamos separar as palavras de cada variável utilizando o caracter padrão '_':
    pattern = '_'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    # Cria uma lista vazia para armazenar os tipos de variáveis.
    vars_type = list()
    # Loop for para criar a lista dos tipos de variáveis:
    for feat in features:
        split_feat = regex.split(feat)
        for v in split_feat:
            if ('var' in str.lower(v)):
                if (v not in vars_type):
                    vars_type.append(v)
                    
    # Agora, vamos separar os números de cada variável, armazenando-os de forma ordenada em uma lista.
    # Para isso, vamos separar tudo que não for dígito, utilizando o padrão "\\D":
    pattern = '\\D'
    regex = re.compile(pattern, flags=re.IGNORECASE)

    # Cria uma lista vazia para armazenar cada número dos tipos de variáveis.
    vars_num_str = list()

    # Loop for para criar a lista dos tipos de variáveis (números):
    for var in vars_type:
        split_var = regex.split(var)
        for v in split_var:
            if (v not in vars_type):
                vars_num_str.append(v)
                
    # Em seguida, vamos cria a lista ordenada dos números de cada variável:
    vars_num = list()

    for v in vars_num_str:
        if (v != ''):
            num = int(v)
            if (num not in vars_num):
                vars_num.append(num)

    # Retorna a lista ordenada dos números de cada variável:
    return (sorted(vars_num))

# ***** Função para obter as informações (features) agrupadas para cada tipo de variável no padrão:
# ***** "var" + "num": "var1", "var15", "var36", etc.
# ***** Exemplo de um dicionário agrupando as features por tipo de variável:
# ***** {'var1': ['feat1', 'feat3']
# ***** {'var9': ['feat5', 'feat12']
#
def get_features_groupby_vars(features):
    '''
    Input:
        "features": lista com os nomes das variáveis do dataset.
    
    Output:
        "vars_features": dicionário de dados com as features agrupadas para cada tipo de variável.
    '''
    # Código da função:

    # Primeiro vamos obter de forma ordenada os tipos de variáveis:
    vars_num = get_vars_type(features)
    
    # Agora, vamos criar um dicionário de dados para armazenar as informações de cada tipo de variável:
    vars_features = dict()
    for num in vars_num:
        vars_features['var' + str(num)] = list()
    
    # Em seguida, vamos criar um loop para buscar as informações de cada tipo de variável.
    # Primeiro vamos definir um padrão ('_') para separar as palavras de cada feature:
    pattern = '_'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    
    # Loop para varrer o dicionário "vars_type": fe
    for k in vars_features:
        # Loop for para criar a lista de features para cada tipo de variável:
        for feat in features:
            split_feat = regex.split(feat)
            for word in split_feat:
                if (k == word):
                    vars_features[k].append(feat)
                    
    # Retorna o dicionário de dados com as informações das features separadas de cada variável:
    return (vars_features)    

# ***** Função para agrupar os tipos de variáveis do dataset, por quantidade (contagem) de features.
# ***** Exemplo de um dicionário agrupando as variáveis por quantidade (contagem) de features:
# ***** {'Feat_1': ['var1', 'var2']
# ***** {'Feat_2': ['var5', 'var8']
#
def get_vars_groupby_featcount(features):
    '''
    Input:
        "features": lista com os nomes das variáveis do dataset.
    
    Output:
        "vars_groupby_featcount": dicionário de dados com as variáveis agrupadas por quantidade de features.
    '''
    # Código da função:

    # Primeiro, vamos obter um dicionário com a relação
    # de features agrupadas por cada tipo de variável:
    feat_groupby_vars = get_features_groupby_vars(features)
    
    # Agora, vamos criar uma lista com a contagem de features
    # relacionadas a cada tipo de variável do nosso dataset:
    feat_count = sorted([len(v) for v in feat_groupby_vars.values()]) # Classificando em ordem crescente.
    # Criando um array com as contagens únicas:
    feat_count = pd.Series(feat_count).unique()
    
    # Agora, vamos criar um dicionário de dados para armazenar as variáveis agrupadas
    # de acordo com a quantidade (contagem) de features:
    vars_groupby_featcount = dict()
    for fct in feat_count:
        vars_groupby_featcount['Feat_' + str(fct)] = list()
    
    # Agora, vamos fazer um Loop para salvar as variáveis agrupadas
    # de acordo com a quantidade (contagem) de features:
    for k, v in feat_groupby_vars.items():
        # Faz a contagem das features da variável "k":
        count = len(v) 
        
        # Armazena a variável no dicionário "vars_groupby_featcount" de acordo
        # com a sua quantidade de features:
        vars_groupby_featcount['Feat_' + str(count)].append(k)
        
    # Retorna o dicionário de dados com as variáveis agrupadas
    # de acordo com a quantidade (contagem) de features:
    return (vars_groupby_featcount)

# ***** Função para agrupar as features do dataset que possuem um mesmo padrão definido em seu nome.
# ***** Exemplos:
# ***** Features que possuem o prefixo 'ind_': ['ind_var1', 'ind_var2']
# ***** Features que possuem o prefixo 'num_': ['num_var1', 'num_var2']
#
def get_pattern_features(prefix=None, pos=0, features=None):
    '''
    Input:
        "prefix": prefixo definido para encontrar as features.
        "pos": posição do prefixo na lista de palavras de cada feature.
        "features": lista com os nomes das variáveis do dataset.
    
    Output:
        "prefix_feature": dicionário de dados com as variáveis agrupadas por quantidade de features.
    '''
    # Código da função:

    # Verifica se foram passados os parâmetros de forma correta:
    if (type(prefix) != str):
        # Erro:
        print("prefix is not a 'str'!")
        return (list()) # retorna um lista vazia.

    if (type(features) != list):
        # Erro:
        print("features is not a 'list'!")
        return (list()) # retorna um lista vazia.

    # Inicializa a lista das features que possuem o mesmo padrão no seu nome:
    prefix_feature = []

    # Cria o objeto de "re":
    pattern = '_'
    regex = re.compile(pattern, flags=re.IGNORECASE)

    # Loop for para procurar as features:
    for feat in features:
        # Separa as palavras do nome da feature:
        split_feat = regex.split(feat)

        # Verifica se a feature possui o "prefixo" na posição desejada:
        if (len(split_feat) > pos):
            if (prefix == split_feat[pos]):
                # Se possui, anexa o nome da feature na lista:
                prefix_feature.append(feat)

    return (prefix_feature)
