###￼ Efficiently finding frequent itemsets with FP-growth
---

- Pros: Usually faster than Apriori.- Cons: Difficult to implement; certain datasets degrade the performance.- Works with: Nominal values.


Build the FP-tree.  Mine frequent itemsets from the FP-tree.
###### FP-trees: an efficient way to encode a dataset
To build the tree, you scan the original dataset twice.
The first pass counts the frequency of occurrence of all the items.  If an item is infrequent, supersets containing that item will also be infrequent, so you don’t have to worry about them. 
You use the first pass to count the frequency of occurrence and then address only the frequent items in the second pass.
###### Build an FP-tree

1. Creating the FP-tree data structure
2. Constructing the FP-tree

###### Mining frequent items from an FP-tree

1. Get conditional pattern bases from the FP-tree.2. From the conditional pattern base, construct a conditional FP-tree.3. Recursively repeat steps 1 and 2 on until the tree contains a single item.