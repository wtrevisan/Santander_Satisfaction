# ************************************* Machine Learning Library For Data Science (Versão 01) *************************************
# Neste arquivo estão definidas algumas funções de "Machine Learning" para serem utilizadas em Data Science.
#

# ************************************* Importando Pacotes e/ou Funções *************************************
#
# Importa o pacote "NumPy":
import numpy as np
# Importa o pacote "Pandas":
import pandas as pd

# Importa a função "time" do pacote "time":
from time import time

# Importa o pacote "os" (Operation System with its Packages and Functions)
import os

# O pacote "sys" permite manipulações com o sistema operacional:
import sys

# Importa a função "Image" do pacote "IPython.display":
from IPython.display import Image

# Importa o pacote "pyplot" do "matplotlib":
import matplotlib.pyplot as plt
# Importa o pacote "seaborn"
import seaborn as sns

# Imports para "Avaliação do Modelo":
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

# Funções de pré-processamento do "Scikit-Learn":
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer

# Path: onde estão armazenadas as classes e funções que serão utilizadas neste módulo:
LIB_PATH = os.path.join(".")

# Adicionando o diretório ao 'path' do Sistema, para podermos importar classes e funções que serão
# utilizadas neste módulo:
sys.path.append(LIB_PATH)

# Importando para este notebook, as classes e funções definidas no módulo "DataScience_Plot_Library_v1_0":
import DataScience_Plot_Library_v1_0 as ptlib

# ************************************* Definindo Funções *************************************
#
# ***** Função para fazermos a "transformação de escala" de uma feature:
#
def scalers_transform(df, feature):
    '''
    Input:
        "df": Dataframe com os dados.
        "feature": Feature onde aplicaremos os "escalers".

    Output:
        "feat_df": Data frame com os dados transformados.
    '''
    # Código da função:

    # Criando as instâncias dos "escalers":

    # Standard Scaler (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
    sts = StandardScaler()

    # Min-Max Scaler (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
    mms = MinMaxScaler()

    # Robust Scaler (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
    rs = RobustScaler()

    # Power Transformer (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)
    pt = PowerTransformer()

    # Quantile Transformer (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
    qt = QuantileTransformer(output_distribution='normal', random_state=42)

    # Criando um dicionário com os dados transformados:
    feat_transform = {'sts': sts.fit_transform(df[feature].values.reshape(-1, 1)),
                      'mms': mms.fit_transform(df[feature].values.reshape(-1, 1)),
                      'rs': rs.fit_transform(df[feature].values.reshape(-1, 1)),
                      'pt': pt.fit_transform(df[feature].values.reshape(-1, 1)),
                      'qt': qt.fit_transform(df[feature].values.reshape(-1, 1))
                     }
    
    # Criando um data frame para armazenarmos as transformações da 'feature':
    feat_df = df[[feature]].copy()

    feat_df[feature + '_sts'] = feat_transform['sts']
    feat_df[feature + '_mms'] = feat_transform['mms']
    feat_df[feature + '_rs'] = feat_transform['rs']
    feat_df[feature + '_pt'] = feat_transform['pt']
    feat_df[feature + '_qt'] = feat_transform['qt']
        
    return feat_df

# ***** Função para mostrar os resultados das pontuações (Scores) da validação cruzada (Cross Validation).
#
def display_scores(scores, decimals=4):
    '''
    Input:
        "scores": pontuações (scores) calculados de um processo de validação cruzada.
        "decimals": número de dígitos decimais para apresentação dos resultados.

    Output: None
    '''
    # Código da função:

    print("Scores:", len(scores))
    print(np.round(scores, decimals=decimals))
    print("Mean:", np.round(scores.mean(), decimals=decimals)) 
    print("Standard deviation:", np.round(scores.std(), decimals=decimals))

# ***** Fução para mostrar os melhores resultados encontrados para os hiperparâmetros do modelo:
#
def best_results_report (estimator, title):
    '''
    Input:
        "estimator": modelo de machine learning que já foi treinado (fit).
        "title": título do relatório.

    Output: None
    '''
    # Código da função:

    # Mostra o título do relatório:
    print(title)
    
    # Mostra a melhor seleção de hiperparâmetros:
    print('Best params:', estimator.best_params_)

    # Mostra o melhor estimador:
    print('Best estimator:', estimator.best_estimator_)

    # Mostra o melhor score:
    print('Best score:', np.round(estimator.best_score_, decimals=4))

# ***** Função para calcularmos as métricas de classificação de um modelo de "Machine Learning":
#
def classif_metrics (y_real, y_pred, metric='All'):
    '''
    Input:
        "y_real": dados "reais" da nossa variável target.
        "y_pred": dados "preditos" da nossa variável target.
        "metric": define as métricas que serão calculadas e mostradas.

    Output: None
    '''
    # Código da função:

    # Calculando a acurácia:
    accuracy = accuracy_score(y_real, y_pred)
    
    # Calculando a precisão:
    precision = precision_score(y_real, y_pred)
    
    # Calculando a revocação:
    recall = recall_score(y_real, y_pred)

    # Calculando a pontuação F1:
    F1_score = f1_score(y_real, y_pred)
    
    if (metric == 'All'):
        print ("Accuracy = %.4f" %(accuracy))
        print ("Precision = %.4f" %(precision))
        print ("Recall = %.4f" %(recall))
        print ("f1-score = %.4f" %(F1_score))
        return (accuracy, precision, recall, F1_score)

    if (metric == 'Accuracy'):
        print ("Accuracy = %.4f" %(accuracy))
        return (accuracy)

    if (metric == 'Precision'):
        print ("Precision = %.4f" %(precision))
        return (precision)

    if (metric == 'Recall'):
        print ("Recall = %.4f" %(recall))
        return (recall)

    if (metric == 'f1-score'):
        print ("f1-score = %.4f" %(F1_score))
        return (F1_score)

