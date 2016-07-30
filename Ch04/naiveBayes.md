### Naive Bayes
---

- Pros: Works with a small amount of data, handles multiple classes  

- Cons: Sensitive to how the input data is prepared  - Works with: Nominal values

Bayesian decision theory: choosing the decision with the highest probability [Classifying with conditional probabilities].  

It’s called naive because the formulation makes some naive assumptions.

1. independence among the features
2. every feature is equally important###### Classifying text with Python
aim: split up the text to get features
reduce every piece of text to a vector of tokens(features) where 1 represents the token existing in the document and 0 represents that it isn’t present.  ###### Prepare: making word vectors from text

text-parsing: create a list of all the unique words in all of our documents.

treated the presence or absence of a word as a feature. This could be described as a set-of-words model.  

If a word appears more than once in a document, that might convey some sort of information about the document over just the word occurring in the document or not. This approach is known as a bag-of-words model. 
###### Train: calculating probabilities from word vectors

calculate p(c) and p(w|c), that is, p(w1w2...wn|ci)
    Count the number of documents in each class    for every training document:
        for each class:
            if a token appears in the document:
                increment the count for that token
            increment the count of tokens
        for each class:
            for each token:
                divide the token count by the total token count 
                to get conditional probabilities
        return conditional probabilities for each class    
###### Test: modifying the classifier for real-world conditions

when multiplying a lot of probabilities together to get the probability that a document belongs to a given class

1. if any of these numbers are 0, when we multipy them together we get 0
   -> initialize all of our occurrence counts to 1 and the denominators 
   to 2


2. many of these numbers are very small, we’ll get underflow, or an 
   incorrect answer -> take the natural logarithm
