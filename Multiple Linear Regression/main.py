import math
import time
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def output_file(coefficient, exe_t, mse, rmse, mae, r2):
    file = open("[8]-UIAI4021-PR1-Q2.txt", "w+")
    file.write("Price: ")
    file.write(str(round(coefficient[0], 2)) + " * [departure_time] + " + str(round(coefficient[1], 2))
               + " * [stops] + " + str(round(coefficient[2], 2)) + " * [arrival_time] + "
               + str(round(coefficient[3], 2)) + " * [class] + " + str(round(coefficient[4], 2))
               + " * [duration] + " + str(round(coefficient[5], 2)) + " * [days_left] + "
               + str(round(coefficient[6], 2)))
    file.write("\nTraining Time: " + str(exe_t) + "s\n\n")
    file.write("Logs:")
    file.write("\nMSE: " + str(mse))
    file.write("\nRMSE: " + str(rmse))
    file.write("\nMAE: " + str(mae))
    file.write("\nR2: " + str(r2))
    file.close()


def gradient_decent(x_tr, y_tr, coefficient, learning_rate, epoch):
    n = len(x_tr)
    for i in range(epoch):
        predictions = np.dot(x_tr, coefficient)
        errors = predictions - y_tr
        gradient = (2/n) * x_tr.T.dot(errors)
        coefficient = coefficient - learning_rate * gradient
    return coefficient


if __name__ == '__main__':
    df = pd.read_csv("Flight_Price_Dataset_Q2.csv")

    df["stops"] = df["stops"].map({"zero": 1, "one": 2, "two_or_more": 3})

    df['arrival_time'] = df['arrival_time'].map({'Early_Morning': 1, 'Morning': 2, 'Afternoon': 3,
                                                 'Evening': 4, 'Night': 5, 'Late_Night': 6})

    df['departure_time'] = df['departure_time'].map({'Early_Morning': 1, 'Morning': 2, 'Afternoon': 3,
                                                     'Evening': 4, 'Night': 5, 'Late_Night': 6})

    df['class'] = df['class'].map({'Economy': 1, 'Business': 10})

    x = df.iloc[0:, 0:6]
    x = np.array(x)
    x = (x - x.mean()) / x.std()
    x = pd.DataFrame(x)
    x['b'] = 1
    x = np.array(x)
    y = df["price"].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)
    coefficients = np.zeros(7)
    epochs = 1000
    L = 0.1

    start = time.time()
    coefficients = gradient_decent(x_train, y_train, coefficients, L, epochs)
    end = time.time()

    exe_time = round(end - start, 1)

    y_pred = np.dot(x_test, coefficients)

    r2 = round(r2_score(y_test, y_pred), 2)
    mse = round(mean_squared_error(y_test, y_pred))
    rmse = round(math.sqrt(mse))
    mae = round(mean_absolute_error(y_test, y_pred))

    output_file(coefficients, exe_time, mse, rmse, mae, r2)
