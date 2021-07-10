import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.model_selection import train_test_split

def classify():
    data = pd.read_csv(
        "C:\\Users\\MudassirRiaz\\PycharmProjects\\Malware Behavior Classification\\Json_Reports\\dataset.csv")
    data = data.drop(['ID', 'Name', 'SHA1', 'SHA256', 'MD5', 'Package', 'Time', 'Tid', 'Category'], axis=1)
    from sklearn.preprocessing import LabelEncoder
    labelencoder = LabelEncoder()
    X = labelencoder.fit_transform(data.Types)
    y = labelencoder.fit_transform(data.Api)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.22)
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Dense
    model = Sequential()
    model.add(Dense(2, input_dim=1, activation='relu'))
    model.add(Dense(2, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, batch_size=30, epochs=100)
    eval_model = model.evaluate(X_train, y_train)
    eval_model
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5)
    y_pred
    result = model.predict([X_test])
    result
    print(model.predict(X_train))
    model.save('C:\\Users\\MudassirRiaz\\PycharmProjects\\Malware Behavior Classification\\Json_Reports\\model1.h5')



# classify()