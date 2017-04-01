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
Steps to execute:
$python logisticRegression.py <train-folder> <test-folder> <stopwords-file> <yes/no> <eta> <lambda> <iterations>
python logisticRegression.py train test stopwords.txt yes 0.49 0.002 10 

$python perceptron.py <train-folder> <test-folder> <eta> <iterations> <stopwords-file> <yes>
python perceptron.py train test 0.04 10 stopwords.txt yes

------------------------------------------------------------------------------------
Description:
There are 6 files

logisticRegression.py - calls train and test data and prints the accuracy
trainLogistic.py - returns the weightVector for testing
testLogistic.py - returns the accuracy

perceptron.py - calls train and test data and prints the accuracy
testPerceptron.py - returns the weightVector for testing
trainPerceptron.py - returns the accuracy

------------------------------------------------------------------------------------
