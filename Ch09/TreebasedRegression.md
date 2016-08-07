￼￼### Tree-based regression
---

- Pros: Fits complex, nonlinear data- Cons: Difficult to interpret results- Works with: Numeric values, nominal values
A tree structure modeling the data with piecewise constant segments is known as a regression tree. 
When the models are linear regression equations, the tree is known as a model tree.###### Building trees with continuous and discrete featuresuse a dictionary for the tree data structure

* Feature — A symbol representing the feature split on for this tree.* Value — The value of the feature used to split.* Right — The right subtree; this could also be a single value if the 
  algorithm decides we don’t need another split.* Left — The left subtree similar to the right subtree.
create tree function:
    Find the best feature to split on:        If we cannot split the data, this node becomes a leaf node        Make binary split of the data        Call createTree() on the right split of the data        Call createTree() on the left split of the data
        
###### Using CART for regression

The regression tree method breaks up data using a tree with constant values on the leaf nodes

Pseudo-code for chooseBestSplit function

    For every feature:        For every unique value:            Split the dataset it two            Measure the error of the two splits            If the error is less than bestError:                set bestSplit to this split and update bestError    Return bestSplit feature and threshold
    
###### Tree pruning

prepruning - using the early stopping conditions

postpruning - involving a test set and a training set

    Split the test data for the given tree:        If the either split is a tree:           call prune on that split        Calculate the error associated with merging two leaf nodes        Calculate the error without merging        If merging results in lower error:            merge the leaf nodes
###### Model trees
a piecewise linear model (means that you have a model that consists of multiple linear segments) at each leaf node
