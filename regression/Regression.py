import numpy as np


class gradient_descent:
    def __init__(self, learning_rate=0.1, num_iterations=2000, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.coefficients = None
        self.coefficients = None
        self.cost_history = []
        self.tolerance = tolerance

    def fit(self, X, Y):

        self.coefficients = np.zeros(X.shape[1])

        for iteration  in range(self.num_iterations):

            predictions = np.dot(X, self.coefficients)

            errors = predictions - Y

            gradient = np.dot(X.T, errors) / len(Y)
            self.coefficients -= self.learning_rate * gradient

            rmse = np.sqrt(np.mean((predictions - Y) ** 2))
            self.cost_history.append(rmse)


            if iteration > 0 and abs(self.cost_history[iteration - 1] - rmse) < 1e-3 and self.learning_rate > 0.01:
                self.learning_rate = self.learning_rate / 10 
                
            if iteration > 0 and abs(self.cost_history[iteration - 1] - rmse) < self.tolerance:
                self.num_iterations = iteration + 1
                break

    def predict(self, X):
        if self.coefficients is None:
            raise ValueError("Model has not been fitted. Call fit() first.")
        return np.dot(X, self.coefficients)
   