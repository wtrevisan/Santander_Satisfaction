# ************************************* Plots Library For Data Science (Versão 1.0) *************************************
# Neste arquivo estão definidas algumas funções gráficas para serem utilizadas em Data Science.
#

# ************************************* Importando Pacotes e/ou Funções *************************************
#
# Importa o pacote "numpy":
import numpy as np

# Importa o pacote "pandas":
import pandas as pd

# Importa o pacote "itertools":
import itertools

# Importa a função "time" do pacote "time":
from time import time

# Importa o pacote "os" (Operation System with its Packages and Functions)
import os

# Importa a função "Image" do pacote "IPython.display":
from IPython.display import Image

# Importa o pacote "matplotlib":
import matplotlib as mpl

# Importa o pacote "pyplot" do "matplotlib":
import matplotlib.pyplot as plt

# Importa o pacote "seaborn"
import seaborn as sns

# Importa a função "confusion_matriz"
from sklearn.metrics import confusion_matrix

# O pacote "sys" permite manipulações com o sistema operacional:
import sys

# Path: onde estão armazenadas as classes e funções que serão utilizadas neste módulo:
LIB_PATH = os.path.join(".")

# Adicionando o diretório ao 'path' do Sistema, para podermos importar classes e funções que serão
# utilizadas neste módulo:
sys.path.append(LIB_PATH)

# Importando para este notebook, as classes e funções definidas no módulo "DataScience_Library_v1_0":
import DataScience_Library_v1_0 as dslib

# ************************************* Definindo Funções *************************************
#  ***** Function to save any figures (e.g., graphics, dashboards, etc.)
#
def save_figure (figure_id, figure_path, figure_file_format="png", figure_file_extension=".png",
                 tight_layout=True, dpi=300):
    '''
    Input:
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
    
    # Define o path (diretório) onde será salvo a figura:
    path = os.path.join(figure_path, figure_id + figure_file_extension)

    # Imprime na tela uma mensagem informando o nome do arquivo:
    print("Saving figure:", figure_id)

    # Tight layout?
    if tight_layout:
        plt.tight_layout()

    # Saving the figure:
    plt.savefig(path, format=figure_file_format, dpi=dpi)

# ***** Função para plotar as contagens de observações de cada classe de uma variável categórica.
# É como se fosse um "histograma" para variáveis qualitativas (categóricas):
#
def plot_count_feature(df=None, feature=None, order=True,
                       plot_style='darkgrid',
                       title=None, title_fontsize=16,
                       xlabel=None, xlabel_fontsize=13,
                       ylabel_fontsize=13,
                       xtick_labelsize=None, ytick_labelsize=None,
                       width=8, height=6,
                       figure_id=None, figure_path=None,
                       figure_file_format="png", figure_file_extension=".png",
                       tight_layout=True, dpi=300
                       ):
    '''
    Input:
        "df": DataFrame com a base de dados do dataset que será utilizado.
        "feature": Variável categórica que será utilizada para construir o gráfico (Plot).
        "order":
            "True": Os valores das classes serão apresentados no gráfico em ordem decrescente. Este é o valor "default".
            "False": Os valores das classes serão apresentados no gráfico em ordem normal, ou seja, de acordo com tipo definido para a variável.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "xlabel": Define o label do eixo "x" para o gráfico.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para o gráfico.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:

    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # Order
    if(order):
        value_counts = df[feature].value_counts().index
    else:
        value_counts = None
    
    # Plot
    sns.countplot(x = feature,
                  data = df,
                  order = value_counts
                 )

    # Definindo o título:
    plt.title(label=title, size=title_fontsize)

    # Definindo o label do eixo "x":
    plt.xlabel(xlabel=xlabel, size=xlabel_fontsize)

    # Definindo o label do eixo "y":
    plt.ylabel(ylabel="Count", size=ylabel_fontsize)

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do gráfico:
    plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
    
    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)
    
    # Mostrando o gráfico:
    plt.show()

    # Fechando as instâncias da figura (Figure) criada:
    plt.close()
    return

# ***** Função para plotar as contagens e proporções de observações de cada categoria de uma variável categórica qualquer.
# É como se fossemos criar um "histograma" para variáveis qualitativas (categóricas):
#
def plot_percent_count_feature(df=None, feature=None,
                               plot_style='darkgrid',
                               title=None, title_fontsize=16, title_share=False,
                               xlabel1=None, xlabel1_fontsize=13,
                               xlabel2=None, xlabel2_fontsize=13,
                               ylabel_fontsize=13,
                               columns_nr=2, rows_nr=1,
                               share_x=False, share_y=False,
                               width=17, height=6,
                               xtick_labelsize=None, ytick_labelsize=None,
                               wspace=None, hspace=None,
                               figure_id=None, figure_path=None,
                               figure_file_format="png", figure_file_extension=".png",
                               tight_layout=True, dpi=300
                               ):
    '''
    Input:
        "df": DataFrame com a base de dados do dataset que será utilizado.
        "feature": Variável categórica que será utilizada para construir o gráfico (Plot).
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "title": Define o título dos gráficos.
        "title_fontsize": Define o tamanho da fonte do título para os gráficos.
        "title_share": Define se o título do gráfico 1 deverá ser compartilhado com o gráfico 2.
        "xlabel1": Define o label do eixo "x" para o gráfico 1.
        "xlabel1_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico 1.
        "xlabel2": Define o label do eixo "x" para o gráfico 2.
        "xlabel2_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico 2.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para os gráficos 1 e 2.
        "colums_nr": Define se os gráficos serão colocados na horixontal (2), ou na vertical (1). 
        "rows_nr": Define se os gráficos serão colocados na horixontal (1), ou na vertical (2).
        "share_x": Define se os dois gráficos compartilharão o eixo "x".
        "share_y": Define se os dois gráficos compartilharão o eixo "y".
        "width": Define a largura da figura onde serão desenhados (plot) os dois gráficos.
        "heigth": Define a altura da figura onde serão desenhados (plot) os dois gráficos.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output:
        "Temp_df": objeto DataFrame com os valores das contagens e proporções da variável categórica "feature".
    '''
    # Código da função:
    
    # Criando um DataFrame temporário, calculando as contagens e proporções de valores da nossa variável (feature),
    # e em seguida faz o "reset" do índice, ou seja, o nosso índice passa a ser uma nova coluna em nosso
    # DataFrame temporário:
    Temp_df = dslib.percent_count_feature(df, feature).sort_index().reset_index()
       
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura e os dois eixos onde serão plotados os gráficos:
    fig, (ax1, ax2) = plt.subplots(nrows=rows_nr, ncols=columns_nr,
                                   sharex=share_x, sharey=share_y,
                                   figsize=(width,height))
    
    # Desenhando o gráfico no primeiro eixo (ax1), com as contagens das classes da nossa variável categórica "feature":
    sns.barplot(x = feature,
                y = 'Total',
                data = Temp_df,
                ax=ax1
                )
    
    # Definindo o título do primeiro gráfico:
    ax1.set_title(label = title, fontdict = {'fontsize': title_fontsize})
    
    # Definindo o label para o eixo "x" do primeiro gráfico:
    ax1.set_xlabel(xlabel = xlabel1, fontdict = {'fontsize': xlabel1_fontsize})
    
    # Definindo o label para o eixo "y" do primeiro gráfico:
    ax1.set_ylabel(ylabel = 'Count', fontdict = {'fontsize': ylabel_fontsize})

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do primeiro gráfico:
    ax1.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax1.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
    
    # Desenhando o gráfico no segundo eixo (ax2), com as proporções das classes da nossa variável categórica "feature":
    sns.barplot(x = feature,
                y = 'Percent',
                data = Temp_df,
                ax=ax2
                )
        
    # Definindo o título do segundo gráfico.
    # Verifica se o segundo gráfico será desenhado na mesma coluna, e se o eixo "x" será compartilhado com o
    # primeiro gráfico:
    if((columns_nr==1) and (share_x==True)):
        # Não coloca o título no segundo gráfico:
        ax2.set_title(label = None)
    else:
        if(title_share):
            # Compartilha o título do gráfico 1 com o gráfico 2:
            ax2.set_title(label = None)
            
        else: # Não compartilha o título do gráfico 1 com o gráfico 2.
            # Coloca o título no segundo gráfico:
            ax2.set_title(label = title, fontdict = {'fontsize': title_fontsize})
    
    # Definindo o label para o eixo "x" do primeiro gráfico:
    ax2.set_xlabel(xlabel = xlabel2, fontdict = {'fontsize': xlabel2_fontsize})
    
    # Definindo o label para o eixo "y" do segundo gráfico:
    ax2.set_ylabel(ylabel = 'Percent', fontdict = {'fontsize': ylabel_fontsize})
       
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do segundo gráfico:
    ax2.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax2.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Ajustando os espaçamentos (largura e altura) entre os gráficos nos subplots:
    fig.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura (Figure) criada:
    plt.close(fig)
    
    # Retorna um objeto DataFrame com os valores das contagens e proporções da variável categórica "feature":
    return (Temp_df)

