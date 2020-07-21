# ************************************* Data Science Library (Versão 1.0) *************************************
# Neste arquivo estão definidas algumas funções (uso geral) para serem utilizadas em Data Science.
#

# ************************************* Importando Pacotes ou Funções *************************************
#
# Importa o pacote "os" Operation System (Packages and Functions):
import os

# Importa o pacote  "numpy":
import numpy as np

# Importa o pacote  "pandas":
import pandas as pd

# Importa o pacote "pickle" para salvar/carregar objetos:
import pickle

# Importa o pacote "time":
import time

# Importa o pacote "pyplot" do "matplotlib":
import matplotlib.pyplot as plt

# Importa a função "Image" do pacote "IPython.display":
from IPython.display import Image

# ************************************* Definindo Classes *************************************
#
#  ***** Classe para calcular o tempo decorrido de um processo/atividade qualquer:
#
class ElapsedTime():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__, e ele é chamado de "Construtor", porque é ele que inicializa os objetos desta classe.
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self, builder_msg=True, display=True):
        
        # Atributos de cada objeto criado a partir desta classe. 
        # O self indica que estes são atributos dos objetos.
        self.display = display # Define se queremos mostrar a mensagem do tempo decorrido.
        self.start_time = 0 # Começa a contagem do tempo.
        self.end_time = 0 # Termina a contagem do tempo.
        self.elapsed_time = 0 # Calcula o tempo decorrido.
        if (builder_msg):
            print("Builder called to create an object of class ElapsedTime!")
        
    # Métodos são funções, que recebem como parâmetro atributos do objeto criado.
    # Método para iniciar a contagem do tempo:
    def start (self, msg=None):
        if (msg != None):
            print(msg) # Print message!
        
        self.start_time = time.perf_counter()

    # Método para terminar a contagem do tempo e imprimir o tempo decorrido se for desejado:
    def end (self, msg=None):
        # Calcula o tempo decorrido:
        self.end_time = time.perf_counter()
        self.elapsed_time = np.round((self.end_time - self.start_time), decimals=2)

        if (msg != None):
            msg_str = msg
        else:
            msg_str = "Elapsed time:"
                
        if (self.display == True):
            if (self.elapsed_time == 1):
                print("%s 1 second." % (msg_str))
            elif (self.elapsed_time == 60):
                print("%s 1 minute." % (msg_str))
            elif (self.elapsed_time == 60*60):
                print("%s 1 hour." % (msg_str))
            elif (self.elapsed_time == 60*60*24):
                print("%s 1 day." % (msg_str))
            elif (self.elapsed_time < 60):
                print("%s %.2f seconds." % (msg_str, self.elapsed_time))
            elif (self.elapsed_time < 60*60):
                print("%s %.2f minutes." % (msg_str, self.elapsed_time/60))
            elif (self.elapsed_time < 60*60*24):
                print("%s %.2f hours." % (msg_str, self.elapsed_time/(60*60)))
            else:
                print("%s %.2f days." % (msg_str, self.elapsed_time/(60*60*24)))

    # Método para obter a contagem do tempo:
    def get (self):
        return self.elapsed_time

