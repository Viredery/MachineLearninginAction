### Association analysis with the Apriori algorithm
---

- Pros: Easy to code up- Cons: May be slow on large datasets- Works with: Numeric values, nominal values
###### Association analysis
Association analysis is the task of finding interesting relationships in large datasets. 
Two forms: 
- frequent item sets - a collection of items that frequently occur together.
- association rules - a strong relationship exists between two items

support
the percentage of the dataset that contains the itemset.

confidence

###### The Apriori principle

if an itemset is fre- quent, then all of its subsets are frequent.

###### Finding frequent itemsets with the Apriori algorithm

Pseudocode for scanning the dataset

    For each transaction in tran the dataset:
        For each candidate itemset, can:            Check to see if can is a subset of tran            If so increment the count of can    For each candidate itemset:        If the support meets the minimum:            keep this item Return list of frequent itemsets
Pseudocode for the whole Apriori algorithm
    While the number of items in the set is greater than 0:         Create a list of candidate itemsets of length k        Scan the dataset to see if each itemset is frequent         Keep frequent itemsets to create itemsets of length k+1
###### Mining association rules from frequent item sets
The confidence for a rule P ➞ H is defined as support(P | H) /  support(P). (the | symbol is the set union)
