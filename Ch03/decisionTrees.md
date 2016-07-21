### Decision Trees
---

the ID3 algorithm: tells us how to split the data and when to stop splitting it

- Pros: Computationally cheap to use, easy for humans to understand learned results, missing values OK, can deal with irrelevane features

- Cons: Prone to overfitting, can’t handle numeric values in spite of using continuous values by quantizing them into discrete bins

- Works with: Numeric values, nominal values

the function called createBranch, using recursion.

        If every item in the dataset is in the same class
            return the class label
        Else
            find the best feature to split the data
            split the dataset
            create a branch node
            for each split
                call createBranch and add the result to the branch node
            return branch node

some quantitative way of determining how to split the data. And we use information gain to split it.

**Information gain**

1. decide how to split a dataset using something called information theory.  

   Using information theory, you can measure the information before and after the split.   

   The change in information before and after the split is known as the information gain. The split with the highest information gain is your best option.  

2. [ Another common measure of disorder in a set is the Gini impurity,2 which is the probability of choosing an item from the set and the probability of that item being misclassified. ] 

**Splitting the dataset**

1. create unique lise of class labels
2. calculate entropy for each split
3. find the best information gain  



**Recursively building the tree**  

when stop splitting:  

- The first assumption is that it comes in the form of a list of lists, and all these lists are of equal size  
- The next assumption is that the last column in the data or the last item in each instance is the class label of that instance  


You’ll stop under the following conditions: you run out of attributes on which to split or all the instances in a branch are the same class.  


**Testing and storing the classifier**

test: do recursively until it hits a leaf node; then it will stop because it has arrived at a conclusion.  

store: use module *pickle* to serialize the decision tree for persisting.  