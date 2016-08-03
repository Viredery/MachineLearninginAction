### Support vector machines
---

- Pros: Low generalization error, computationally inexpensive, easy to interpret results

- Cons: Sensitive to tuning parameters and kernel choice; natively only handles binary classification

- Works with: Numeric values, nominal values


implementation:  

1. the sequential minimal optimazation (SMO) algorithm  
2. *kernels* function to extend SVMs to a larger number of datasets  

support vectors:  
The points closest to the separating hyperplane.

** Find the maximum margin **  

find the points with the smallest margin, we must maximize that margin:  

<img src="http://www.forkosh.com/mathtex.cgi? \arg\max_{\omega, b}\{\min_n(label*(\omega^\mathrm{T}{x}+b))*\frac{1}{||\omega||}\}">

subject to the following constraints:

<img src="http://www.forkosh.com/mathtex.cgi? label*(\omega^\mathrm{T}{x}+b) \geq 1.0">

solution:  

using Lagrange multiplier and slack variable.

###### Efficient optimization with the SMO algorithm

Here’s how the SMO algorithm works:
 
    it chooses two alphas to optimize on each cycle. Once a suitable pair of alphas is found, one is increased and one is decreased. To be suitable, a set of alphas must meet certain criteria. One criterion a pair must meet is that both of the alphas have to be outside their margin boundary. The second criterion is that the alphas aren’t already clamped or bounded.
    
Pseudocode:  

    Create an alphas vector filled with 0s    While the number of iterations is less than MaxIterations:        For every data vector in the dataset: 
            If the data vector can be optimized:                Select another data vector at random                Optimize the two vectors together                If the vectors can’t be optimized:                    break            If no vectors were optimized:                increment the iteration count
                
###### Speeding up optimization with the full Platt SMO
The only difference from simplified SMO is how we select which alpha to use in the optimization. The full Platt uses some heuristics that increase the speed. 
1. The Platt SMO algorithm has an outer loop for choosing the first alpha. This alternates between single passes over the entire dataset and single passes over non-bound alphas.  
2. The second alpha is chosen using an inner loop after we’ve selected the first alpha. This alpha is chosen in a way that will maximize the step size during optimization. ###### Mapping data to higher dimensions with kernels
solving this linear problem in high-dimensional space, which is equivalent to solving a nonlinear problem in low-dimensional space.
radial bias function