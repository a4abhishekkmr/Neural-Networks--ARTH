# -*- coding: utf-8 -*-
"""Churn_Modelling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-zzH-PMuIxxdf5RkIG6VXWCjUu1lskmW
"""

#Importing pandas

import pandas as pd

#Importing DAtaset

dataset=pd.read_csv("/content/sample_data/Churn_Modelling.csv")

dataset

dataset.columns

y = dataset['Exited']

X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
                  'IsActiveMember', 'EstimatedSalary']]
X.shape

#One Hot Encoding For Geography Feature

Geo = pd.get_dummies(dataset['Geography'], drop_first=True)
Geo

#One Hot Encoding For Gender Feature

Gender = pd.get_dummies(dataset['Gender'], drop_first=True)
Gender

X = pd.concat([X, Geo, Gender], axis=1)
X.shape

#importing train_test_split

#Before feeding your data into the neural network you need to split that data into training set and testing set. this can be done using

#train_test_split method from sklearn library and from model_selection module

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=40)

#importing Sequrntial Model From keras

from keras.models import Sequential
model = Sequential()            # creating Empty model

#Importing Dense Layer

from keras.layers import Dense

#Adding First Layer to model with neurons=8, input_feature=11 and activation fn = relu (rectified linear unit)

#1st layer
model.add(Dense(units=8, activation='relu', input_dim=11))

#Relu is an activation function i.e its will activate the neurons in the hidden layers. The main functions of relu is that all the output from a layers from all the neuron will pass to another layers of the respective neurons.

#Adding Second Layer with neurons=6 and activation fn = relu

model.add(Dense(units=6, activation='relu'))

#Adding third layer with neurons=6 and activation fn = relu

model.add(Dense(units=6, activation='relu'))

#Adding last layer with neurons=1 and activation fn = relu

model.add(Dense(units=1, activation='sigmoid'))

model.get_config()

model.summary()

#Now

from keras.optimizers import Adam

#As i have only one output that whether the Employee is exited from the company or not. i.e Binary output (Exited/notexited). So the loss will be generating in binary. To handle the binary loss we have binary_crossentropy.

model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.000001))

model.get_weights()

#For training the model we need to fit the model and it require training data i.e X_train, y_train. And the epochs is 100. That means your training data will goes 100 times through the neural network which you have build above with the respective layers.

model.fit(X_train, y_train, epochs=100)

loss = pd.DataFrame(model.history.history)
loss

#Plotting Loss Graph

loss.plot()

#As you can see the graph of the loss is slowly decreasing. So this can be possible because of Adam Optimizers

#Prediction
# To predict i am just giving random iputs but you can use the right values and it will predict on that case.

print("The employee will  :", model.predict([[1,2,3,4,5,6,7,8,9,10,11]])[0][0])

