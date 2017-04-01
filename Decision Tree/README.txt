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
python decision.py <training-set> <test-set> <to-print>
to-print:{yes,no}

Example: ./program training_set.csv test_set.csv yes

------------------------------------------------------------------------------------

Description:
Decision Tree
1 Class:
Node class to store tree nodes

10 Functions:
1. selectBestAttribute(examples, targetAttribute, attributes):
This function will calculate the best attribute by analysing the information gains

2. id3(examples, targetAttribute, attributes):
This function implements the algorithm

3. readDataMatrix(path):
It reads the data from the provided path

4. calcEntropy(datasetMatrix, column, value, classColumn):
It calculates the entropy

5. calcInitialEntropy(datasetMatrix, classColumn):
It calculates the initial entropy

6. calcGain(datasetMatrix, entropy, column, classColumn):
This calculates the information gain of the given column

7. calcVariance(datasetMatrix, column, value, classColumn):
It calculates the Variance

8. calcInitialVariance(datasetMatrix, classColumn):
It calculates the initial Variance

9. calcGain(datasetMatrix, Variance, column, classColumn):
This calculates the information gain of the given column

10. printTree() - To print Tree

11. calculateAccuracy() - To calculate Accuracy
------------------------------------------------------------------------------------

Output:
The tree will be printed on the prompt if user has given input yes and the accuracies will be written in the accuracy.txt

------------------------------------------------------------------------------------