#  ***** Classe para armazenar informações sobre as variáveis preditoras (features) de um dataset:
#  ***** As features do dataset serão classificadas e armazenadas em "chaves" específicas.
#
class FeaturesInformations():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__, e ele é chamado de "Construtor", porque é ele que inicializa os objetos desta classe.
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self, builder_msg=True, keys=None):
        
        # Atributos de cada objeto criado a partir desta classe. 
        # O self indica que estes são atributos dos objetos.
        
        # Cria um dicionário vazio onde serão armazenadas os nomes das features,
        # classificadas em algumas informações específicas:
        self.feat_info = dict()

        if (keys != None):
            # Cria as chaves do nosso dicionário:
            for k in keys:
                # Para a chave 'k' cria uma lista vazia de valores:
                self.feat_info[k] = list()

        if (builder_msg):
            print("Builder called to create an object of class FeaturesInformations!")

        print(self.feat_info.keys())

    # Métodos são funções, que recebem como parâmetro atributos do objeto criado.
    # Método para inserir uma nova chave (informação) em nosso dicionário:
    def insert (self, key):
        # Para a chave 'key' cria uma lista vazia de valores:
        self.feat_info[key] = list()

    # Método para salvar os nomes das features em uma chave (informação) específica:
    def save (self, key, features):
        # Para a chave 'key' inclui (anexa) uma lista de features:
        for feat in features:
            self.feat_info[key].append(feat)

    # Método para retornar a contagem total de features nas chaves desejadas:
    def count (self, keys):
        total = 0
        for k in keys:
            total += len(self.feat_info[k])

        # Retorna a contagem total:
        return total

    # Método para retornar os valores de uma chave:
    def get (self, key, default=None):
        return self.feat_info.get(key, default)

    # Método para retornar as chaves (Informações) do dicionário:
    def keys (self):
        return self.feat_info.keys()

    # Método para retornar os itens (chaves e valores) do dicionário:
    def items (self):
        return self.feat_info.items()

    # Método para retornar todos os valores do dicionário:
    def values (self):
        return self.feat_info.values()

    # Método para limpar (remover) todas as chaves (Informações) e valores (nomes das features),
    # do dicionário, ou seja, neste caso teremos "all=True", ou então removerá os valores
    # (nomes das features) de uma chave (Informação) específica.
    # Neste caso deveremos ter "all=False" e "keys != None":
    def clear (self, keys=None, all=True):
        # Verificando se vamos limpar todas as chaves e valores do dicionário:
        if (all == True):
            self.feat_info.clear()
        else:
            # Verificando se alguma chave (Informação) foi definida:
            if (keys == None):
                print("Information (keys)) not found!")
            else:
                # Remove os valores (nome das features) das chaves (informações)
                # do dicionário, definidas em 'keys':
                for k in keys:
                    self.feat_info[k].clear()

    # Método para remover valores de uma chave específica do dicionário:
    def remove (self, key, values, msg=False):
        for v in values:
            if v in self.feat_info[key]:
                self.feat_info[key].remove(v)
            else:
                if (msg == True):
                    print("Item {} not found!".format(v))

    # Método para classificar os valores das chaves do dicionário:
    def sort (self, keys=None, key=None, reverse=False):
        if (keys == None):
            # Classificamos todas as chaves do dicionário:
            for k in self.feat_info.keys():
                self.feat_info[k].sort(key=key, reverse=reverse)
        else:
            # Classificamos os valores definidos em "keys":
            for k in keys:
                self.feat_info[k].sort(key=key, reverse=reverse)

