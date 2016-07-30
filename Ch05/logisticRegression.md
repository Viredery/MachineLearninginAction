### Logisric regression
---

Logistic regression is finding best-fit parameters to a nonlinear function called the sig- moid. 

- Pros: Computationally inexpensive, easy to implement, knowledge representation easy to interpret
- Cons: Prone to underfitting, may have low accuracy 
- Works with: Numeric values, nominal values
###### Classification with logistic regression and the sigmoid function
sigmoid function
    1 / ( 1 + e ^ ( -z ) )
    At 0 the value of the sigmoid is 0.5. For increasing values of x, the sigmoid will approach 1, and for decreasing values of x, the sigmoid will approach 0. 
For the logistic regression classifier we’ll take our features and multiply each one by a weight and then add them up. This result will be put into the sigmoid, and we’ll get a number between 0 and 1. 
###### using optimization to find the best regression coefficients
z = w0x0 + w1x1 + w2x2 + ... + wnxnGradient ascent
   if we want to find the maximum point on a func- tion, then the best way to move is in the direction of the gradient.
   gradient: ▽f(x,y)
   The gradient operator will always point in the direction of the greatest increase.

###### Prepare: dealing with missing values in the data

- Use the feature's mean value from all the available data
- Fill in the unknown with a special value like -1
- Ignore the instance
- Use a mean value from similar items
- Use another machine learning algorithm to predict the value
###### Train: using gradient ascent to find the best parameters
Pseudocode for the gradient ascent
    Start with the weights all set to 1    Repeat R number of times:
        Calculate the gradient of the entire dataset
        Update the weights vector by alpha * gradient
        Return the weights vector
        
###### Train: stochastic gradient ascent

an example of an online learning algorithm

An alternative to this method is to update the weights using only one instance at a time.

    Start with the weights all set to 1
    For each piece of data in the dataset:
         Calculate the gradient of one piece of data
         Update the weights vector by alpha * gradient
         Return the weights vector