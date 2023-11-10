import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


def cost(x_tr, y_tr, coefficient):
    total_cost = 0
    n = len(x_tr)
    for i in range(n):
        total_cost += (1 / n) * ((x_tr[i] * coefficient).sum() - y_tr[i]) ** 2
    return total_cost


def dg(x_tr, y_tr, coefficient, l, epoch):
    n = len(x_tr)
    for i in range(epoch):
        slopes = np.zeros(6)
        for j in range(n):
            for k in range(6):
                slopes[k] += (1 / n) * ((x_tr[j] * coefficient).sum() - y_tr[j]) * x_tr[j][k]
        coefficient = coefficient - l * slopes
        print(cost(x_tr, y_tr, coefficient))
    return coefficient


if __name__ == '__main__':
    df = pd.read_csv("Flight_Price_Dataset_Q2.csv")

    df["stops"] = df["stops"].map({"zero": 0, "one": 1, "two_or_more": 2})

    df['arrival_time'] = df['arrival_time'].map({'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2,
                                                 'Evening': 3, 'Night': 4, 'Late_Night': 5})

    df['departure_time'] = df['departure_time'].map({'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2,
                                                     'Evening': 3, 'Night': 4, 'Late_Night': 5})

    df['class'] = df['class'].map({'Economy': 0, 'Business': 1})

    x = df.drop("price", axis=1).values
    y = df["price"].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    coefficients = np.zeros(6)
    epochs = 100
    L = 0.0001
    coefficients = dg(x_train, y_train, coefficients, L, epochs)
