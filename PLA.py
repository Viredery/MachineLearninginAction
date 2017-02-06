import numpy as np

def loadDataSet2():
    dataMat = []
    fr = open('data.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
	features = [1.0]
	features.extend([float(num) for num in lineArr])
	dataMat.append(features)
    return np.array(dataMat)

def loadDataSet():
    dataMat, labelMat = [], []
    fr = open('data.txt')
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

def stocGradDescent(dataMat, labelMat, learningRate):
    m, n = dataMat.shape
    w = np.zeros(n)
    numUpdates = 0
    numUpdates, index, numCorrect = 0, 0, 0
    while True:
	if signFunc(np.dot(w, dataMat[index])) != labelMat[index]:
	    w = w + learningRate * labelMat[index] * dataMat[index]
	    numUpdates, numCorrect = numUpdates + 1, 0
	numCorrect, index = numCorrect + 1, (index + 1) % m
	if numCorrect == m:
	    break
    print "the number of updates is " + str(numUpdates)
    return w, numUpdates

if __name__ == '__main__':
    # visit examples in the naive cycle using the order of examples in the data set
    #X_all, y_all = loadDataSet()
    #weights, numUpdates = stocGradDescent(X_all, y_all, 1)
    
    # visit examples in the fixed, pre-determined random cycles
    dataMat = loadDataSet2()
    totalNumUpdates = 0
    for _ in range(2000):
        np.random.shuffle(dataMat)
	y_all = dataMat[:, -1]
	X_all = dataMat[:, :-1]
	X_all = np.column_stack((X_all, np.ones(len(y_all))))
	y_all = y_all.astype(int)
	
        weights, numUpdates = stocGradDescent(X_all, y_all, 0.5)
	totalNumUpdates = totalNumUpdates + numUpdates
    
    print "the average number of updates is " + str(totalNumUpdates / 2000)
