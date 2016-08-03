### Logisric regression
---

Logistic regression is finding best-fit parameters to a nonlinear function called the sig- moid. 

- Pros: Computationally inexpensive, easy to implement, knowledge representation easy to interpret













###### Prepare: dealing with missing values in the data

- Use the feature's mean value from all the available data
- Fill in the unknown with a special value like -1
- Ignore the instance
- Use a mean value from similar items
- Use another machine learning algorithm to predict the value



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