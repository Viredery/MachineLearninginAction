import numpy as np

def loadDataSet(fileName):
    dataMat, labelMat = [], []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split()
	dataMat.append([float(num) for num in lineArr[:-1]])
	labelMat.append(int(lineArr[-1]))
    return np.array(dataMat), np.array(labelMat)

def decisionStump(inX, s, theta):
    return s * (1 if inX - theta > 0 else -1)

def findBestThreshold(X, y):
    m, n = X.shape
    minError = 1.0
    feature, bestThreshold, bestS = None, None, None
    for i in range(n):
        sortedFeature = X[:, i].copy()
	sortedFeature = np.append(sortedFeature, [sortedFeature.min() - 0.5, sortedFeature.max() + 0.5])
	sortedFeature.sort()
	for j in (1, -1):
	    for k in range(m + 1):
	        theta = (sortedFeature[k] + sortedFeature[k + 1]) / 2
		curError = error(X[:, i], y, j, theta)
	        if minError > curError:
	            minError, feature, bestThreshold, bestS = curError, i, theta, j
    return feature, bestThreshold, bestS, minError

def error(X, y, s, theta):
    m, err = X.shape[0], 0
    for i in range(m):
        if decisionStump(X[i], s, theta) != y[i]:
            err = err + 1
    return err * 1.0 / m

if __name__ == '__main__':
    X_train, y_train = loadDataSet('train.txt')
    X_test, y_test = loadDataSet('test.txt')
    feature, threshold, s, inError = findBestThreshold(X_train, y_train)
    print inError
    print error(X_test[:, feature], y_test, s, threshold)
