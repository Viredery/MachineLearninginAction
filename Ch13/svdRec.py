from numpy import *
from numpy import linalg as la

# Similarity measure

def ecludSim(inA, inB):
    return 1.0 / (1.0 + la.norm(inA - inB))

def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar = 0)[0][1]

def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * (num / denom)

def loadExData():
    return [[1, 1, 1, 0, 0], 
            [2, 2, 2, 0, 0], 
	    [1, 1, 1, 0, 0], 
	    [5, 5, 5, 0, 0], 
	    [1, 1, 0, 2, 2],
	    [0, 0, 0, 3, 3], 
	    [0, 0, 0, 1, 1]]

if __name__ == '__main__':
    myMat = mat(loadExData())
    print ecludSim(myMat[:, 0], myMat[:, 4])
    print ecludSim(myMat[:, 0], myMat[:, 0])
    print cosSim(myMat[:, 0], myMat[:, 4])
    print cosSim(myMat[:, 0], myMat[:, 0])
    print pearsSim(myMat[:, 0], myMat[:, 4])
    print pearsSim(myMat[:, 0], myMat[:, 0])

