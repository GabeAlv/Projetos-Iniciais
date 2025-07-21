# importando as bibliotecas necessarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

base = pd.read_csv('iris.csv') # lendo a base de dados e passando para a variavel base

def visualizar_dados(): # função para visualizar os dados
    print(base.head(10)) # visualizando os 10 primeiros registros
    print(np.unique(base['species'], return_counts=True)) # visualizando quais classes tem e quantas tem
    print(base.shape) # visualizando quantos registros tem na base
    print(base.describe()) # visualizando informaçoes sobre os dados
    print(base.isnull().sum()) # vendo se há valores nulos na base de dados
    plt.hist(base['sepal_width']) # plotando um grafico de barras de uma coluna
    plt.show()

def separando_dados(base):
    x_iris = base.iloc[:,:-1].to_numpy() # separando os atributos previsores
    y_iris = base.iloc[:, -1].to_numpy() # seprando os atributos metas

    #separando em base de teste e treino
    x_iris_treino, x_iris_teste, y_iris_treino, y_iris_teste = train_test_split(x_iris, y_iris, test_size=0.10, random_state=0 )
    return  x_iris_treino, x_iris_teste, y_iris_treino, y_iris_teste

def treinando_modelo(x_iris_treino, y_iris_treino):
    model = GaussianNB() # # Instancia o modelo de classificação Naive Bayes Gaussiano
    model.fit(x_iris_treino, y_iris_treino) # treinando o modelo

    return model

def previsao_metrica(model, x_iris_teste, y_iris_teste):
    previsao = model.predict(x_iris_teste) # prevendo os dados
    print(previsao)
    print(accuracy_score(y_iris_teste, previsao)) # mostrando a porcentagem de acerto do modelo
    print(confusion_matrix(y_iris_teste, previsao)) # mostrando a matriz de confusão do modelo
    print(classification_report(y_iris_teste, previsao)) # Avaliação do desempenho do modelo com métricas para cada classe


x_iris_treino, x_iris_teste, y_iris_treino, y_iris_teste = separando_dados(base)
modelo_treinado = treinando_modelo(x_iris_treino, y_iris_treino)

previsao_metrica(modelo_treinado, x_iris_teste, y_iris_teste)

#visualizar_dados()
