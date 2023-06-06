from sklearn.linear_model import LinearRegression
import numpy as np

def find_prob(prob, car_performance, labels):

    X = np.column_stack([prob, car_performance])

    model = LinearRegression()

    model.fit(X, labels)

    probabilities = model.predict(X)
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    return probabilities