#  ***** Classe para armazenar os "Outliers" (Valores Extremos/Discrepantes) sobre as variáveis preditoras (features) de um dataset:
#  ***** Os nomes das features serão as chaves do dicionário e os valores serão os "Outliers" encontrados, armazenados
#  ***** em um objeto "Series" do "Pandas".
#
class OutliersByFeatures():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__, e ele é chamado de "Construtor", porque é ele que inicializa os objetos desta classe.
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self, builder_msg=True, features=None):
        
        # Atributos de cada objeto criado a partir desta classe. 
        # O self indica que estes são atributos dos objetos.
        
        # Cria um dicionário vazio onde as chaves são os nomes de cada feature informada no parâmetro
        # "features". Para cada feature será criado um objeto "Series" do Pandas, inicialmente "vazio".
        self.outliers = dict()

        if (features != None):
            # Cria as chaves do nosso dicionário:
            for feat in features:
                # Para cada 'feat' cria um objeto "Series" do pandas, vazio:
                self.outliers[feat] = pd.Series()

        if (builder_msg):
            print("Builder called to create an object of class OutliersByFeatures!")

        print(self.outliers.keys())

    # Métodos são funções, que recebem como parâmetro atributos do objeto criado.
    # Método para inserir uma nova "feature" (chave) em nosso dicionário:
    def insert (self, feature):
        # Para a chave 'feature' cria um objeto "Series" do pandas, vazio:
        self.outliers[feature] = pd.Series()

    # Método para salvar os nomes das features em uma chave (informação) específica:
    def save (self, feature, outliers):
        # Para a 'feature' cria uma nova chave no dicionário (se não existir)
        # e armazena (salva) os 'outliers' (Objeto Series):
        
        # Verifica se a feature existe no dicionário:
        if (feature in self.outliers.keys()):
            # Concatena (append) os outliers:
            self.outliers[feature].append(outliers)
        else:
            # Cria uma nova feature (chave) no dicionário e armazena
            # os outliers.
            self.outliers[feature] = outliers

    # Método para retornar a contagem total de todos os 'outliers' (todas as features),
    # ou seja, neste caso teremos "all=True", ou então retornará a contagem dos outliers
    # de uma 'feature' específica. Neste caso deveremos ter "all=False" e "feature != None":
    def count (self, feature=None, all=True):
        # Verificando se a contagem dos outliers é geral (todas as features):
        if (all == True):
            total = 0
            for feat in self.outliers.keys():
                total += self.outliers[feat].count()

            # Retorna a contagem total de outliers:
            return total
        else:
            # Verificando se a feature foi informada:
            if (feature == None):
                print("Feature not found!")
                return np.nan
            else:
                # Retorna a contagem de outiers da feature:
                return self.outliers[feature].count()

    # Método para retornar os outliers de uma feature:
    def get (self, feature, default=None):
        return self.outliers.get(feature, default)

    # Método para retornar as chaves (Features) do dicionário:
    def keys (self):
        return self.outliers.keys()

    # Método para retornar os itens (features e outliers) do dicionário:
    def items (self):
        return self.outliers.items()

    # Método para retornar todos os outliers do dicionário:
    def values (self):
        return self.outliers.values()

    # Método para limpar (remover) todas as features (e os seus 'outliers'),
    # do dicionário, ou seja, neste caso teremos "all=True", ou então removerá
    # uma 'feature' específica (e os seus 'outliers').
    # Neste caso deveremos ter "all=False" e "feature != None":
    def clear (self, feature=None, all=True):
        # Verificando se vamos limpar todas as features do dicionário:
        if (all == True):
            self.outliers.clear()
        else:
            # Verificando se a feature foi informada:
            if (feature == None):
                print("Feature not found!")
            else:
                # Remove a 'feature' e os seus outliers do dicionário:
                del(self.outliers[feature])

    # Método para limpar (remover) todos os outliers (de todas as features),
    # do dicionário, ou seja, neste caso teremos "all=True", ou então removerá
    # todos os outliers de uma 'feature' específica.
    # Neste caso deveremos ter "all=False" e "feature != None":
    def drop (self, feature=None, all=True):
        # Verificando se vamos remover todos os outliers de todas as features do dicionário:
        if (all == True):
            for feat in self.outliers.keys():
                self.outliers[feat].drop(index=feat, inplace=True)
        else:
            # Verificando se a feature foi informada:
            if (feature == None):
                print("Feature not found!")
            else:
                # Remove os outliers da 'feature':
                self.outliers[feature].drop(index=feature, inplace=True)

    # Método para classificar os outliers de todas as features do dicionário, ou seja,
    # neste caso teremos "all=True", ou então classificará os os outliers de uma 'feature' específica.
    # Neste caso deveremos ter "all=False" e "feature != None":
    def sort (self, feature=None, all=True, ascending=True):
        # Verificando se vamos classificar todos os outliers de todas as features do dicionário:
        if (all == True):
            for feat in self.outliers.keys():
                self.outliers[feat].sort_values(ascending=ascending, inplace=True)
        else:
            # Verificando se a feature foi informada:
            if (feature == None):
                print("Feature not found!")
            else:
                # Classifica os outliers da 'feature':
                self.outliers[feature].sort_values(ascending=ascending, inplace=True)

# ************************************* Definindo Funções *************************************
#
# ***** Função para carregar (load) um objeto python qualquer, armazenado em um arquivo "pickle":
#
def pickle_object_load (path=".", file="None", msg=None):
    '''
    Input:
        "path": diretório (path) do arquivo que será carregado.
        "file": nome do arquivo que será carregado.
        "msg": mensagem que será impressa na tela (default é None, ou seja,
               não será impressa uma mensagem).

    Output:
        "obj": retorna os dados do "objeto" armazenado no arquivo.
    '''
    # Código da função:

    # Prepara o nome completo do arquivo piclke que será carregado (load):
    object_file = os.path.join(path, file)
    
    try:
        # Abre o arquivo para o modo leitura (read):
        pickle_in = open(object_file,"rb")
        
        # Faz a leitura do arquivo e carrega os dados no objeto ("obj"):
        obj = pickle.load(pickle_in)

        # Fecha o arquivo "pickle":
        pickle_in.close()

        # Verifica se existe uma mensagem para ser impressa na tela:
        if (msg != None):
            # Imprime na tela a mensagem:
            print(msg)

        # Retorna os dados carregados:
        return obj
    
    except FileNotFoundError as error:
        # Erro encontrado na abertura do arquivo:
        print(error)
        # Retorna um valor nulo (None):
        return None

    except ValueError:
        # Erro encontrado na leitura do arquivo:
        print("I can not upload the '{}' file".format(file))
        
        # Fecha o arquivo "pickle":
        pickle_in.close()
        
        # Retorna um valor nulo (None):
        return None

