supervised learning - when we specify a target variable, the machine can learn from our data.  

- divine some pattern from the input data to get the target variable
- two cases of the target variable: nominal values and numeric values

classification algorithm

- k-Nearest Neighbors
- decision tree
- Naive Bayes
- logistic regression
- support vector machine
- AdaBoost


#### Classifying with k-Nearest Neighbors  

instance-based learning

- Pros: High accuracy, insensitive to outliers, no assumptions about data

- Cons: Computationally expensive, requires a lot of memory, cannot give you any idea of the underlying structure of the data.  

- Works with: Numeric values, nominal values

*putting the kNN classification algorithm into action*  

    # the input vector to classify called inX
    # calculate the distances using the Euclidian distance
    For every point in the dataset we need to classify:
        calculate the distance between inX and the current point
        sort the distances in increasing order
        take k items with lowest distances to inX
        find the majority class among these items
        return the majority class as our prediction for the class of inX

###### *Prepare: normalizing numeric values*  

When dealing with values that lie in different ranges, it’s common to normalize them.  

###### *Test: testing the classifier as a whole program*

One common task in machine learning is evaluating an algorithm’s accuracy.

error rate - add up the number of times the classifier was wrong and divide it by the total number of tests.

the results will vary by algorithm, dataset, and settings

One way you can use the existing data is to take some portion, say 90%, to train the classifier. Then you’ll take the remaining 10% to test the classifier and see how accurate it is.

###### *Use: putting together a useful system*  
