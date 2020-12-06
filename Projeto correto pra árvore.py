#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn import tree

train1 = pd.read_csv('DV.csv')
train = train1.iloc[0:535,:]
y_train = train['TARGET']
x_train = train.drop(['TARGET'], axis=1).values
decision_tree = tree.DecisionTreeClassifier(max_depth = 20)
decision_tree.fit(x_train, y_train)
features=['bedrooms','bathrooms','sqft_lot','condition','GRADE','yr_built']

with open("aula.dot", 'w') as f:
     f = tree.export_graphviz(decision_tree,
                              out_file=f,
                              max_depth = 20,
                              impurity = True,
                              feature_names = features,
                              class_names = ['0', '1'],
                              rounded = True,
                              filled= True )


# In[ ]:




