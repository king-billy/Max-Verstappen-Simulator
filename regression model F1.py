from sklearn.linear_model import LogisticRegression
import numpy as np

def find_prob(prob, car_performance, labels):
    X = np.column_stack([prob, car_performance])
    model = LogisticRegression()
    model.fit(X, labels)
    probabilities = model.predict_proba(X)[:, 1]
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    return probabilities