import sys
from trainLogistic import TrainLogistic
from testLogistic import TestLogistic

class Logistic(object):
    @staticmethod
    def sample():
        print "sample"

if __name__ == '__main__':
	if(len(sys.argv) != 8):
		print "Enter correct number of arguments...!!!"
		sys.exit()

	trainData = [sys.argv[1] + "/spam/", sys.argv[1] + "/ham/"]
	testData = [sys.argv[2] + "/spam/", sys.argv[2] + "/ham/"]

	eta = float(sys.argv[5])
	lambdaVar = float(sys.argv[6])
	iterations = int(sys.argv[7])

	weightVector = {}
	vocabDict = {}
	if(sys.argv[4].lower() == "yes"):
		weightVector, vocabDict = TrainLogistic.train(trainData, eta, lambdaVar, iterations, sys.argv[3])
	else:
		weightVector, vocabDict = TrainLogistic.train(trainData, eta, lambdaVar, iterations)

	accuracy = TestLogistic.test(testData, weightVector, vocabDict)
	print "Accuracy: ", accuracy