### Using principal component analysis to simplify data
---

- Pros: Reduces complexity of data, indentifies most important features 
- Cons: May not be needed, could throw away useful information- Works with: Numerical values
A short list of reasons of simplify our data:
- Displaying data and results- Making the dataset easier to use- Reducing computational cost of many algorithms- Removing noise- Making the results easier to understand
###### Principal component analysis
the dataset is transformed from its original coordinate system to a new coordinate system.

Pseudocode for transforming out data into the top N principal components:    Remove the mean    Compute the covariance matrix    Find the eigenvalues and eigenvectors of the covariance matrix    Sort the eigenvalues from largest to smallest    Take the top N eigenvectors    Transform the data into the new space created by the top N eigenvectors