# ***** Função para salvar (save) um objeto python qualquer em um arquivo "pickle":
#
def pickle_object_save (path=".", file="None", object_name=None, msg=None):
    '''
    Input:
        "path": diretório (path) onde o arquivo será criado.
        "file": nome do arquivo que será armazenado (salvo) o objeto python.
        "object_name": nome do objeto python que será armazenado (salvo) no arquivo.
        "msg": mensagem que será impressa na tela (default é None, ou seja,
               não será impressa uma mensagem).

    Output: None
    '''
    # Código da função:

    # Prepara o nome completo do arquivo piclke que será criado:
    object_file = os.path.join(path, file)
    
    try:
        # Abre o arquivo para o modo escrita (write):
        pickle_out = open(object_file,"wb")
        
        # Faz o 'dump' do objeto ("object_name") e salva os dados no arquivo ("file"):
        pickle.dump(object_name, pickle_out)

        # Fecha o arquivo "pickle":
        pickle_out.close()

        # Verifica se existe uma mensagem para ser impressa na tela:
        if (msg != None):
            # Imprime na tela a mensagem:
            print(msg)

    except FileNotFoundError as error:
        # Erro encontrado na abertura do arquivo:
        print(error)

    except:
        # Erro encontrado ao fazer o "dump" do objeto:
        print("I can not save the '{}' object".format(object_name))
        
        # Fecha o arquivo "pickle":
        pickle_out.close()

# ***** Função para carregar um dataset qualquer, retornando um objeto Dataframe do Pandas:
#
def load_dataset(file_path, index_col=None, low_memory=False):
    '''
    Input:
        "file_path": diretório (path) do dataset que será carregado.
        "index_col": atributo que será utilizado para indexar as linhas do dataframe criado.
                     default será "None"
        "low_memory": se "True", informa que a máquina possui pouca memória RAM disponível (default é False).

    Output:
        "df": objeto do tipo data frame do "Pandas".
    '''
    # Código da função:
    df = pd.read_csv(file_path, index_col=index_col, low_memory=False)
    
    # Retornando o resultado:
    return (df)

# ***** Função para verificar "duplicidades" em um dataset:
#
def dts_duplicated(file_name, df):
    '''
    Input:
        "file_name": nome do dataset que será analisado.
        "df": objeto do tipo DataFrame do Pandas.
    
    Output:
        "total": quantidade total de linhas duplicadas no dataset.
    '''
    # Código da função:

    # Soma a quantidade total de linhas duplicadas.
    total = df.duplicated().sum()
    
    print("\nQuantidade Total de Linhas Dupicadas no Dataset '%s': %d"
          %(file_name, total))

    # Retornando o resultado:
    return (total)

# ***** Função para verificar "missing values" (NaN) em um dataset:
#
def dts_missing_value(file_name, df):
    '''
    Input:
        "file_name": nome do dataset que será analisado.
        "df": objeto do tipo DataFrame do Pandas.
    
    Output:
        "result": objeto do tipo Series do "Pandas" com o resultado, ou seja,
                  com a quantidade de "missing values" em cada "feature" do DataFrame "df".
    '''
    # Código da função:
    print("\nAnalisando se existem valores ausentes (NaN) no dataset '%s':"
          %(file_name))
    
    result = df.isnull().sum()

    # Retornando o resultado:
    return (result)

# ***** Função para mostrar uma imagem em uma célula do "jupyter notebook":
#
def Image_Display(url):
    '''
    Input:
        "url": path do arquivo ou "url" onde está a imagem a ser mostrada.
    
    Output: None
    '''
    # Código da função:
    Image(url = url)

    return

