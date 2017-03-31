# import modules
import csv
import math
import copy

# read csv file
datafile = open('dataset 1/dataset 1/training_set1.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
mydata, data, columns, classColumn = [], [], [], []
count, columnLength = 0, 0
columnDict = {}

# read csv file into columns
for row in datareader:
    if(count == 0):
        row1 = map(str, row[0].split(','))
        columnList = row1
        for item in row1:
            columnDict[item] = 0
        columnLength = len(row1)
        columns = row1
        del columns[len(columns) - 1]
        value_to_remove = 'Class'
        columnDict = {key: value for key, value in columnDict.items() if value is not value_to_remove}
    elif(count != 0):
        row1 = map(int, row[0].split(','))
        data.append(row1)
    count = count + 1

# assigning values to variables
mydata = zip(*data)
classColumn = list(mydata[columnLength - 1])
zeroCount = classColumn.count(0)
oneCount = classColumn.count(1)

# handle this condition on priority
if(zeroCount == 0):
	print "Only one root node: 1"
if(oneCount == 0):
	print "Only one root node: 0"
if(not mydata):
	if(oneCount > zeroCount):
		print "1"
	else:
		print "0"

def calcEntropy(a, b):
	term1, term2 = 0, 0
	if(a == 0):
		term1 = 0
	else:
		term1 = (a / float(a + b)) * math.log(a / float(a + b), 2)
	if(b == 0):
		term2 = 0
	else:
		term2 = (b / float(a + b)) * math.log(b / float(a + b), 2)
	return (-term1-term2)

entropy = calcEntropy(zeroCount, oneCount)
print "Entropy: " + str(entropy)

# initial information gain
def infoGain(entropy, index):
	del mydata[index - 1]
	gains = []
	maxGain = 0
	index = -1
	for column in mydata:
		length = len(column)
		zeroCount = column.count(0)
		oneCount = column.count(1)
		oneOneCount, oneZeroCount, zeroOneCount, zeroZeroCount = 0, 0, 0, 0
		for i in xrange(len(column)):
			if(column[i] == 1):
				if(classColumn[i] == 1):
					oneOneCount = oneOneCount + 1
				else:
					oneZeroCount = oneZeroCount + 1
			else:
				if(classColumn[i] == 0):
					zeroZeroCount = zeroZeroCount + 1
				else:
					zeroOneCount = zeroOneCount + 1
		
		term1, term2 = 0, 0
		
		#zeroZeroCount
		# if(zeroZeroCount == 0):
		# 	term1 = 0
		# else:
		# 	term1 = (-1) * (zeroZeroCount / float(zeroCount)) * math.log(zeroZeroCount / float(zeroCount), 2)
		# if(zeroOneCount == 0):
		# 	term2 = 0
		# else:
		# 	term2 = (zeroOneCount / float(zeroCount)) * math.log(zeroOneCount / float(zeroCount), 2)
		# zeroEntropy = term1 - term2
		zeroEntropy = calcEntropy(zeroZeroCount, zeroOneCount)

		#oneZeroCount
		if(oneZeroCount == 0):
			term1 = 0
		else:
			term1 = (-1) * (oneZeroCount / float(oneCount)) * math.log(oneZeroCount / float(oneCount), 2)
		if(oneOneCount == 0):
			term2 = 0
		else:
			term2 = (oneOneCount / float(oneCount)) * math.log(oneOneCount / float(oneCount), 2)
		oneEntropy = term1 - term2
		
		#zeroCount and oneCount
		if(zeroCount == 0):
			term1 = 0
		else:
			term1 = ((zeroCount / float(zeroCount + oneCount)) * zeroEntropy)
		if(oneCount == 0):
			term2 = 0
		else:	
			term2 = ((oneCount / float(zeroCount + oneCount)) * oneEntropy)
		newGain = entropy - term1 - term2
		gains.append(newGain)
		if(maxGain < newGain):
			maxGain = newGain
			index = gains.index(maxGain)
	index = gains.index(max(gains))
	print "Gains: " + str(gains)
	print "Max Gain: " + str(max(gains))
	print "Index of Column: " + str(index)
	print ""
	return index
index = infoGain(entropy, columnLength)




# Recursive part 
def buildTree(currentData, currentIndex, listOfColumns):
	print "Current Data: ", len(currentData), "\nIndex: ", currentIndex
	maxGainColumn = currentData[currentIndex]
	del currentData[currentIndex]
	del listOfColumns[currentIndex]
	print listOfColumns
	
	count1, count2, count3, count4 = 0, 0, 0, 0
	for i in range(len(maxGainColumn)):
		if(maxGainColumn[i] == 0 and classColumn[i] == 0):
			count1 = count1 + 1
		elif(maxGainColumn[i] == 0 and classColumn[i] == 1):
			count2 = count2 + 1
		elif(maxGainColumn[i] == 1 and classColumn[i] == 0):
			count3 = count3 + 1
		elif(maxGainColumn[i] == 1 and classColumn[i] == 1):
			count4 = count4 + 1

	entropyZero = -(((count1/float(count1+count2)) * math.log(count1/float(count1+count2), 2)) + ((count2/float(count1+count2)) * math.log(count2/float(count1+count2), 2)))
	entropyOne = -(((count3/float(count3+count4)) * math.log(count3/float(count3+count4), 2)) + ((count4/float(count3+count4)) * math.log(count4/float(count3+count4), 2)))
	print "Entropy Zero: " + str(entropyZero) + "\nEntropy One: "+ str(entropyOne)
	# term2 = (((count1+count2)/float(count1+count2+count3+count4))*entropyZero) + (((count1+count2)/float(count1+count2+count3+count4)) * entropyOne)
	# print "Term2: " + str(term2)
	# print str(entropy - term2)

	#entropyZero from column
	igZero, igOne = [], []
	for column in currentData:
		var1, var2, var3, var4 = 0, 0, 0, 0
		for i in range(len(column)):
			if(maxGainColumn[i] == 0 and column[i] == 0 and classColumn[i] == 0):
				var1 = var1 + 1
			elif(maxGainColumn[i] == 0 and column[i] == 0 and classColumn[i] == 1):
				var2 = var2 + 1
			elif(maxGainColumn[i] == 0 and column[i] == 1 and classColumn[i] == 0):
				var3 = var3 + 1
			elif(maxGainColumn[i] == 0 and column[i] == 1 and classColumn[i] == 1):
				var4 = var4 + 1
		
		# term1, term2 = 0, 0
		# if(var1 == 0):
		# 	term1 = 0
		# else:
		# 	term1 = ((var1/float(var1+var2)) * math.log(var1/float(var1+var2), 2))
		# if(var2 == 0):
		# 	term2 = 0
		# else:
		# 	term2 = ((var2/float(var1+var2)) * math.log(var2/float(var1+var2), 2))
		ent0 = calcEntropy(var1, var2)
		
		# term1, term2 = 0, 0
		# if(var3 == 0):
		# 	term1 = 0
		# else:
		# 	term1 = ((var3/float(var3+var4)) * math.log(var3/float(var3+var4), 2))
		# if(var4 == 0):
		# 	term2 = 0
		# else:
		# 	term2 = ((var4/float(var3+var4)) * math.log(var4/float(var3+var4), 2))
		ent1 = calcEntropy(var3, var4)
		
		ig0 = entropyZero - ((count1 / float(count1 + count2)) * ent0) - ((count2 / float(count1 + count2)) * ent1)
		
		# print ent0 # print var1 # print var2 # print var3 # print var4 # print ""
		var1, var2, var3, var4 = 0, 0, 0, 0
		for i in range(len(column)):
			if(maxGainColumn[i] == 1 and column[i] == 0 and classColumn[i] == 0):
				var1 = var1 + 1
			elif(maxGainColumn[i] == 1 and column[i] == 0 and classColumn[i] == 1):
				var2 = var2 + 1
			elif(maxGainColumn[i] == 1 and column[i] == 1 and classColumn[i] == 0):
				var3 = var3 + 1
			elif(maxGainColumn[i] == 1 and column[i] == 1 and classColumn[i] == 1):
				var4 = var4 + 1
		# term1, term2 = 0, 0
		# if(var1 == 0):
		# 	term1 = 0
		# else:
		# 	term1 = ((var1/float(var1+var2)) * math.log(var1/float(var1+var2), 2))
		# if(var2 == 0):
		# 	term2 = 0
		# else:
		# 	term2 = ((var2/float(var1+var2)) * math.log(var2/float(var1+var2), 2))
		# ent0 = -(term1 + term2)
		ent0 = calcEntropy(var1, var2)
		
		# term1, term2 = 0, 0
		# if(var3 == 0):
		# 	term1 = 0
		# else:
		# 	term1 = ((var3/float(var3+var4)) * math.log(var3/float(var3+var4), 2))
		# if(var4 == 0):
		# 	term2 = 0
		# else:
		# 	term2 = ((var4/float(var3+var4)) * math.log(var4/float(var3+var4), 2))
		ent1 = calcEntropy(var3, var4)
		
		ig1 = entropyZero - ((count1 / float(count1 + count2)) * ent0) - ((count2 / float(count1 + count2)) * ent1)
		# print ent1 # print var1 # print var2 # print var3 # print var4
		# print "Information Gains" # print ig0 # print ig1
		
		igZero.append(ig0)
		igOne.append(ig1)

	print igZero
	print igOne
	print "\nChildren"
	print max(igZero)
	print max(igOne), "\n"

	print "Zero List: " + str(len(igZero))
	print "One List: ", len(igOne) 
	indexZero = igZero.index(max(igZero))
	indexOne = igOne.index(max(igOne))
	print listOfColumns[igZero.index(max(igZero))]
	print listOfColumns[igOne.index(max(igOne))]
	if(len(currentData) > indexZero and indexZero >= 1):
	 	print "CurrentData Length: ", len(currentData), " ", "IndexZero: ", indexZero
	 	buildTree(currentData, indexZero, listOfColumns)
	if(len(currentData) > indexOne and indexOne >= 1): 	
		print "CurrentData Length: ", len(currentData), " ", "IndexOne: ", indexOne
	 	buildTree(currentData, indexOne, listOfColumns)

buildTree(copy.deepcopy(mydata), index, copy.deepcopy(columns))