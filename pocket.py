import numpy as np

def loadDataSet2(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split()
	features = [1.0]
	features.extend([float(num) for num in lineArr])
	dataMat.append(features)
    return np.array(dataMat)

def loadDataSet(fileName):
    dataMat, labelMat = [], []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split()
	features = [1.0]
	features.extend([float(num) for num in lineArr[:-1]])
	dataMat.append(features)
	labelMat.append(int(lineArr[-1]))
    return np.array(dataMat), np.array(labelMat)

def signFunc(inX):
    if inX <= 0:
        return -1
    else:
        return 1

def pocketAlgo(dataMat, labelMat, learningRate, iteration):
    m, n = dataMat.shape
    w = np.zeros(n)
    wPocket = w
    numUpdates = 0
    numUpdates, index, numCorrect = 0, 0, 0
    while numUpdates < iteration:
	if signFunc(np.dot(w, dataMat[index])) != labelMat[index]:
	    w = w + learningRate * labelMat[index] * dataMat[index]
	    numUpdates, numCorrect = numUpdates + 1, 0
	    if errorCalc(w, dataMat, labelMat) < errorCalc(wPocket, dataMat, labelMat):
	        wPocket = w
	numCorrect, index = numCorrect + 1, (index + 1) % m
        if numCorrect == m:
	    break
    print "the number of updates is " + str(numUpdates)
    return wPocket, numUpdates

def errorCalc(w, X, y):
    n = len(y)
    errorNum = 0
    for i in range(n):
        if signFunc(sum(X[i] * w)) != y[i]:
	    errorNum = errorNum + 1
    return errorNum * 1.0 / n

if __name__ == '__main__':
    dataMat = loadDataSet2('pocketTrain.txt')
    X_test, y_test = loadDataSet('pocketTest.txt')
    totalErrorRate = 0
    for _ in range(1000):
        np.random.shuffle(dataMat)
	y_all = dataMat[:, -1]
	X_all = dataMat[:, :-1]
	y_all = y_all.astype(int)
        weights, numUpdates = pocketAlgo(X_all, y_all, 1, 100)
        print errorCalc(weights, X_test, y_test)
        totalErrorRate = totalErrorRate + errorCalc(weights, X_test, y_test)
    
    print "the average error is " + str(totalErrorRate / 1000)