# ***** Função para plotar as contagens e proporções de observações de cada categoria entre duas variáveis categóricas qualquer.
# Estamos criando uma tabela de referência cruzada para fazermos uma análise "bi-variada" entre duas variáveis qualitativas (categóricas):
#
def plot_crosstab_feature(x, y, plot_style='darkgrid', ticks_fontsize=12,
                          title=None, title_fontsize=16, title_share=False,
                          xlabel1=None, xlabel1_fontsize=13,
                          xlabel2=None, xlabel2_fontsize=13,
                          ylabel_fontsize=13,
                          columns_nr=2, rows_nr=1,
                          share_x=False, share_y=False,
                          width=17, height=6,
                          bar_width=0.5,
                          xtick_labelsize=None, ytick_labelsize=None,
                          wspace=None, hspace=None,
                          figure_id=None, figure_path=None,
                          figure_file_format="png", figure_file_extension=".png",
                          tight_layout=True, dpi=300
                          ):
    '''
    Input:
        "x": Variável categórica que será representada no eixo "x" dos gráficos.
        "y": Variável categórica que será representada no eixo "y" dos gráficos.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "ticks_fontsize": Define o tamanho da fonte dos ticks para os gráficos.
        "title": Define o título dos gráficos.
        "title_fontsize": Define o tamanho da fonte do título para os gráficos.
        "title_share": Define se o título do gráfico 1 deverá ser compartilhado com o gráfico 2.
        "xlabel1": Define o label do eixo "x" para o gráfico 1.
        "xlabel1_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico 1.
        "xlabel2": Define o label do eixo "x" para o gráfico 2.
        "xlabel2_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico 2.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para os gráficos 1 e 2.
        "colums_nr": Define se os gráficos serão colocados na horixontal (2), ou na vertical (1). 
        "rows_nr": Define se os gráficos serão colocados na horixontal (1), ou na vertical (2).
        "share_x": Define se os dois gráficos compartilharão o eixo "x".
        "share_y": Define se os dois gráficos compartilharão o eixo "y".
        "width": Define a largura da figura onde serão desenhados (plot) os dois gráficos.
        "heigth": Define a altura da figura onde serão desenhados (plot) os dois gráficos.
        "bar_width": Define a largura das barras dos gráficos.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output:
        Objeto DataFrame contendo a tabela de referência cruzada das "contagens" e "Proporções".
    '''
    # Código da função:
    
    # Cria uma tabela de referência cruzada para as variáveis "x" e "y":
    crosstab_counts = pd.crosstab(index=x, columns=y)
    
    # Normalizando para que a soma de cada linha seja igual a "1", ou seja, calculando as proporções de cada linha
    # da tabela:
    crosstab_pcts = crosstab_counts.div(crosstab_counts.sum(1), axis=0)
    
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura e os dois eixos onde serão plotados os gráficos:
    fig, (ax1, ax2) = plt.subplots(nrows=rows_nr, ncols=columns_nr,
                                   sharex=share_x, sharey=share_y,
                                   figsize=(width,height))
    
    # Desenhando o gráfico das proporções no primeiro eixo (ax1):
    crosstab_pcts.plot.bar(fontsize=ticks_fontsize, width=bar_width, ax=ax1)
    
    # Definindo o título do primeiro gráfico:
    ax1.set_title(label = title, fontdict = {'fontsize': title_fontsize})
    
    # Definindo o label para o eixo "x" do primeiro gráfico:
    ax1.set_xlabel(xlabel = xlabel1, fontdict = {'fontsize': xlabel1_fontsize})
    
    # Definindo o label para o eixo "y" do primeiro gráfico:
    ax1.set_ylabel(ylabel = 'Percent', fontdict = {'fontsize': ylabel_fontsize})

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do primeiro gráfico:
    ax1.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax1.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
    
    # Desenhando o gráfico das contagens no segundo eixo (ax2):
    crosstab_counts.plot.bar(fontsize=ticks_fontsize, width=bar_width, ax=ax2)
    
    # Definindo o título do segundo gráfico.
    # Verifica se o segundo gráfico será desenhado na mesma coluna, e se o eixo "x" será compartilhado com o
    # primeiro gráfico:
    if((columns_nr==1) and (share_x==True)):
        # Não coloca o título no segundo gráfico:
        ax2.set_title(label = None)
    else:
        if(title_share):
            # Compartilha o título do gráfico 1 com o gráfico 2:
            ax2.set_title(label = None)
            
        else: # Não compartilha o título do gráfico 1 com o gráfico 2.
            # Coloca o título no segundo gráfico:
            ax2.set_title(label = title, fontdict = {'fontsize': title_fontsize})

    # Definindo o label para o eixo "x" do segundo gráfico:
    ax2.set_xlabel(xlabel = xlabel2, fontdict = {'fontsize': xlabel2_fontsize})
    
    # Definindo o label para o eixo "y" do segundo gráfico:
    ax2.set_ylabel(ylabel = 'Count', fontdict = {'fontsize': ylabel_fontsize})
    
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do segundo gráfico:
    ax2.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax2.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Ajustando os espaçamentos (largura e altura) entre os gráficos nos subplots:
    fig.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura (Figure) criada:
    plt.close(fig)
    
    # Retorna um objeto DataFrame contendo a tabela de referência cruzada das "contagens" e "Proporções":
    return (pd.concat({'Count':crosstab_counts, 'Percent': round(number=crosstab_pcts, ndigits=2)}, axis=1))

