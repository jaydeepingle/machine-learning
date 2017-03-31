import csv
class ReadData(object):
	# read data from csv
	@classmethod
	def readDataMatrix(self, path):
		datafile = open(path, 'r')
		datareader = csv.reader(datafile, delimiter=';')
		data = []
		count = 0

		# read csv file into columns
		for row in datareader:
		    if(count != 0):
		    	dataRow = map(int, row[0].split(','))
		    	data.append(dataRow)
		    else:
		    	dataRow = map(str, row[0].split(','))
		    	data.append(dataRow)
		    count = count + 1
		return data