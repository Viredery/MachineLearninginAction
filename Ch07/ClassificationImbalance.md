### Classification imbalance
---

The classification imbalance problem is training a classifier with data that doesn’t have an equal number of positive and negative examples. The problem also  from positive and negative examples.

###### Alternative performance metrics: precision, recall, and ROC

confusion matrix

Precision = TP / (TP + FP)the fraction of records that were posi- tive from the group that the classifier predicted to be positive. 
Recall = TP / (TP + FN)
the fraction of positive examples the classifier got right.
ROC curve: compare classifiers and make cost-versus-benefit deci- sions.
###### Manipulating the classifier’s decision with a cost function
cost-sensitive learning
There are many ways to include the cost information in classification algorithms.
1. In AdaBoost, you can adjust the error weight vexists when the costs for misclassification are differentector D based on the cost function. 
2. In naïve Bayes, you could predict the class with the lowest expected cost instead of the class with the highest probability. 
3. In SVMs, you can use different C parameters in the cost function for the different classes.
###### Data sampling for dealing with classification imbalance
* Oversample means to duplicate examples
* Undersample means to delete examples.

The sampling can be done either randomly or in a predetermined fashion.