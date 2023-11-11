import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def R2(y_pred, y_true):
    return r2_score(y_true, y_pred)


def cost(x_tr, y_tr, coefficient):
    total_cost = 0
    n = len(x_tr)
    for i in range(n):
        total_cost += (1 / n) * ((x_tr[i] * coefficient).sum() - y_tr[i]) ** 2
    return total_cost


def gradient_decent(x_tr, y_tr, y_test, coefficient, learning_rate, epoch):
    n = len(x_tr)
    for i in range(epoch):
        slopes = np.zeros(19)
        for j in range(n):
            for k in range(19):
                slopes[k] += (2 / n) * ((x_tr[j] * coefficient).sum() - y_tr[j]) * x_tr[j][k]
            coefficient = coefficient - learning_rate * slopes
            print(cost(x_tr, y_tr, coefficient))
    return coefficient


if __name__ == '__main__':
    df = pd.read_csv("Flight_Price_Dataset_Q2.csv")

    ohe = OneHotEncoder()

    feature_array = ohe.fit_transform(df[['stops', 'arrival_time', 'departure_time']]).toarray()
    labels = ["one", "two_or_more", "zero", "arrival_time_Afternoon", "arrival_time_Early_Morning",
              "arrival_time_Evening", "arrival_time_Late_Night", "arrival_time_Morning", "arrival_time_Night",
              "departure_time_Afternoon", "departure_time_Early_Morning", "departure_time_Evening",
              "departure_time_Late_Night", "departure_time_Morning", "departure_time_Night"]

    dataframe = pd.DataFrame(feature_array, columns=labels)
    df = df.drop("departure_time", axis=1)
    df = df.drop("arrival_time", axis=1)
    df = df.drop("stops", axis=1)
    df = pd.concat([dataframe, df], axis=1)

    df['class'] = df['class'].map({'Economy': 1, 'Business': 5})

    x = df.iloc[0:, 0:18]
    x['b'] = 1
    x = np.array(x)
    y = np.array(df.iloc[0:, 18:])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, shuffle=False)

    coefficients = np.zeros(19)
    epochs = 100
    L = 0.1

    coefficients = gradient_decent(x_train, y_train, y_test, coefficients, L, epochs)
    #R2(y_test, y_train)
