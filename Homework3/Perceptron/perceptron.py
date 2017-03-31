import sys
import random
from trainPerceptron import TrainPerceptron
from testPerceptron import TestPerceptron

class Perceptron(object):
    @staticmethod
    def sample():
        print "sample"

if __name__ == '__main__':
	# python perceptron.py train test eta iterations stopwords.txt yes
	if(len(sys.argv) != 7):
		print "Enter correct number of arguments...!!!"
		sys.exit()

	trainData = [sys.argv[1] + "/spam/", sys.argv[1] + "/ham/"]
	testData = [sys.argv[2] + "/spam/", sys.argv[2] + "/ham/"]
	eta = float(sys.argv[3])
	iterations = int(sys.argv[4])


	if(sys.argv[6].lower() == "yes"):
		weightVector = TrainPerceptron.train(trainData, eta, iterations, sys.argv[5])
	else:
		weightVector = TrainPerceptron.train(trainData, eta, iterations)
	
	accuracy = TestPerceptron.test(testData, weightVector)
	print "Acc: ", accuracy