# ***** Função para calcular os "missing values" em um DataFrame:
#
def Missing_Values(df):
    '''
    Input:
        "df": Data Frame.

    Output:
        Objeto do tipo "Dataframe" do Pandas.
    '''
    # Código da função:

    # Calcula o total de missing values para cada atributo (feature) do DataFrame "df":
    total = df.isnull().sum().sort_values(ascending=False)
    
    # Calcula a porcentagem de missing values para cada atributo (feature) do DataFrame "df":
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    
    # Retorna um dataframe com os resultados:
    return (pd.concat([total, percent], axis=1, names='Attributes (Columns)', keys=['Total', 'Percent']))

# ***** Função para calcular a proporção dos valores atribuidos para uma variável qualquer em um DataFrame:
#
def percent_count_feature(df, feature, lines_drop=False):

    '''
    Entrada:
        "df": Data Frame;
        "feature": atributo (variável) do Dataframe.
        "lines_drop":
            "True": eliminar as linhas cujo "Total" seja igual a zero ("0").
            "False": não eliminar as linhas cujo "Total" seja igual a zero ("0"). Este é o valor default.

    Saída:
        temp_df: Objeto do tipo "Dataframe" do Pandas, com os resultados calculados.
    '''
    # Código da função:

    # Cria um DataFrame temporário calculando a contagem de cada valor atribuido a variável desejada ('feature'):
    temp_df = pd.DataFrame(df[feature].groupby(df[feature]).count())
    temp_df.rename(columns={feature:'Total'}, inplace=True)
    temp_df.sort_values(by='Total', ascending=False, inplace=True)

    # Verifica se devemos eliminar as linhas cujo "Total" seja igual a zero ("0"), ou seja, "lines_drop=True":
    if(lines_drop):
        # Eliminando as linhas:
        lines = list(temp_df[temp_df['Total'] == 0].index) # Retorna uma lista com os índices das linhas.
        temp_df.drop(list(lines), inplace=True) # Elimina do DataFrame as linhas selecionadas.
    
    # Calcula a soma total (geral) dos valore para o atributo (feature) do DataFrame "df":
    TotalGeral = temp_df.Total.sum()
    
    # Cria uma nova coluna ('Percent'), calculando a porcentagem de cada valor do atributo (feature) do DataFrame "df":
    temp_df['Percent'] = round(number=temp_df.Total / TotalGeral, ndigits=4)

    # Retorna um dataframe com os resultados:
    return (temp_df)

# ***** Função para obter os "percentis" das features de um dataset qualquer.
#

def get_features_percentiles(data, features, percent_range):
    '''
    Input:
        "data": Data Frame com os dados.
        "features": Features do Data Frame que desejamos calcular os "Percentis".
        "percet_range": Lista dos percentis que desejamos calcular, no formto de 0 a 100.
    
    Output:
        "df": Data Frame com os percentis calculados para cada variável.
    '''
    # Código da função:

    # Cria um array dos "percentis" desejados:
    percentiles = np.array(percent_range)
    
    # Cria um data frame onde serão armazenados os percentis de cada feature:
    percentiles_str = [str(v)+'%' for v in percentiles] # prepara os índices do data frame.
    
    # Cria o dataframe:
    df = pd.DataFrame(index=percentiles_str)
    df.index.name = 'Percentile' # nomeia o índice do data frame.
    
    # Verifica se temos apenas "1" variável em "features":
    if (type(features) == str):
        # Calcula os percentis:
        result = np.percentile(a=data[features], q=percentiles)
        # Armazena os resultados no data frame:
        df[features] = result
    else:
        # Neste caso, "features" representa uma lista de variáveis.
        # Loop para calcular os percentis de cada variável em 'features':
        for feat in features:
            # Calcula os percentis:
            result = np.percentile(a=data[feat], q=percentiles)
            # Armazena os resultados no data frame:
            df[feat] = result
    
    # Retorna o resultado:
    return df

