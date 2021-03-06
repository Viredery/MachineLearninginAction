import numpy as np

N = 100 # number of points per class
D = 2 # dimensionality
K = 3 # number of classes
X = np.zeros((N * K, D)) # data matrix (each row = single example)
y = np.zeros(N * K, dtype='uint8') # class labels

for j in xrange(K):
    ix = range(N * j, N * (j + 1))
    r = np.linspace(0.0, 1, N) # radius
    t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2 # theta
    X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
    y[ix] = j

# Training a Softmax Linear Classifier
W = 0.01 * np.random.randn(D, K)
b = np.zeros((1, K))

learn_rate = 1e-0
reg_param = 1e-3
num_examples = X.shape[0]
  
for i in xrange(200):
    scores = np.dot(X, W) + b
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    # correct_logprobs: a 1D array of just the probabilities assigned to the correct classes for each example.
    correct_logprobs = - np.log(probs[range(num_examples), y]) 

    data_loss = np.sum(correct_logprobs) / num_examples
    reg_loss = 0.5 * reg_param * np.sum(W * W)
    loss = data_loss + reg_loss

    if i % 10 == 0:
        print "iteration %d: loss %f" % (i, loss)

    dcorrect_logprobs = 1.0 / num_examples
    dscores = probs
    dscores[range(num_examples), y] -= 1
    dscores = dscores * dcorrect_logprobs
    dW = np.dot(X.T, dscores)
    db = np.sum(dscores, axis=0, keepdims=True)
    dW += reg_param * W

    W += -learn_rate * dW
    b += -learn_rate * db