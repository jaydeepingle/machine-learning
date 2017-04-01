Name	: Jaydeep Digambar Ingle
B-Number: B00671052
Email	: jingle1@binghamton.edu

------------------------------------------------------------------------------------
Academic Honesty Statement:
I have done this assignment completely on my own. I have not copied it, nor have
I given my solution to anyone else. I understand that if I am involved in
plagiarism or cheating I will have to sign an official form that I have cheated
and that this form will be stored in my official university record. I also
understand that I will receive a grade of 0 for the involved assignment for my
first offense and that I will receive a grade of “F” for the course for any
additional offense.
-Jaydeep Digambar Ingle

------------------------------------------------------------------------------------

Step to execute:
1. Post Pruning Algorithm
python program.py <L> <K> <training-set> <validation-set> <test-set> <to-print>
e.g. python decision.py 5 6 training_set.csv validation_set.csv test_set.csv yes

2. Naive Bayes
python program.py <train-folder-name> <test-folder-name> <stopwords-file>
<yes/no>
e.g. python naiveBayes.py train test stopwords.txt yes
------------------------------------------------------------------------------------
Description:
Code is seprated in 2 folders
There are multiple files as follows
1. Post Pruning
    decision.py : Main file which builds the tree and calls postPruning
    algorithm
    postPruning.py : Prunes the tree with respect to L and K
    readData.py : Reads the data from the csv and returns 2D matrix
    entropy.py : Deals with the entropy
    variance.py : Deals with the variance
    node.py : Deals with the tree node
    tree.py : Deals with the functions related to tree

2. Naive Bayes
    naiveBayes.py : It calls 2 modules Train and Apply
    trainMultiNB.py : It implements trainMultinomialNB
    applyMultiNB.py : It implements applyMultinomialNB

3. ExtraCredit
    This part deals with the stopwords filtering
    Accuracy may increase or decrease. It depends on the number of stopwords
    present in the dataset. If there are no stopwords in the dataset the
    accuracy is going to be same. 
    Also if training data contains less stopwords and test contains more or vice
    versa the accuracy will be either greater or less than the accuracy without
    the stopwords

------------------------------------------------------------------------------------
Output:
The tree will be printed on the prompt if user has given input yes and the accuracies will be written in the accuracy.txt
------------------------------------------------------------------------------------
