from math import log
import operator

def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# Function to calculate the Shannon entropy of a dataset
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
	if currentLabel not in labelCounts.keys():
	    labelCounts[currentLabel] = 0
	labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
	prob = float(labelCounts[key]) / numEntries
	shannonEnt -= prob * log(prob, 2)
    return shannonEnt

# Dataset splitting on a given feature
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
	    reducedFeatVec.extend(featVec[axis + 1:])
	    retDataSet.append(reducedFeatVec)
    return retDataSet

# Choosing the best feature to split on
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
	uniqueVals = set(featList)
	newEntropy = 0.0
	for value in uniqueVals:
	    subDataSet = splitDataSet(dataSet, i, value)
	    prob = len(subDataSet) / float(len(dataSet))
	    newEntropy += prob * calcShannonEnt(subDataSet)
	infoGain = baseEntropy - newEntropy
	if (infoGain > bestInfoGain):
	    bestInfoGain = infoGain
	    bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
	    classCount[vote] = 0
	classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
        key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

# Tree-building code
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # Stop when all classes are equal
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # When no more features, return majority
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
	myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

# Classification function for an existing decision tree
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
	    if type(secondDict[key]).__name__ == 'dict':
	        classLabel = classify(secondDict[key], featLabels, testVec)
	    else:
	        classLabel = secondDict[key]
    return classLabel

def handleLensesExample():
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lensesTree = createTree(lenses, lensesLabels)
    return lensesTree

# Methods for persisting the decision tree with pickle
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

if __name__ == '__main__':
    print handleLensesExample()
    
