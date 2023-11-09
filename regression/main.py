
import pandas as pd
import numpy as np
import time
from Regression import gradient_descent
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_squared_error, r2_score

def output(Y_test , prediction , X_columns , model , training_time):
    rmse_test = np.sqrt(mean_squared_error(Y_test, prediction))
    mae_test = mean_absolute_error(Y_test , prediction)
    mse_test = mean_squared_error(Y_test, prediction)
    r2_test = r2_score(Y_test, prediction)
    output = "PRICE = "
    for col, coef in zip(X_columns, model.coefficients):
        output+=''.join([f"({coef:.2f} * [{col}]) + "])

    output += f"({model.coefficients[-1]}) \n"
    output += f"Training Time: {training_time:.3f}s\n\n"
    output += "Logs:\n"
    output += f"MSE: {mse_test}\n"
    output += f"RMSE: {rmse_test}\n"
    output += f"MAE: {mae_test}\n"
    output += f"R2: {r2_test}"
    print(output)
    with open('[10]-UIAI4021-PR1-Q2.txt', 'w') as file:
        file.write(output)

def read_data(path):
    data = pd.read_csv(path)
    X = data[['duration', 'days_left']]
    Y = data['price']
    dummies = pd.get_dummies(data[['departure_time', 'stops', 'arrival_time', 'class']])
    X = pd.concat([X, dummies], axis=1)
    X_columns = X.columns

    return X , Y , X_columns

def normalize_data(X,Y):
    X = (X - X.mean())/ X.std()
    X['Ones'] = 1
    X = X.to_numpy()
    Y = Y.to_numpy()
    return X , Y

if __name__ == '__main__':
    X , Y , X_columns = read_data("Flight_Price_Dataset_Q2.csv")
    X , Y = normalize_data(X,Y)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    

    model = gradient_descent()
    start_time = time.time()
    model.fit(X_train, Y_train)
    training_time = time.time() - start_time
    prediction = model.predict(X_test)
    output = output(Y_test , prediction , X_columns , model , training_time)



