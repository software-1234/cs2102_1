import csv
with open('resale-flat-prices.csv','rb') as csvfile:
	results = []
	reader = csv.reader(csvfile)
	for row in reader:
		if row[2] == '3 ROOM' and row[7] == 'TERRACE': 
			results.append(row)
	myFile = open('result.csv', 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(results)
	print("Writing Complete")
	#print results
