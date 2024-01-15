import random
from sklearn.datasets import load_iris
from collections import Counter
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.utils import shuffle
from sklearn.naive_bayes import GaussianNB
import numpy as np


def ZeroR(data):
    c = Counter(data)
    return c.most_common(1)[0][0]

# a) Implement RandR

def RandR(data):
    return random.choice(data)


# ris dataset
features, classifications = load_iris(return_X_y=True)

# predict classifications
ZeroRScore = 0
RandRScore = 0

for classification in classifications:
    pred1 = ZeroR(classifications)
    pred2 = RandR(classifications)

    if pred1 == classification:
        ZeroRScore += 1
    if pred2 == classification:
        RandRScore += 1

print("ZeroR accuracy: %f RandR accuracy: %f" % (ZeroRScore / len(classifications), RandRScore / len(classifications)))

# b) Implement the split into test and training sets by hand
X_train, X_test, y_train, y_test = train_test_split(features, classifications, test_size=0.2)

# Perform five-fold cross-validation using a built-in sklearn estimator.
gnb = GaussianNB()
print(cross_val_score(gnb, features, classifications, cv=5))

# c) Implement five-fold cross-validation by hand
folds = 5
features, classifications = shuffle(features, classifications, random_state=42)
fold_size = len(features) // folds

accuracies = []

for i in range(folds):
    start = i * fold_size
    end = (i + 1) * fold_size

    X_test_fold = features[start:end]
    y_test_fold = classifications[start:end]

    X_train_fold = np.concatenate((features[:start], features[end:]))
    y_train_fold = np.concatenate((classifications[:start], classifications[end:]))

    model = GaussianNB()
    model.fit(X_train_fold, y_train_fold)

    accuracy = np.sum(model.predict(X_test_fold) == y_test_fold) / len(y_test_fold)
    accuracies.append(accuracy)

print("Manual cross validation accuracy: %f" % np.mean(accuracies))