# ***** Função para encontrar os "outliers" das features de um dataset qualquer.
#
def iqr_score(df, features):
    '''
    O intervalo interquartil (IQR), também denominado por "média espalhada" (midspread) ou "média de 50%" (middle 50%), ou tecnicamente
    "propagação de H" (H-spread), é uma medida de dispersão estatística, sendo igual à diferença entre os percentis 75 e 25,
    ou entre os quartis superior e inferior, isto é: **`IQR = Q3 - Q1`**.

    Em outras palavras, o IQR é o primeiro quartil subtraído do terceiro quartil; estes quartis podem ser claramente vistos num gráfico
    de caixa (Box Plot) sobre os dados. É uma medida da dispersão semelhante ao desvio padrão ou variância, mas é muito mais robusta contra "outliers".

    Input:
        "df": Data Frame com as features que contém os "Outliers".
        "features": Lista com os nomes das features que contém os "Outliers".
    
    Output:
        "df_iqr": Data Frame com os cálculos relacionados ao IQR.
    '''
    # Código da função:

    # Criando um Data Frame para armazenar os cálculos relacionados ao "IQR":
    # Q1 = primeiro quartil (Inferior);
    # Q3 = terceiro quartil (Superior).
    df_iqr = pd.DataFrame(data={'Q1': df[features].quantile(0.25),
                                'Q3': df[features].quantile(0.75)})

    # Nomeando os índices:
    df_iqr.index.name = 'Features'

    # Calculado o interquartile range (IQR):
    df_iqr['IQR'] = df_iqr.Q3 - df_iqr.Q1

    # Calculando o Limite Inferior:
    df_iqr['Lower'] = df_iqr.Q1 - 1.5 * df_iqr.IQR

    # Calculando o Limite Superior:
    df_iqr['Upper'] = df_iqr.Q3 + 1.5 * df_iqr.IQR

    return df_iqr

# ***** Função para localizar os "outliers" (utilizando IQR score) das features de um dataset qualquer,
# ***** e, em seguida, salvá-los em um objeto específico passado em um dos parâmetros da função.
#
def outliers_save(df, features, df_iqr, outliers, display=True, elapsed_time=False):
    '''
    Input:
        "df": Data Frame com as features que contém os "Outliers".
        "features": Lista das features (nomes) que contêm os "outliers".
        "df_iqr": Data Frame com os cálculos relacionados ao IQR, referente as features que contêm os "outliers".
        "outliers": É uma instância (objeto) da classe "OutliersByFetures", onde serão armazenados
                    os nomes das "features" com os seus respectivos "outliers".
        "display": Flag para imprimir na tela um resumo dos resultados da função (default = True).
        "elapsed_time": Flag para calcular o "Tempo Decorrido" desta função (default = False).
    
    Output:
        "None": Está função não retornará informações.
    '''
    # Código da função:

    if (elapsed_time):
        # Criando uma instância para medirmos o tempo decorrido desta atividade:
        save_time = ElapsedTime(builder_msg=False)

        # Iniciando a contagem do tempo:
        msg = "Saving outliers..."
        save_time.start(msg=msg)
        print()

    # Salvando os outliers de cada feature em nosso objeto "outliers" da classe "OutliersByFetures":
    for feat in features:
        # Cria um índice para localizar os "outliers":
        index = (df[feat] < df_iqr.loc[feat,'Lower']) | (df[feat] > df_iqr.loc[feat,'Upper'])
        
        # Salvando os outliers:
        outliers.save(feature=feat, outliers=df.loc[index, feat])

        # Calculando o tempo decorrido:
    if (elapsed_time):
        replace_time.end()

        # Eliminando da memória o objeto criado para contagem do tempo decorrido:
        del(replace_time)

    if (display):
        print("Summary:")

        # Calculando o número total de "Oultliers":
        print("Features({0}): {1} outliers saved".format(len(outliers.keys()), outliers.count()))

