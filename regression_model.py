from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
import numpy as np
from model_metrics import X, y

def find_prob():
    kf = KFold(n_splits=5)
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    model = LinearRegression()

    model.fit(X_train, y_train)

    probabilities = np.array(model.predict(X_test))
    prob = [0, 0, 0, 0, 0]
    for i in range(5):
        driver_predictions = probabilities[i::5]
        prob[i] = np.mean(driver_predictions)
    
    prob = np.array(prob)
    prob /= prob.sum()
    return prob

