
#while (len(mydata) != 1):
# maxGainColumn = mydata[index]
# #print str(maxGainColumn)
# del mydata[index]
# # 0 and 1 are only the distinct values
# for column in mydata:
# 	oneOneCount, oneZeroCount, zeroZeroCount, zeroOneCount = 0, 0, 0, 0
# 	classOneOneCount, classOneZeroCount, classZeroZeroCount, classZeroOneCount = 0, 0, 0, 0
# 	columnOneOneCount, columnOneZeroCount, columnZeroZeroCount, columnZeroOneCount = 0, 0, 0, 0
	
# 	maxGainOneCount = maxGainColumn.count(1)
# 	maxGainZeroCount = maxGainColumn.count(0)

# 	print "MaxGainOneCount: " + str(maxGainOneCount)
# 	print "MaxGainZeroCount: " + str(maxGainZeroCount)

# 	# calculate entropy of sunny wrt to class column, 1 wrt to class column
# 	# print classColumn
# 	for i in xrange(len(classColumn)):
# 		if(maxGainColumn[i] == 1):
# 			if(classColumn[i] == 1):
# 				classOneOneCount = classOneOneCount + 1
# 			else:
# 				classOneZeroCount = classOneZeroCount + 1
# 		else:
# 			if(classColumn[i] == 0):
# 				classZeroZeroCount = classZeroZeroCount + 1
# 			else:
# 				classZeroOneCount = classZeroOneCount + 1
# 	print "Class to E"
# 	print "1: " + str(classOneOneCount) + " " + str(classOneZeroCount) + " 0: " + str(classZeroOneCount) + " " + str(classZeroZeroCount)

# 	# Entropy
# 	entropyOne = 0
# 	entropyZero = 0
# 	if(maxGainOneCount == 0):
# 		entropyOne = 0
# 	else:
# 		entropyOne = -(classOneOneCount / float(maxGainOneCount)) * math.log(classOneOneCount / float(maxGainOneCount), 2)-(classOneZeroCount / float(maxGainOneCount)) * math.log(classOneZeroCount / float(maxGainOneCount), 2)
# 	if(maxGainZeroCount == 0):
# 		entropyZero = 0
# 	else:
# 		entropyZero = -(classZeroOneCount / float(maxGainZeroCount)) * math.log(classZeroOneCount / float(maxGainZeroCount), 2)-(classZeroZeroCount / float(maxGainZeroCount)) * math.log(classZeroZeroCount / float(maxGainZeroCount), 2)


# 	# calculate the terms for 0 and 1
# 	for i in xrange(len(column)):
# 		if(maxGainColumn[i] == 1):
# 			if(column[i] == 1):
# 				oneOneCount = oneOneCount + 1
# 			else:
# 				oneZeroCount = oneZeroCount + 1
# 		else:
# 			if(column[i] == 0):
# 				zeroZeroCount = zeroZeroCount + 1
# 			else:
# 				zeroOneCount = zeroOneCount + 1
# 	print "E to Columns"
# 	print str(oneOneCount) + " " + str(oneZeroCount) + " " + str(zeroZeroCount) + " " + str(zeroOneCount)

# 	for i in xrange(len(column)):
# 		if(maxGainColumn[i] == 0 and column[i] == 0 and classColumn[i] == 0):
# 				columnZeroZeroCount = columnZeroZeroCount + 1
# 		elif(maxGainColumn[i] == 0 and column[i] == 0 and classColumn[i] == 1):
# 				columnZeroOneCount = columnZeroOneCount + 1
# 		elif(maxGainColumn[i] == 1 and column[i] == 0 and classColumn[i] == 0):
# 				columnOneZeroCount = columnOneZeroCount + 1
# 		elif(maxGainColumn[i] == 1 and column[i] == 0 and classColumn[i] == 1):
# 				columnOneOneCount = columnOneOneCount + 1

# 	print "A to Class"
# 	print str(columnOneOneCount) + " " + str(columnOneZeroCount) + " " + str(columnZeroOneCount) + " " + str(columnZeroZeroCount)
# 	columnOneCount = columnOneOneCount + columnOneZeroCount
# 	columnZeroCount = columnZeroOneCount + columnZeroZeroCount
	
# 	print columnOneCount
# 	print columnZeroCount
# 	entropyColumnOne, entropyColumnZero = 0, 0
	
# 	# entropy one
# 	if(columnOneCount == 0):
# 		entropyColumnOne = 0
# 	else:	
# 		if(columnOneOneCount == 0):
# 			term1 = 0
# 		else:
# 			term1 = (columnOneOneCount / float(columnOneCount)) * math.log(columnOneOneCount / float(columnOneCount), 2)
# 		if(columnOneZeroCount == 0):
# 			term2 = 0
# 		else:
# 			term2 = (columnOneZeroCount / float(columnOneCount)) * math.log(columnOneZeroCount / float(columnOneCount), 2)
# 		entropyColumnOne = -term1-term2
	
# 	# entropy zero
# 	if(columnZeroCount == 0):
# 		entropyColumnZero = 0
# 	else:
# 		if(columnZeroOneCount == 0):
# 			term1 = 0
# 		else:
# 			term1 = ((columnZeroOneCount / float(columnZeroCount)) * math.log(columnZeroOneCount / float(columnZeroCount), 2))
# 		if(columnZeroZeroCount == 0):
# 			term2 = 0
# 		else:
# 			term2 = ((columnZeroZeroCount / float(columnZeroCount)) * math.log(columnZeroZeroCount / float(columnZeroCount), 2))
# 		entropyColumnZero = -term1-term2

# 	gainZero = entropyZero - ((classZeroOneCount / float(maxGainZeroCount)) * entropyColumnZero) - ((classZeroZeroCount / float(maxGainZeroCount)) * entropyColumnOne)
# 	#gainOne = entropyOne - ((classOneOneCount / float(maxGainOneCount)) * entropyColumnOne) - ((classOneZeroCount / float(maxGainOneCount)) * entropyColumnOne)
# 	print gainZero
# 	#print gainOne
# 	break