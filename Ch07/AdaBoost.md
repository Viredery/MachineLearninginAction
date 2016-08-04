## AdaBoost meta-algorithm
---

Meta-algorithms are a way of combining other algorithms

- Pros: Low generalization error, easy to code, works with most 
  classifiers, no parameters to adjust- Cons: Sensitive to outliers- Works with: Numeric values, nominal values
####### Bagging: building classifiers from randomly resampled data
1. the data is taken from the original dataset S times to make S new datasets.
2. Each dataset is built by randomly selecting an example from the original with replacement.
3. After the S datasets are built, a learning algorithm is applied to each one individually. 
4. When you’d like to classify a new piece of data, you’d apply our S classifiers to the new piece of data and take a majority vote.
###### Boosting
the different classifiers are trained sequentially. Each new classifier is trained based on the performance of those already trained.
the output is calculated from a weighted sum of all classifiers. The weights are based on how successful the classifier was in the previous iteration.
####### Train: improving the classifier by focusing on errors
AdaBoost is short for adaptive boosting.
1. A weight is applied to every example in the training data. We’ll call the weight vector D. Initially, these weights are all equal. 
2. A weak classifier is first trained on the training data.
3. The errors from the weak classifier are calculated, and the weak classifier is trained a second time with the same dataset.
4. This second time the weak classifier is trained, the weights of the training set are adjusted so the examples properly classified the first time are weighted less and the examples incorrectly classified in the first iteration are weighted more.
To get one answer from all of these weak classifiers, AdaBoost assigns *alpha* values to each of the classifiers. 
The *alpha* values are based on the error of each weak classifier. The error *epsilon* is given by

<img src="http://www.forkosh.com/mathtex.cgi? \Large \epsilon=\frac{number\ of\ incorrectly\ classified\ examples}{total\ number\ of\ examples}">
epsilon = number of incorrectly classified examples / total number of examples
and *alpha* is given by
<img src="http://www.forkosh.com/mathtex.cgi? \Large \alpha=\frac{1}{2}\ln(\frac{1 - \epsilon}{\epsilon})">###### Creating a weak learner with a decision stump
    Set the minError to infinite    For every feature in the dataset:        For every step:            For each inequality:                Build a decision stump and test it with the weighted dataset                If the error is less than minError:                    set this stump as the best stump    Return the best stump
###### Implementing the full AdaBoost algorithm
    For each iteration:        Find the best stump using buildStump()        Add the best stump to the stump array        Calculate alpha        Calculate the new weight vector - D        Update the aggregate class estimate        If the error rate == 0.0:            break out of the for loop

###### Test: classifying with AdaBoost
