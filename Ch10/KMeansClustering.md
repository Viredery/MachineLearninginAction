### Grouping unlabeled items using k-means clustering
---

it finds k unique clusters, and the center of each cluster is the mean of the values in that cluster.

- Pros: Easy to implement- Cons: Can converge at local minima; slow on very large datasets- Works with: Numeric values
###### The k-means clustering algorithm
pseudo-code:    Create k points for starting centroids (often randomly)     While any point has changed cluster assignment        for every point in our dataset:             for every centroid                calculate the distance between the centroid and point            assign the point to the cluster with the lowest distance        for every cluster            calculate the mean of the points in that cluster and assign the centroid to the mean
###### Improving cluster performance with postprocessing
One metric for the quality of your cluster assignments you can use is the SSE, or sum of squared error.
A lower SSE means that points are closer to their centroids.
One sure way to reduce the SSE is to increase the number of clusters. This defeats the purpose of clustering, so assume that you have to increase the quality of your clusters while keeping the number of clusters constant.
To get your cluster count back to the original value, you could merge two clusters.
Two quantifiable ideas are merging the closest centroids or merging the two centroids that increase the total SSE the least.
###### Bisecting k-means
Pseudocode
    Start with all the points in one cluster     While the number of clusters is less than k        for every cluster            measure total error            perform k-means clustering with k=2 on the given cluster             measure total error after k-means has split the cluster in two        choose the cluster split that gives the lowest error and commit this split