# ***** Função para plotar um histograma de uma variável, para verificar a sua distribuição de frequências:
#
def plot_histogram_feature(data, bins=None,
                           plot_style='darkgrid', kde=False, color=None,
                           title=None, title_fontsize=16,
                           xlabel=None, xlabel_fontsize=13,
                           ylabel=None, ylabel_fontsize=13,
                           xtick_labelsize=None, ytick_labelsize=None,
                           width=8, height=6,
                           figure_id=None, figure_path=None,
                           figure_file_format="png", figure_file_extension=".png",
                           tight_layout=True, dpi=300
                          ):
    '''
    Input:
        "data": Variável numérica que será representada no eixo "x" do gráfico.
        "bins": Define o número de bins para o histograma.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "kde": Define se será plotado no gráfico a curva de densidade (KDE).
        "color": Define a cor do gráfico.
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "xlabel": Define o label do eixo "x" para o gráfico.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico.
        "ylabel": Define o label do eixo "y" para o gráfico.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para o gráfico.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # Plot
    sns.distplot(a=data, bins=bins, color=color, kde=kde)

    # Definindo o título:
    plt.title(label=title, size=title_fontsize)

    # Definindo o label do eixo "x":
    plt.xlabel(xlabel=xlabel, size=xlabel_fontsize)

    # Definindo o label do eixo "y":
    plt.ylabel(ylabel=ylabel, size=ylabel_fontsize)

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar um histograma e um gráfico de densidade duas variáveis numéricas.
# Está função é útil para verificarmos as distribuições de frequências de uma variável numérica, de acordo com as
# classes de uma variável categórica. Neste caso estamos considerando apenas "duas" classes para a variável categórica.
#
def plot_hist_kde_feature(data1, data2, bins=None,
                          plot_style="darkgrid",
                          title_hist=None, title_kde=None,title_fontsize=16,
                          legend_label1=None, legend_label2=None,
                          legend_fontsize=10,
                          xlabel=None, xlabel_fontsize=13,
                          color1=None, color2=None,
                          xtick_labelsize=None, ytick_labelsize=None,
                          width=17, height=6,
                          wspace=None, hspace=None,
                          figure_id=None, figure_path=None,
                          figure_file_format="png", figure_file_extension=".png",
                          tight_layout=True, dpi=300
                         ):
    '''
    Input:
        "data1": Variável numérica que será representada no eixo "x" do gráfico para a primeira classe (categoria).
        "data2": Variável numérica que será representada no eixo "x" do gráfico para a segunda classe (categoria).
        "bins": Define o número de bins para os histogramas.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "title_hist": Define o título do gráfico de histograma.
        "title_kde": Define o título do gráfico de densidade (KDE).
        "title_fontsize": Define o tamanho da fonte do título para os dois gráficos.
        "legend_label1": Define o label da legenda para a primeira classe (categoria).
        "legend_label2": Define o label da legenda para a segunda classe (categoria).
        "legend_fontsize": Define o tamanho da fonte para a legenda nos dois gráficos.
        "xlabel": Define o label do eixo "x" para os dois gráficos.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para os dois gráficos.
        "color1": Define a cor do gráfico para a primeira classe (categoria).
        "color2": Define a cor do gráfico para a segunda classe (categoria).
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde serão desenhados (plot) os dois gráficos.
        "heigth": Define a altura da figura onde serão desenhados (plot) os dois gráficos.
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
    
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura e os dois eixos onde serão plotados os gráficos:
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(width,height))
    
    # Desenhando os histogramas no primeiro eixo (ax1):
    sns.distplot(a=data1, bins=bins, color=color1, kde=False, label=legend_label1, ax=ax1)
    sns.distplot(a=data2,  bins=bins, color=color2, kde=False, label=legend_label2, ax=ax1)
    
    # Definindo o título do primeiro gráfico (Histogramas):
    ax1.set_title(label = title_hist, fontdict = {'fontsize': title_fontsize})
    
    # Definindo o label para o eixo "x" do primeiro gráfico (Histogramas):
    ax1.set_xlabel(xlabel = xlabel, fontdict = {'fontsize': xlabel_fontsize})
    
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do primeiro gráfico (Histogramas):
    ax1.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax1.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Colocando a legenda no primeiro gráfico (Histogramas):
    ax1.legend(fontsize=legend_fontsize)
    
    # Desenhando os gráficos de densidade (KDE) no segundo eixo (ax2):
    sns.kdeplot(data=data1, label=legend_label1, color=color1, shade=True, ax=ax2)
    sns.kdeplot(data=data2, label=legend_label2, color=color2, shade=True, ax=ax2)
    
    # Definindo o título do segundo gráfico (KDE's):
    ax2.set_title(label = title_kde, fontdict = {'fontsize': title_fontsize})
    
    # Definindo o label para o eixo "x" do segundo gráfico (KDE's):
    ax2.set_xlabel(xlabel = xlabel, fontdict = {'fontsize': xlabel_fontsize})
    
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do segundo gráfico (KDE's):
    ax2.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax2.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Colocando a legenda no segundo gráfico (KDE's):
    ax2.legend(fontsize=legend_fontsize)
    
    # Ajustando os espaçamentos (largura e altura) entre os gráficos nos subplots:
    fig.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura (Figure) criada:
    plt.close(fig)
    
    return

# ***** Função para plotar um boxplot de uma variável preditora ("Numérica"), de acordo com as classes de uma outra variável
# ("Categórica"):
def plot_boxplot_feature(x=None, y=None, hue=None, df=None, 
                         plot_style='darkgrid', orient='v', color=None, palette=None, saturation=0.75,
                         title=None, title_fontsize=16,
                         xlabel=None, xlabel_fontsize=13,
                         ylabel=None, ylabel_fontsize=13,
                         xtick_labelsize=None, ytick_labelsize=None,
                         width=8, height=6,
                         figure_id=None, figure_path=None,
                         figure_file_format="png", figure_file_extension=".png",
                         tight_layout=True, dpi=300
                         ):
    '''
    Input:
        "x": Variável categórica que será representada no eixo "x" do gráfico.
        "y": Variável numérica que será representada no eixo "y" do gráfico.
        "hue": Variável categórica para plotarmos o gráfico por classe.
        "df": DataFrame onde estão armazenadas as informações das variáveis "x" e "y".
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "color": Define a cor do gráfico.
        "palette": cores para serem usadas em diferentes níveis (classes) da variável "hue".
        "saturation": Define o nível de saturação da cor do gráfico.
        "orient": Define a orientação do gráfico: 'v' (vertical) ou 'h' (horizontal).
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título do gráfico.
        "xlabel": Define o label do eixo "x" para o gráfico.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico.
        "ylabel": Define o label do eixo "y" para o gráfico.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para o gráfico.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
    
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # Plot
    sns.boxplot(x=x, y=y, hue=hue, data=df, orient=orient, color=color, palette=palette, saturation=saturation)

    # Definindo o título:
    plt.title(label=title, size=title_fontsize)

    # Definindo o label do eixo "x":
    plt.xlabel(xlabel=xlabel, size=xlabel_fontsize)

    # Definindo o label do eixo "y":
    plt.ylabel(ylabel=ylabel, size=ylabel_fontsize)

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar um histograma e um boxplot de um variável numérica.
# Está função é útil para verificarmos as distribuições de frequências de uma variável numérica,
# assim como verificarmos a possível presença de "outliers".
#
def plot_hist_boxplot_feature(df, feature, bins=None, kde=False, orient_boxplot='h',
                              plot_style="darkgrid", cols_nr=1, rows_nr=2,
                              titles=None, titles_fontsize=16,
                              xlabels=None, xlabels_fontsize=13,
                              ylabels=None, ylabels_fontsize=13,
                              colors=None, saturation_boxplot=0.75,
                              xtick_labelsize=None, ytick_labelsize=None,
                              width=17, height=6,
                              wspace=None, hspace=None,
                              figure_id=None, figure_path=None,
                              figure_file_format="png", figure_file_extension=".png",
                              tight_layout=True, dpi=300
                             ):
    '''
    Input:
        "df": Data frame com os dados.
        "feature": Variável numérica que será representada nos dois gráficos (Histograma e BoxPlot).
        "bins": Define o número de bins para o histograma.
        "kde": Define se será plotado no gráfico do histograma a curva de densidade (KDE).
        "orient_boxplot": Define a orientação do gráfico de BoxPlot: 'v' (vertical) ou 'h' (horizontal).
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "cols_nr": Define o número de colunas dos subplots.
        "rows_nr": Define o número de linhas dos subplots.
        "title_hist": Define o título do gráfico de histograma.
        "title_boxplot": Define o título do gráfico de BoxPlot.
        "title_fontsize": Define o tamanho da fonte do título para os dois gráficos.
        "xlabel_hist": Define o label do eixo "x" para o Histograma.
        "xlabel_boxplot": Define o label do eixo "x" para o BoxPlot.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para os dois gráficos.
        "ylabel_hist": Define o label do eixo "y" para o Histograma.
        "ylabel_boxplot": Define o label do eixo "y" para o BoxPlot.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para os dois gráficos.
        "color_hist": Define a cor do Histograma.
        "color_boxplot": Define a cor do BoxPlot.
        "saturation_boxplot": Define o nível de saturação da cor do gráfico de BoxPlot.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x" para os dois gráficos.
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y" para os dois gráficos.
        "width": Define a largura da figura onde serão desenhados (plot) os dois gráficos.
        "heigth": Define a altura da figura onde serão desenhados (plot) os dois gráficos.
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:

    # Cria uma lista com duas "features" iguais, pois são dois plots para a mesma "feature":
    features = [feature, feature]

    # Verificando "Total de Subplots" x "Total de Variáveis":
    if(len(features) > (cols_nr * rows_nr)):
        # A quantidade de variáveis que deveremos plotar é maior que o número total de subplots definido.
        # Sendo assim, enviamos uma mensagem de erro e terminamos a função.
        print("***** ERROR: Quantidade total de variáveis é MAIOR que o total de subplots (columns_nr * rows_nr) *****")
        print("Redimensionar os parâmetros 'columns_nr' e 'rows_nr', ou diminuir a quantidade de variáveis!")
        return
    
    # Verificando (check) e definindo os valores para alguns parâmetros:
    #
    # colors:
    colors_values = dslib.check_params(features=features, params=colors)
    # Verifica se o tamanho (size) de "colors" x "features" são diferentes:
    if (colors_values == None):
        # Erro:
        print("Error: Size of 'colors' and 'features' are different!")
        return

    # titles:
    titles_names = dslib.check_params(features=features, params=titles)
    # Verifica se o tamanho (size) de "titles" x "features" são diferentes:
    if (titles_names == None):
        # Erro:
        print("Error: Size of 'titles' and 'features' are different!")
        return

    # xlabels:
    xlabels_names = dslib.check_params(features=features, params=xlabels)
    # Verifica se o tamanho (size) de "xlabels" x "features" são diferentes:
    if (xlabels_names == None):
        # Erro:
        print("Error: Size of 'xlabels' and 'features' are different!")
        return
    
    # xlabels:
    ylabels_names = dslib.check_params(features=features, params=ylabels)
    # Verifica se o tamanho (size) de "ylabels" x "features" são diferentes:
    if (ylabels_names == None):
        # Erro:
        print("Error: Size of 'ylabels' and 'features' are different!")
        return

    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)
    
    # Definindo a figura e os dois eixos onde serão plotados os gráficos:
    fig, (ax1, ax2) = plt.subplots(nrows=rows_nr, ncols=cols_nr, figsize=(width,height))
    
    # Desenhando o histograma no primeiro eixo (ax1):
    sns.distplot(a=df[feature], bins=bins, color=colors_values[0], kde=kde, ax=ax1)

    # Definindo o título do primeiro gráfico (Histograma):
    ax1.set_title(label = titles_names[0], fontdict = {'fontsize': titles_fontsize})
    
    # Definindo o label para o eixo "x" do primeiro gráfico (Histograma):
    ax1.set_xlabel(xlabel = xlabels_names[0], fontdict = {'fontsize': xlabels_fontsize})

    # Definindo o label para o eixo "y" do primeiro gráfico (Histograma):
    ax1.set_ylabel(ylabel = ylabels_names[0], fontdict = {'fontsize': ylabels_fontsize})
    
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do primeiro gráfico (Histograma):
    ax1.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax1.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Desenhando o gráficos de boxplot no segundo eixo (ax2):
    sns.boxplot(y=df[feature], orient=orient_boxplot, color=colors_values[1], saturation=saturation_boxplot)
    
    # Definindo o título do segundo gráfico (BoxPlot):
    ax2.set_title(label = titles_names[1], fontdict = {'fontsize': titles_fontsize})
    
    # Definindo o label para o eixo "x" do segundo gráfico (BoxPlot):
    ax2.set_xlabel(xlabel = xlabels_names[1], fontdict = {'fontsize': xlabels_fontsize})
    
    # Definindo o label para o eixo "y" do segundo gráfico (BoxPlot):
    ax2.set_ylabel(ylabel = ylabels_names[1], fontdict = {'fontsize': ylabels_fontsize})
    
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y" do segundo gráfico (BoxPlot):
    ax2.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    ax2.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Ajustando os espaçamentos (largura e altura) entre os gráficos nos subplots:
    fig.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura (Figure) criada:
    plt.close(fig)
    
    return

# ***** Função para plotar um histograma para cada variável definida em "features", para verificarmos a sua distribuição de frequências:
#
def plot_histograms_features(df, features, bins=None,
                             plot_style='darkgrid', kde=False, colors=None,
                             titles=None, titles_fontsize=16,
                             xlabels=None, xlabels_fontsize=13,
                             ylabels=None, ylabels_fontsize=13,
                             xtick_labelsize=None, ytick_labelsize=None,
                             cols_nr=2, rows_nr=2,
                             width=8, height=6,
                             wspace=None, hspace=None,
                             figure_id=None, figure_path=None,
                             figure_file_format="png", figure_file_extension=".png",
                             tight_layout=True, dpi=300
                             ):
    '''
    Input:
        "df": DataFrame com as variáveis que serão utilizadas.
        "features": Lista das variáveis numéricas que serão utilizadas nos plots.
        "bins": Define o número de bins para cada histograma.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "kde": Lista com as definições de plotagem do gráfico de densidade (KDE) para cada variável.
        "colors": Lista com as cores de cada histograma de cada variável.
        "titles": Lista com o título de cada histograma.
        "titles_fontsize": Lista com os tamanhos das fontes dos títulos para cada histograma.
        "xlabels": Lista com os labels do eixo "x" para cada histograma.
        "xlabels_fontsize": Define tamanho da fonte dos labels do eixo "x" para todos os histogramas.
        "ylabels": Lista com os labels do eixo "y" para cada histograma.
        "ylabels_fontsize": Define tamanho da fonte dos labels do eixo "y" para todos os histogramas.
        "xtick_labelsize": Define o tamanho da fonte dos labels dos "ticks" do eixo "x" para todos os histogramas.
        "ytick_labelsize": Define o tamanho da fonte dos labels dos "ticks" do eixo "y" para todos os histogramas.
        "colums_nr": Define o número de colunas para a plotagem dos histogramas.
        "rows_nr": Define o número de linhas para a plotagem dos histogramas.
        "width": Define a largura da figura onde serão desenhados (plot) todos os histogramas.
        "heigth": Define a altura da figura onde serão desenhados (plot) todos os histogramas.
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Verificando "Total de Subplots" x "Total de Variáveis":
    if(len(features) > (cols_nr * rows_nr)):
        # A quantidade de variáveis que deveremos plotar é maior que o número total de subplots definido.
        # Sendo assim, enviamos uma mensagem de erro e terminamos a função.
        print("***** ERROR: Quantidade total de variáveis é MAIOR que o total de subplots (columns_nr * rows_nr) *****")
        print("Redimensionar os parâmetros 'columns_nr' e 'rows_nr', ou diminuir a quantidade de variáveis!")
        return
    
    # Verificando (check) e definindo os valores para alguns parâmetros:
    #
    # bins
    bins_values = dslib.check_params(features=features, params=bins)
    # Verifica se o tamanho (size) de "bins" x "features" são diferentes:
    if (bins_values == None):
        # Erro:
        print("Error: Size of 'bins' and 'features' are different!")
        return

    # colors:
    colors_values = dslib.check_params(features=features, params=colors)
    # Verifica se o tamanho (size) de "colors" x "features" são diferentes:
    if (colors_values == None):
        # Erro:
        print("Error: Size of 'colors' and 'features' are different!")
        return

    # kde:
    kde_values = dslib.check_params(features=features, params=kde)
    # Verifica se o tamanho (size) de "kde" x "features" são diferentes:
    if (kde_values == None):
        # Erro:
        print("Error: Size of 'kde' and 'features' are different!")
        return

    # titles:
    titles_names = dslib.check_params(features=features, params=titles)
    # Verifica se o tamanho (size) de "titles" x "features" são diferentes:
    if (titles_names == None):
        # Erro:
        print("Error: Size of 'titles' and 'features' are different!")
        return

    # xlabels:
    xlabels_names = dslib.check_params(features=features, params=xlabels)
    # Verifica se o tamanho (size) de "xlabels" x "features" são diferentes:
    if (xlabels_names == None):
        # Erro:
        print("Error: Size of 'xlabels' and 'features' are different!")
        return
    
    # xlabels:
    ylabels_names = dslib.check_params(features=features, params=ylabels)
    # Verifica se o tamanho (size) de "ylabels" x "features" são diferentes:
    if (ylabels_names == None):
        # Erro:
        print("Error: Size of 'ylabels' and 'features' are different!")
        return

    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # "Loop for" para plotarmos os gráficos:
    for i, feature in enumerate(features):
        # Cria o subplot:
        ax = plt.subplot(rows_nr, cols_nr, i+1)
        
        # Plot do gráfico:
        sns.distplot(a=df[feature], bins=bins_values[i], color=colors_values[i], kde=kde_values[i], ax=ax)

        # Definindo o título:
        ax.set_title(label = titles_names[i], fontdict = {'fontsize': titles_fontsize})

        # Definindo o label do eixo "x":
        ax.set_xlabel(xlabel = xlabels_names[i], fontdict = {'fontsize': xlabels_fontsize})

        # Definindo o label do eixo "y":
        ax.set_ylabel(ylabel = ylabels_names[i], fontdict = {'fontsize': ylabels_fontsize})
        
        # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
        plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
        plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
   
    # Ajustando os espaçamentos entre os gráficos nos subplots:
    plt.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando os gráficos:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para ajustar (Fit) e plotar (Plot) uma "Estimativa da Densidade de kernel" (KDE) univariada ou bivariada.
#
def plot_kde_features(df, features, data2=None, shade=True, vertical=False, kernel='gau', bw='scott', gridsize=100,
                      cut=3, clip=None, legend=False, cumulative=False, shade_lowest=True, cbar=False, cbar_ax=None,
                      cbar_kws=None,
                      plot_style='darkgrid', colors=None, titles=None, titles_fontsize=16, xlabels=None, xlabels_fontsize=13,
                      ylabels=None, ylabels_fontsize=13, xtick_labelsize=None, ytick_labelsize=None, cols_nr=2, rows_nr=2,
                      width=8, height=6, wspace=None, hspace=None, figure_id=None, figure_path=None, figure_file_format="png",
                      figure_file_extension=".png", tight_layout=True, dpi=300
                     ):
    '''
    Input:
        "df": DataFrame com as variáveis que serão utilizadas.
        "features": Lista das variáveis numéricas que serão utilizadas nos plots.
        "data2": Second input data. If present, a bivariate KDE will be estimated.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "colors": Lista com as cores de cada KDE de cada variável.
        "titles": Lista com o título de cada KDE.
        "titles_fontsize": Lista com os tamanhos das fontes dos títulos para cada KDE.
        "xlabels": Lista com os labels do eixo "x" para cada KDE.
        "xlabels_fontsize": Define tamanho da fonte dos labels do eixo "x" para todos os KDEs.
        "ylabels": Lista com os labels do eixo "y" para cada KDE.
        "ylabels_fontsize": Define tamanho da fonte dos labels do eixo "y" para todos os KDEs.
        "xtick_labelsize": Define o tamanho da fonte dos labels dos "ticks" do eixo "x" para todos os KDEs.
        "ytick_labelsize": Define o tamanho da fonte dos labels dos "ticks" do eixo "y" para todos os KDEs.
        "colums_nr": Define o número de colunas para a plotagem dos KDEs.
        "rows_nr": Define o número de linhas para a plotagem dos KDEs.
        "width": Define a largura da figura onde serão desenhados (plot) todos os KDEs.
        "heigth": Define a altura da figura onde serão desenhados (plot) todos os KDEs.
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Verificando "Total de Subplots" x "Total de Variáveis":
    if(len(features) > (cols_nr * rows_nr)):
        # A quantidade de variáveis que deveremos plotar é maior que o número total de subplots definido.
        # Sendo assim, enviamos uma mensagem de erro e terminamos a função.
        print("***** ERROR: Quantidade total de variáveis é MAIOR que o total de subplots (columns_nr * rows_nr) *****")
        print("Redimensionar os parâmetros 'columns_nr' e 'rows_nr', ou diminuir a quantidade de variáveis!")
        return
    
    # Verificando (check) e definindo os valores para alguns parâmetros:
    #
    # gridsize
    gridsize_values = dslib.check_params(features=features, params=gridsize)
    # Verifica se o tamanho (size) de "bins" x "features" são diferentes:
    if (gridsize_values == None):
        # Erro:
        print("Error: Size of 'gridsize' and 'features' are different!")
        return

    # colors:
    colors_values = dslib.check_params(features=features, params=colors)
    # Verifica se o tamanho (size) de "colors" x "features" são diferentes:
    if (colors_values == None):
        # Erro:
        print("Error: Size of 'colors' and 'features' are different!")
        return

    # titles:
    titles_names = dslib.check_params(features=features, params=titles)
    # Verifica se o tamanho (size) de "titles" x "features" são diferentes:
    if (titles_names == None):
        # Erro:
        print("Error: Size of 'titles' and 'features' are different!")
        return

    # xlabels:
    xlabels_names = dslib.check_params(features=features, params=xlabels)
    # Verifica se o tamanho (size) de "xlabels" x "features" são diferentes:
    if (xlabels_names == None):
        # Erro:
        print("Error: Size of 'xlabels' and 'features' are different!")
        return
    
    # xlabels:
    ylabels_names = dslib.check_params(features=features, params=ylabels)
    # Verifica se o tamanho (size) de "ylabels" x "features" são diferentes:
    if (ylabels_names == None):
        # Erro:
        print("Error: Size of 'ylabels' and 'features' are different!")
        return

    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # "Loop for" para plotarmos os gráficos:
    for i, feature in enumerate(features):
        # Cria o subplot:
        ax = plt.subplot(rows_nr, cols_nr, i+1)
        
        # Plot do gráfico:
        sns.kdeplot(data=df[feature], gridsize=gridsize_values[i], color=colors_values[i], shade=shade, vertical=vertical,
                    kernel=kernel, bw=bw, cut=cut, clip=clip, legend=legend, cumulative=cumulative, shade_lowest=shade_lowest,
                    cbar=cbar, cbar_ax=cbar_ax, cbar_kws=cbar_kws, ax=ax)

        # Definindo o título:
        ax.set_title(label = titles_names[i], fontdict = {'fontsize': titles_fontsize})

        # Definindo o label do eixo "x":
        ax.set_xlabel(xlabel = xlabels_names[i], fontdict = {'fontsize': xlabels_fontsize})

        # Definindo o label do eixo "y":
        ax.set_ylabel(ylabel = ylabels_names[i], fontdict = {'fontsize': ylabels_fontsize})
        
        # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
        plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
        plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
   
    # Ajustando os espaçamentos entre os gráficos nos subplots:
    plt.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando os gráficos:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar um BoxPlot para cada variável definida em "features", para verificarmos a sua distribuição de frequências:
#
def plot_boxplots_features(df, features,
                           plot_style='darkgrid', colors=None,
                           orient='h', saturation=0.75,
                           titles=None, titles_fontsize=16,
                           xlabels=None, xlabels_fontsize=13,
                           ylabels=None, ylabels_fontsize=13,
                           xtick_labelsize=None, ytick_labelsize=None,
                           cols_nr=2, rows_nr=2,
                           width=8, height=6,
                           wspace=None, hspace=None,
                           figure_id=None, figure_path=None,
                           figure_file_format="png", figure_file_extension=".png",
                           tight_layout=True, dpi=300
                          ):
    '''
    Input:
        "df": DataFrame com as variáveis que serão utilizadas.
        "features": Lista das variáveis numéricas que serão utilizadas nos plots.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "colors": Lista com as cores de cada histograma de cada variável.
        "orient": Define a orientação do gráfico: 'v' (vertical) ou 'h' (horizontal).
        "saturation": Define o nível de saturação da cor do gráfico.
        "titles": Lista com o título de cada histograma.
        "titles_fontsize": Lista com os tamanhos das fontes dos títulos para cada histograma.
        "xlabels": Lista com os labels do eixo "x" para cada histograma.
        "xlabels_fontsize": Define tamanho da fonte dos labels do eixo "x" para todos os histogramas.
        "ylabels": Lista com os labels do eixo "y" para cada histograma.
        "ylabels_fontsize": Define tamanho da fonte dos labels do eixo "y" para todos os histogramas.
        "xtick_labelsize": Define o tamanho da fonte dos labels dos "ticks" do eixo "x" para todos os histogramas.
        "ytick_labelsize": Define o tamanho da fonte dos labels dos "ticks" do eixo "y" para todos os histogramas.
        "colums_nr": Define o número de colunas para a plotagem dos histogramas.
        "rows_nr": Define o número de linhas para a plotagem dos histogramas.
        "width": Define a largura da figura onde serão desenhados (plot) todos os histogramas.
        "heigth": Define a altura da figura onde serão desenhados (plot) todos os histogramas.
        "wspace": Define o espaçamento (largura) entre os gráficos nos subplots.
        "hspace": Define o espaçamento (altura) entre os gráficos nos subplots.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Verificando "Total de Subplots" x "Total de Variáveis":
    if(len(features) > (cols_nr * rows_nr)):
        # A quantidade de variáveis que deveremos plotar é maior que o número total de subplots definido.
        # Sendo assim, enviamos uma mensagem de erro e terminamos a função.
        print("***** ERROR: Quantidade total de variáveis é MAIOR que o total de subplots (columns_nr * rows_nr) *****")
        print("Redimensionar os parâmetros 'columns_nr' e 'rows_nr', ou diminuir a quantidade de variáveis!")
        return
    
    # Verificando (check) e definindo os valores para alguns parâmetros:
    #
    # colors:
    colors_values = dslib.check_params(features=features, params=colors)
    # Verifica se o tamanho (size) de "colors" x "features" são diferentes:
    if (colors_values == None):
        # Erro:
        print("Error: Size of 'colors' and 'features' are different!")
        return

    # titles:
    titles_names = dslib.check_params(features=features, params=titles)
    # Verifica se o tamanho (size) de "titles" x "features" são diferentes:
    if (titles_names == None):
        # Erro:
        print("Error: Size of 'titles' and 'features' are different!")
        return

    # xlabels:
    xlabels_names = dslib.check_params(features=features, params=xlabels)
    # Verifica se o tamanho (size) de "xlabels" x "features" são diferentes:
    if (xlabels_names == None):
        # Erro:
        print("Error: Size of 'xlabels' and 'features' are different!")
        return
    
    # xlabels:
    ylabels_names = dslib.check_params(features=features, params=ylabels)
    # Verifica se o tamanho (size) de "ylabels" x "features" são diferentes:
    if (ylabels_names == None):
        # Erro:
        print("Error: Size of 'ylabels' and 'features' are different!")
        return

    # Definindo o estilo do gráfico:
    if (plot_style != None):
        sns.set(style=plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # "Loop for" para plotarmos os gráficos:
    for i, feature in enumerate(features):
        # Cria o subplot:
        ax = plt.subplot(rows_nr, cols_nr, i+1)
        
        # Plot do gráfico:
        sns.boxplot(y=df[feature], orient=orient, color=colors_values[i], saturation=saturation)

        # Definindo o título:
        ax.set_title(label = titles_names[i], fontdict = {'fontsize': titles_fontsize})

        # Definindo o label do eixo "x":
        ax.set_xlabel(xlabel = xlabels_names[i], fontdict = {'fontsize': xlabels_fontsize})

        # Definindo o label do eixo "y":
        ax.set_ylabel(ylabel = ylabels_names[i], fontdict = {'fontsize': ylabels_fontsize})
        
        # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
        plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
        plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
   
    # Ajustando os espaçamentos entre os gráficos nos subplots:
    plt.subplots_adjust(wspace=wspace, hspace=hspace)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando os gráficos:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar as correlações entre as variáveis preditoras ("Numéricas") de um dataset qualquer:
#
def plot_corr_features(df, features, digits=3,
                       title=None, title_fontsize=None,
                       xtick_labelsize=None, ytick_labelsize=None,
                       width=8, height=6,
                       figure_id=None, figure_path=None,
                       figure_file_format="png", figure_file_extension=".png",
                       tight_layout=True, dpi=300
                      ):
    '''
    Input:
        "df": DataFrame onde estão armazenadas as informações das variáveis preditoras.
        "features": Lista com as variáveis preditoras.
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título do gráfico.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
    
    # Definindo a figura e o eixo onde será plotado o gráfico:
    fig, ax = plt.subplots(figsize=(width,height))
    
    # Plot:
    #sns.heatmap(data=df[features].corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
    sns.heatmap(data=np.around(df[features].corr(), decimals=digits), annot=True, linewidths=.5, ax=ax)
    
    # Definindo o título:
    plt.title(label=title, size=title_fontsize)
    
    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)
  
    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando a instância da figura criada:
    plt.close(fig)
    return

