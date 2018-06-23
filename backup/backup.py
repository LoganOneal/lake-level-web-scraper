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

def write(year):
	with open('data/'+year+'.csv', "w") as output:
		writer = csv.writer(output)
		for val in eval('year_'+year):
			writer.writerow([val])

for i in range(2013, 2018+1):
	getData(str(i))
	write(str(i))
