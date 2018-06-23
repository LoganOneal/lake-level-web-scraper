import requests
import json
import csv

r = requests.get(url='http://www.cherokeelake.info/LevelDataJSON.asp?SiteID=TN005')
data = r.json()


year_2013 = []
year_2014 = []
year_2015 = []
year_2016 = []
year_2017 = []
year_2018 = []

def getData(year):
	i = 0
	for item in data["charts"]:
		try:
			eval('year_' + year).append(data["charts"][i][year])
		except KeyError:
			eval('year_' +year).append('null')		
		i += 1
def write():
	with open('data/out.csv', "w") as output:
		writer = csv.writer(output)
		header = ('Day', '2013', '2014', '2015', '2016', '2017', '2018')
		writer.writerow(header)
		for i in range(365):
			data = (i, year_2013[i], year_2014[i], year_2015[i], year_2016[i], year_2017[i], year_2018[i])
			print(data)
			writer.writerow(data)

for i in range(2013, 2018+1):
	getData(str(i))
write()