# ***** Função para plotar o número de features versus as pontuações (scores) da validação cruzada:
# ***** Este plot pode ser utilizado após o treinamento de um algorítmo utilizando a função "RFECV".
#
def plot_nb_feature_vs_cv_scores(nb_feat, cv_scores, plot_style=None, linewidth=2.0, color=None,
                                 scales=None, title=None, title_fontsize=18,
                                 xlabel=None, xlabel_fontsize=15, ylabel=None, ylabel_fontsize=15,
                                 xtick_labelsize=13, ytick_labelsize=13, width=8, height=7,
                                 figure_id=None, figure_path=None,
                                 figure_file_format="png", figure_file_extension=".png",
                                 tight_layout=True, dpi=300
                                ):
    '''
    Input:
        "nb_feat": Quantidade de features que serão representado no eixo "x" do gráfico.
        "cv_scores": Pontuações (Scores) da Validação Cruzada que serão representados no eixo "y" do gráfico.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "color": Define a cor do gráfico.
        "scales": define as escalas dos eixos "x" e "y".
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "xlabel": Define o label do eixo "x" para o gráfico.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico.
        "ylabel": Define o label do eixo "y" para o gráfico.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para o gráfico.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        mpl.style.use(plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # Plot
    plt.plot(nb_feat, cv_scores, color=color, linewidth=linewidth, linestyle='-')

    # Definindo as escalas dos eixos "x" e "y":
    if (scales != None):
        # Define as escalas:
        plt.axis(scales)

    # Definindo o título:
    plt.title(label=title, size=title_fontsize)

    # Definindo o label do eixo "x":
    plt.xlabel(xlabel=xlabel, size=xlabel_fontsize)

    # Definindo o label do eixo "y":
    plt.ylabel(ylabel=ylabel, size=ylabel_fontsize)

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar as features selecionadas (importantes) com as suas pontuações (scores):
# ***** Este plot pode ser utilizado após o treinamento de um algorítmo utilizando a função "RFE".
#
def plot_importances_features(feats, scores, plot_style=None, bar='h', bardim=0.8, align='center',
                              color=None, title=None, title_fontsize=20,
                              xlabel=None, xlabel_fontsize=15, ylabel=None, ylabel_fontsize=15,
                              xtick_labelsize=13, ytick_labelsize=13, width=12, height=10,
                              figure_id=None, figure_path=None,
                              figure_file_format="png", figure_file_extension=".png",
                              tight_layout=True, dpi=300
                             ):
    '''
    Input:
        "feats": Nomes das features que serão representadas no eixo "x" ou "y" do gráfico.
        "scores": Pontuações (Scores) das features que serão representados no eixo "x" ou y" do gráfico.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "bar": Define se as barras serão desenhadas, no gráfico, na vertical ('v') ou na horizontal ('h').
        "bardim": Define o tamanho da largura ou altura das barras que serão desenhadas no gráfico.
        "align": Define o tipo de alinhamento das barras que serão desenhadas no gráfico.
        "color": Define a cor das barras do gráfico.
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "xlabel": Define o label do eixo "x" para o gráfico.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico.
        "ylabel": Define o label do eixo "y" para o gráfico.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para o gráfico.
        "xtick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "x".
        "ytick_labelsize": Define o tamanho da fonte do label do "tick" do eixo "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        mpl.style.use(plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))
    
    # Verifica o tipo de gráfico que será desenhado:
    if (bar == 'v'):
        # Plot das barras na vertical:
        plt.bar(x=feats, height=scores, width=bardim, align=align, color=color)
    else:
        plt.barh(y=feats, width=scores, height=bardim, align=align, color=color)

    # Definindo o título:
    plt.title(label=title, size=title_fontsize)

    # Definindo o label do eixo "x":
    plt.xlabel(xlabel=xlabel, size=xlabel_fontsize)

    # Definindo o label do eixo "y":
    plt.ylabel(ylabel=ylabel, size=ylabel_fontsize)

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=xtick_labelsize)
    plt.tick_params(axis='y', which='major', labelsize=ytick_labelsize)

    # Verifica se os "ticks" do eixo "x" serão escritos na vertical:
    if (bar == 'v'):
        # Escreve os nomes das features na vertical:
        plt.xticks(rotation='vertical')

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar os modelos de machine learning com as suas pontuações (scores):
#
def plot_models_vs_scores(scores, plot_style=None, bar_color=None, alpha=0.8,
                          score_color=None, score_fontsize=15,
                          title=None, title_fontsize=20,
                          xlabel=None, xlabel_fontsize=18, ylabel=None, ylabel_fontsize=18,
                          ticks_fontsize=15, width=10, height=8,
                          figure_id=None, figure_path=None,
                          figure_file_format="png", figure_file_extension=".png",
                          tight_layout=True, dpi=300
                         ):
    '''
    Input:
        "scores": objeto Series do pandas com os modelos (index) e as suas pontuações (Scores).
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "bar_color": Define a cor das barras no gráfico.
        "alpha": Set the alpha value used for blending - not supported on all backends.
        "score_color": Define a cor dos valores (scores) que serão escritos ao lado das barras no gráfico.
        "score_fontsize": Define o tamanho da fonte dos valores (scores) que serão escritos ao lado das barras no gráfico.
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "xlabel": Define o label do eixo "x" para o gráfico.
        "xlabel_fontsize": Define tamanho da fonte do label do eixo "x" para o gráfico.
        "ylabel": Define o label do eixo "y" para o gráfico.
        "ylabel_fontsize": Define tamanho da fonte do label do eixo "y" para o gráfico.
        "ticks_fontsize": Define o tamanho da fonte dos labels dos "tick" dos eixos "x" e "y".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        mpl.style.use(plot_style)

    # Plot:
    ax = scores.plot(kind='barh', figsize=(width,height), color=bar_color, fontsize=ticks_fontsize);

    # Definindo o valor de alpha:
    ax.set_alpha(0.8)

    # Definindo o título:
    ax.set_title(title, fontsize=title_fontsize)

    # Definindo o label do eixo "x":
    ax.set_xlabel(xlabel, fontsize=xlabel_fontsize);
    
    # Definindo o label do eixo "y":
    ax.set_ylabel(ylabel, fontsize=ylabel_fontsize);
    
    # Definindo os ticks do eixo "x":
    ax.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])

    # set individual bar lables:
    for i in ax.patches:
        # get_width pulls left or right; get_y pushes up or down
        ax.text(i.get_width()+.01, i.get_y()+.38, \
                str(round(i.get_width()*100, 2))+'%', fontsize=score_fontsize,
                color=score_color)

    # invert for largest on top 
    ax.invert_yaxis()

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar a "Confusion Matrix" dos modelos de machine learning com as suas previsões:
#
def plot_confusion_matrix(truth, pred, display_labels, normalize=False, plot_style=None,
                          colors=plt.cm.Greens, title=None, title_fontsize=18,
                          labels_fontsize=15, ticks_fontsize=13, values_fontsize=13,
                          rotation=0, width=6, height=6,
                          figure_id=None, figure_path=None,
                          figure_file_format="png", figure_file_extension=".png",
                          tight_layout=True, dpi=300
                         ):
    '''
    Input:
        "truth": valores reais das classes.
        "pred": valores previstos das classes.
        "display_labels": lista com os nomes (labels) das classes.
        "normalize": se 'True' os valores serão normalizados.
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "colors": Define as cores do gráfico.
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "labels_fontsize": Define tamanho da fonte dos labels dos eixos "x" e "y" para o gráfico.
        "ticks_fontsize": Define o tamanho da fonte dos labels dos "tick" dos eixos "x" e "y".
        "values_fontsize": Define o tamanho da fonte dos valores (números) que serão apresentados no gráfico.
        "rotation": Define a rotação das classes no eixo "x".
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Calculando os dados da matriz de confusão:
    cm = confusion_matrix(truth, pred)
    
    # Se "True", normaliza os dados:
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        mpl.style.use(plot_style)
 
    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    plt.imshow(cm, interpolation='nearest', cmap=colors)
    
    # Definindo o título:
    if (title == None):
        plt.title('Confusion Matrix', size=title_fontsize)
    else:
        plt.title(title, size=title_fontsize)
    
    # Definindo a barra de cores (vertical):
    cb = plt.colorbar(fraction=0.046, pad=0.05, orientation="vertical")
    for t in cb.ax.get_yticklabels():
        t.set_fontsize(values_fontsize)
    
    # Definindo os ticks nos eixos "x" e "y":
    plt.tick_params(direction='out', length=6, width=1, axis='both', which='major')
    tick_marks = np.arange(len(display_labels))
    plt.xticks(tick_marks, display_labels, rotation=rotation, size=ticks_fontsize)
    plt.yticks(tick_marks, display_labels, size=ticks_fontsize)

    # Formatando os valores do gráfico:
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center", fontsize=values_fontsize,
                 color="white" if cm[i, j] > thresh else "black")

    # Define os labels dos eixos "x" e "y":
    plt.ylabel('Real Classes', size=labels_fontsize)
    plt.xlabel('Predicted Classes', size=labels_fontsize)

    # Desliga o 'grid':
    plt.grid(False)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar a "ROC Curve" dos modelos de machine learning:
