import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


def cost(x_tr, y_tr, coefficient):
    total_cost = 0
    n = len(x_tr)
    temp = np.dot(x_tr, coefficient) - y_tr
    total_cost = (1 / n) * np.dot(np.transpose(temp), temp)
    return total_cost


def gradient_decent(x_tr, y_tr, coefficient, learning_rate, epoch):
    n = len(x_tr)
    for i in range(epoch):
        # slopes = (2/n) * np.dot(np.transpose(np.dot(x_tr, coefficient) - y_tr), x_tr)
        predictions = np.dot(x_tr, coefficient)
        errors = predictions - y_tr
        gradient = (2/n) * x_tr.T.dot(errors)
        coefficient = coefficient - learning_rate * gradient
        # print(cost(x_tr, y_tr, coefficient))
    return coefficient


if __name__ == '__main__':
    df = pd.read_csv("Flight_Price_Dataset_Q2.csv")

    # ohe = OneHotEncoder()
    #
    # feature_array = ohe.fit_transform(df[['stops', 'arrival_time', 'departure_time']]).toarray()
    # labels = ["one", "two_or_more", "zero", "arrival_time_Afternoon", "arrival_time_Early_Morning",
    #           "arrival_time_Evening", "arrival_time_Late_Night", "arrival_time_Morning", "arrival_time_Night",
    #           "departure_time_Afternoon", "departure_time_Early_Morning", "departure_time_Evening",
    #           "departure_time_Late_Night", "departure_time_Morning", "departure_time_Night"]
    #
    # dataframe = pd.DataFrame(feature_array, columns=labels)
    # df = df.drop("departure_time", axis=1)
    # df = df.drop("arrival_time", axis=1)
    # df = df.drop("stops", axis=1)
    # df = pd.concat([dataframe, df], axis=1)

    df["stops"] = df["stops"].map({"zero": 1, "one": 2, "two_or_more": 3})

    df['arrival_time'] = df['arrival_time'].map({'Early_Morning': 1, 'Morning': 2, 'Afternoon': 3,
                                                 'Evening': 4, 'Night': 5, 'Late_Night': 6})

    df['departure_time'] = df['departure_time'].map({'Early_Morning': 1, 'Morning': 2, 'Afternoon': 3,
                                                     'Evening': 4, 'Night': 5, 'Late_Night': 6})

    df['class'] = df['class'].map({'Economy': 1, 'Business': 10})

    # label = ["one", "two_or_more", "zero", "arrival_time_Afternoon", "arrival_time_Early_Morning",
    #          "arrival_time_Evening", "arrival_time_Late_Night", "arrival_time_Morning", "arrival_time_Night",
    #          "departure_time_Afternoon",
    #          "departure_time_Early_Morning", "departure_time_Evening", "departure_time_Late_Night",
    #          "departure_time_Morning", "departure_time_Night", "class", "duration", "days_left", "price"]

    # data = np.array(df)
    # scaler = MinMaxScaler()
    # normalized = scaler.fit_transform(data)
    # df = pd.DataFrame(normalized, columns=label)

    # x = df.drop("price", axis=1).values
    x = df.iloc[0:, 0:6]
    x = np.array(x)
    x = (x - x.mean()) / x.std()
    x = pd.DataFrame(x)
    x['b'] = 1
    x = np.array(x)
    y = df["price"].values

    # y = (y - y.mean()) / y.std()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)
    coefficients = np.zeros(7)
    epochs = 2000
    L = 0.1
    coefficients = gradient_decent(x_train, y_train, coefficients, L, epochs)
    y_pred = np.dot(x_test, coefficients)
    r2 = round(r2_score(y_test, y_pred), 2)
    mse = mean_squared_error(y_test, y_pred)
    print(coefficients)
    print("MSE: ", str(mse))
    print("R2: ", str(r2))
