import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.metrics import r2_score


def mse(x_tr, y_tr, coefficient, b):
    total_cost = 0
    n = len(x_tr)
    for i in range(n):
        total_cost += (1 / n) * (y_tr[i] - ((x_tr[i] * coefficient).sum() + b)) ** 2
    return total_cost


def gradient_decent(x_tr, y_tr, coefficient, b, learning_rate, epoch):
    n = len(x_tr)
    for i in range(epoch):
        b_temp = b
        slopes = coefficient
        for j in range(n):
            b_temp += (-2 / n) * (y_tr[j] - (x_tr[j] * coefficient).sum() + b)
            for k in range(18):
                slopes[k] += (-2 / n) * ((x_tr[j] * coefficient).sum() - y_tr[j]) * x_tr[j][k]
        b = b - learning_rate * b_temp
        coefficient = coefficient - learning_rate * slopes
        predict = (x_tr[i] * coefficient).sum() + b
        # print(r2_score(y_tr[i], [predict]))
        print(mse(x_tr, y_tr, coefficient, b))
    return coefficient, b


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

    # df["stops"] = df["stops"].map({"zero": 0, "one": 1, "two_or_more": 2})
    #
    # df['arrival_time'] = df['arrival_time'].map({'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2,
    #                                              'Evening': 3, 'Night': 4, 'Late_Night': 5})
    #
    # df['departure_time'] = df['departure_time'].map({'Early_Morning': 0, 'Morning': 1, 'Afternoon': 2,
    #                                                  'Evening': 3, 'Night': 4, 'Late_Night': 5})

    df['class'] = df['class'].map({'Economy': 1, 'Business': 5})

    # label = ["one", "two_or_more", "zero", "arrival_time_Afternoon", "arrival_time_Early_Morning",
    #          "arrival_time_Evening", "arrival_time_Late_Night", "arrival_time_Morning", "arrival_time_Night",
    #          "departure_time_Afternoon",
    #          "departure_time_Early_Morning", "departure_time_Evening", "departure_time_Late_Night",
    #          "departure_time_Morning", "departure_time_Night", "class", "duration", "days_left", "price"]

    # data = np.array(df)
    # scaler = MinMaxScaler()
    # normalized = scaler.fit_transform(data)
    # df = pd.DataFrame(normalized, columns=label)

    x = df.drop("price", axis=1).values
    y = df["price"].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, shuffle=False)
    coefficients = np.zeros(18)
    b = 0.1
    epochs = 100
    L = 0.01
    coefficients, b = gradient_decent(x_train, y_train, coefficients, b, L, epochs)