#
def plot_roc_curve(fpr, tpr, auc, auc_decimals=4, plot_style=None, color=None, line_width=2,
                   title=None, title_fontsize=18, labels_fontsize=15,
                   ticks_fontsize=13, legendtitle=None, legendtitle_fontsize=13,
                   legend_label=None, legend_fontsize=13,
                   width=6, height=6,
                   figure_id=None, figure_path=None,
                   figure_file_format="png", figure_file_extension=".png",
                   tight_layout=True, dpi=300
                  ):
    '''
    Input:
        "fpr": São as taxas de falsos positivos (False Positive Rate).
        "tpr": São as taxas de verdadeiros positivos (True Positive Rate).
        "auc": É o valor da "AUC" (Area Uder Curve).
        "auc_decimals": Define o número de casas decimais do valor da "AUC".
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "color": Define a cor do gráfico.
        "line_width": define a largura da linha.
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "labels_fontsize": Define tamanho da fonte dos labels dos eixos "x" e "y" para o gráfico.
        "ticks_fontsize": Define o tamanho da fonte dos labels dos "tick" dos eixos "x" e "y".
        "legendtitle": Define o título da legenda.
        "legendtitle_fontsize": Define o tamanho da fonte do título da legenda.
        "legend_label": Define o label da legenda.
        "legend_fontsize": Define o tamanho da fonte da legenda.
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        mpl.style.use(plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # Definindo o "label" da legenda:
    label = legend_label + "(" + str(np.round(auc, decimals=auc_decimals)) + ")"

    # Plot da curva ROC:
    plt.plot(fpr, tpr, linewidth=line_width, color=color, label=label)
    
    # Plot da linha diagonal tracejada:
    plt.plot([0, 1], [0, 1], 'k--')
    
    # Definindo as escalas dos eixos "x" e "y":
    plt.axis([0, 1, 0, 1])

    # Definindo o título:
    plt.title(title, size=title_fontsize)

    # Definindo os labels dos eixos "x" e "y":
    plt.xlabel('False Positive Rate', fontsize=labels_fontsize)
    plt.ylabel('True Positive Rate', fontsize=labels_fontsize)

    # Definindo a "legenda":
    plt.legend(title=legendtitle, title_fontsize=legendtitle_fontsize,
               fontsize=legend_fontsize, loc="lower right")

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=ticks_fontsize)
    plt.tick_params(axis='y', which='major', labelsize=ticks_fontsize)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return

# ***** Função para plotar duas ou mais "ROC Curves" dos modelos de machine learning:
#
def plot_roc_curves(fpr, tpr, auc, auc_decimals=4, plot_style=None, color=None, line_width=2, scales=None,
                    title=None, title_fontsize=18, labels_fontsize=15,
                    ticks_fontsize=13, legendtitle=None, legendtitle_fontsize=13,
                    legend_label=None, legend_fontsize=13,
                    width=6, height=6,
                    figure_id=None, figure_path=None,
                    figure_file_format="png", figure_file_extension=".png",
                    tight_layout=True, dpi=300
                   ):
    '''
    Input:
        "fpr": "Dicionário" com as taxas de falsos positivos (False Positive Rate) de cada modelo.
        "tpr": "Dicionário" com  as taxas de verdadeiros positivos (True Positive Rate) de cada modelo.
        "auc": "Data frame" com os valores da "AUC" (Area Uder Curve) de cada modelo.
        "auc_decimals": Define o número de casas decimais do valor da "AUC".
        "plot_style": Define o estilo do gráfico (ver os estilos na função "matplotlib.style.available").
        "color": "Lista" com as cores do gráfico.
        "line_width": define a largura das linhas do gráfico.
        "scales": define as escalas dos eixos "x" e "y".
        "title": Define o título do gráfico.
        "title_fontsize": Define o tamanho da fonte do título para o gráfico.
        "labels_fontsize": Define tamanho da fonte dos labels dos eixos "x" e "y" para o gráfico.
        "ticks_fontsize": Define o tamanho da fonte dos labels dos "tick" dos eixos "x" e "y".
        "legendtitle": Define o título da legenda.
        "legendtitle_fontsize": Define o tamanho da fonte do título da legenda.
        "legend_label": "Lista" com os labels da legenda para cada modelo.
        "legend_fontsize": Define o tamanho da fonte da legenda.
        "width": Define a largura da figura onde será desenhado (plot) o gráfico.
        "heigth": Define a altura da figura onde será desenhado (plot) o gráfico.
        "figure_id": nome do arquivo onde será salvo a figura.
        "figure_path": nome do diretório (path) onde será salvo a figura.
        "figure_file_format": formato da figura que será salvo no arquivo.
        "figure_file_extension": extansão do arquivo onde será salvo a figura.
        "tight_layout": Se "True" chama o método "tight_layout()".
        "dpi": define a resolução da figura que será salva.

    Output: None
    '''
    # Código da função:
        
    # Definindo o estilo do gráfico:
    if (plot_style != None):
        mpl.style.use(plot_style)

    # Definindo a figura onde serão plotados os gráficos:
    if ((width != None) and (height != None)):
        plt.figure(figsize=(width,height))

    # Loop for para plotar cada modelo:
    for i in range(0, len(legend_label)):
        # Definindo o "label" da legenda:
        label = legend_label[i] + "(" + str(np.round(auc.iloc[i,0], decimals=auc_decimals)) + ")"
        
        # Plot da curva ROC:
        plt.plot(fpr[legend_label[i]], tpr[legend_label[i]], linewidth=line_width, color=color[i], label=label)
    
    # Plot da linha diagonal tracejada:
    plt.plot([0, 1], [0, 1], 'k--')
    
    # Definindo as escalas dos eixos "x" e "y":
    if (scales == None):
        # Define as escalas "default":
        plt.axis([0, 1, 0, 1])
    else:
        plt.axis(scales)

    # Definindo o título:
    plt.title(title, size=title_fontsize)

    # Definindo os labels dos eixos "x" e "y":
    plt.xlabel('False Positive Rate', fontsize=labels_fontsize)
    plt.ylabel('True Positive Rate', fontsize=labels_fontsize)

    # Definindo a "legenda":
    plt.legend(title=legendtitle, title_fontsize=legendtitle_fontsize,
               fontsize=legend_fontsize, loc="lower right")

    # Definindo o tamanho dos labels dos ticks nos eixos "x" e "y":
    plt.tick_params(axis='x', which='major', labelsize=ticks_fontsize)
    plt.tick_params(axis='y', which='major', labelsize=ticks_fontsize)

    # Verificando se o gráfico deverá se salvo:
    if (figure_id != None):
        save_figure (figure_id=figure_id, figure_path=figure_path,
                     figure_file_format=figure_file_format,
                     figure_file_extension=figure_file_extension,
                     tight_layout=tight_layout, dpi=dpi)

    # Mostrando o gráfico:
    plt.show()
    
    # Fechando as instâncias da figura criada:
    plt.close()
    
    return