import pandas as pd
import numpy as np
from sklearn import tree

train1 = pd.read_csv('planilha 1 e 0 - tratamento excel.csv', delimiter=';')
train = train1.iloc[0:535,:]
y_train = train['TARGET']
x_train = train.drop(['TARGET'], axis=1).values
decision_tree = tree.DecisionTreeClassifier(max_depth = 20)
decision_tree.fit(x_train, y_train)

print('Olá, sou o seu Assistente Imobiliário.\nInformarei se o imóvel está caro ou barato com base no meu banco de dados.\nSepare os decimais por pontos(.) e não por vírgulas(,).')
try:
    valor_casa = float(input('Qual o valor da casa? '))
except:
    print('insira apenas valores numéricos, separados por ponto(.) em vez de vírgula(,)')
    quit()
    
data = {'Quartos':['Quantos quartos a casa tem? ', 154506.7183],
       'Banheiros':['Quantos banheiros a casa tem? ', 25197.9271],
       'Área':['Qual a área da casa? (sqft_lot)', 265.9522484],
       'Condição':['Qual a nota da condição da casa? ', 158589],
       'Grade':['Que estado a casa está (Grade)? ', 67505.9],
       'Ano':['Que ano foi construída? ', 263.61]}
df_chatbox = pd.DataFrame(data, index=['pergunta','média'], columns = ['Quartos', 'Banheiros', 'Área', 'Condição', 'Grade', 'Ano'])

array = []

for coluna in df_chatbox:
    try:
        resposta = float(input(df_chatbox.loc['pergunta', coluna]))
    except:
        print('insira um valor numérico, separado por ponto(.) em vez de vírgula(,)')
        quit()
    if (valor_casa/resposta) > df_chatbox.loc['média', coluna]:
        array.append(1)
    else:
        array.append(0)

resposta = decision_tree.predict([array])
if resposta[0] == 0:
    print('-------------Está BARATO!-------------')
else:
    print('-------------Está CARO!-------------')