# ***** Função para remover os "outliers" das features de um dataset qualquer.
# ***** Está função, na verdade, substituirá (replace) os "outliers" por valores
# ***** ausentes (NaN) (default).
#
def outliers_replace(df, outliers, value=np.nan, display=True, elapsed_time=True):
    '''
    Input:
        "df": Data Frame com as features que contém os "Outliers".
        "outliers": É uma instância (objeto) da classe "OutliersByFetures".
        "value": Valor que será utilizado para substituir os outliers (default = NaN).
        "display": Flag para imprimir na tela informações sobre o processo (default = True).
        "elapsed_time": Flag para calcular o "Tempo Decorrido" desta função (default = True).
    
    Output:
        "None": Está função não retornará informações.
    '''
    # Código da função:

    if (elapsed_time):
        # Criando uma instância para medirmos o tempo decorrido desta atividade (replace dos outliers):
        replace_time = ElapsedTime(builder_msg=False)

        # Iniciando a contagem do tempo de substituição (replace) dos outliers:
        msg = "Replacing outliers..."
        replace_time.start(msg=msg)
        print()

    # Vamos varrer com um loop cada feature que possui outliers, para então substituir (replace) seus valores por
    # valores ausentes (NaN):
    for feat, out in outliers.items():
        if (display):
            print("Feature({0}): {1} outliers".format(feat, out.count()))
        df[feat].replace(out, value, inplace=True)
        
    if (display):
        print("Summary:")
        print("Features({0}): {1} outliers replaced".format(len(outliers.keys()), outliers.count()))

    if (elapsed_time):
        # Calculando o tempo decorrido:
        print()
        replace_time.end()

        # Eliminando da memória o objeto criado para contagem do tempo decorrido:
        del(replace_time)

# ***** Função para calcular algumas medidas estatísticas de tendência central (moda, média e mediana),
# de dispersão (desvio padrão), de forma (assimetria e curtose), e também o coeficiente de variação (CV).
#
def statistical_measures(df, feature, decimals=3):

    '''
    Entrada:
        "df": Data Frame que contém os atributos (features);
        "feature": atributos (variáveis) do Dataframe.

    Saída:
        results_df: Objeto do tipo "Dataframe" do Pandas, com os resultados calculados.
    '''
    # Código da função:

    # Cria um dicionário, calculando as medidas estatísticas para cada atributo (feature) do DataFrame (df):
    measures = {'mean': df[feature].mean(), # média
                'median': df[feature].median(), # mediana
                'mode': df[feature].mode(axis=0).iloc[0], # moda
                'var': df[feature].var(), # variância.
                'std': df[feature].std(), # desvio padrão.
                'var_coff': (df[feature].std()/df[feature].mean())*100, # CV = (std/mean)*100
                'skewness': df[feature].skew(axis=0), # Assimetria
                'kurtosis': df[feature].kurtosis(axis=0) # Curtose
               }
    
    # Criando um DataFrame para armazenar os resultados:
    results_df = pd.DataFrame(data=measures).T

    # Verifica se os resultados serão arredondados:
    if (decimals != None):
        # Retorna o resultado com arredondamento dos resultados:
        return results_df.round(decimals=decimals)
    else:
        # Retorna os resultados sem arredondamento:
        return (results_df)

# ***** Função para converter algumas features do dataset em variáveis categóricas:
#
def set_categorical_dtype(df, features, categories, ordinal=False):
    '''
    Input:
        "df": dataframe da base de dados que contém as "features".
        "features": nome das "features" que serão transformadas em categóricas.
        "categories": lista com as classes das "features".
        "ordinal": se "True" indica que as categorias são "ordinais".
    
    Output: None
    '''
    # Código da função:
    
    # Define o dtype:
    cat_dtype = pd.api.types.CategoricalDtype(categories=categories, ordered=ordinal)
    df[features] = df[features].astype(cat_dtype)

    return

# ***** Função para verificar (check) "features" x "parâmetros" passados em uma função qualquer:
#
def check_params(features, params):
    '''
    Input:
        "features": lista de variáveis (features) de um dataframe qualquer.
        "params": valor único ou valores (lista) definidos para cada feature.
    
    Output:
        "None": Se o tamanho da lista de features for diferente do tamanho da lista de parâmetros.
        "params": retorna a própria lista de parâmetros.
        "default" Retorna uma lista de parâmetros com valores iguais (default).
    '''
    # Código da função:
    
    # Verifica se "params" é uma lista:
    if (type(params) == list):
            # Compara "params x features":
            if (len(params) != len(features)):
                # Erro: Size of 'params' and 'features' are different!"
                return None
            else:
                # Retorna a própria lista de parâmetros:
                return params
    else:
        # Retorna uma lista de parâmetros com valores iguais (default):
        return [params for i in range(0, len(features))]
