### Predicting numeric values: regression
---

- Pros: Easy to interpret results, computationally inexpensive
- Cons: Poorly models nonlinear data- Works with: Numeric values, nominal values
###### Finding best-fit lines with linear regression

<img src="http://www.forkosh.com/mathtex.cgi? \Large w=(X^\mathrm{T}X)^{-1}X^\mathrm{T}y">the squared error:
<img src="http://www.forkosh.com/mathtex.cgi? \Large \sum_{i=1}^m (y_i - x_i^\mathrm{T}w)^2">
###### Locally weighted linear regression

<img src="http://www.forkosh.com/mathtex.cgi? \Large w=(X^\mathrm{T}WX)^{-1}X^\mathrm{T}Wy">###### Shrinking coefficients to understand our data

1. Ridge regression

   <img src="http://www.forkosh.com/mathtex.cgi? \Large w=(X^\mathrm{T}X+\lambda I)^{-1}X^\mathrm{T}y">
   Shrinkage methods allow us to throw out unimportant parameters 
   Shrinkage can give us a better prediction value than linear regression.

2. Forward stagewise regression
   This algorithm is a greedy algorithm in that at each step it makes the decision that will reduce the error the most at that step. 
        Regularize the data to have 0 mean and unit variance        For every iteration:            Set lowestError to infinite For every feature:            For increasing and decreasing:                Change one coefficient to get a new W                Calculate the Error with new W                If the Error is lower than lowestError:                     set Wbest to the current W            Update set W to Wbest
###### The bias/variance tradeoff
errors as a sum of three components: bias, error, and ran- dom noise.
Shrinkage methods can also be viewed as adding bias to a model and reducing the variance.