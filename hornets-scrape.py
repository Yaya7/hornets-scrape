import urllib2
import re
import sys
from bs4 import BeautifulSoup
import csv
import os
import itertools
from itertools import izip
import datetime
from datetime import datetime
from datetime import date


my_url = "http://www.nba.com/hornets/schedule/"
scheduleHTML = urllib2.urlopen(my_url)

# Now we create a beautifulsoup object by passing through html to the BeautifulSoup()
soup = BeautifulSoup(scheduleHTML, "html.parser")


daysofweek = []
weekdays = soup.findAll('span', attrs={'class': 'desktop'})
for day in weekdays:
	weekday = str(day.string)
	daysofweek.append(weekday)
print len(daysofweek) #89

newdaysofweek = []

for dd in daysofweek:
	if(dd == "Sunday"):
		dd = "Monday"
		newdaysofweek.append(dd)
	elif(dd == "Monday"):
		dd = "Tuesday"
		newdaysofweek.append(dd)
	elif(dd == "Tuesday"):
		dd = "Wednesday"
		newdaysofweek.append(dd)
	elif(dd == "Wednesday"):
		dd = "Thursday"
		newdaysofweek.append(dd)
	elif(dd == "Thursday"):
		dd = "Friday"
		newdaysofweek.append(dd)
	elif(dd == "Friday"):
		dd = "Saturday"
		newdaysofweek.append(dd)
	elif(dd == "Saturday"):
		dd = "Sunday"
		newdaysofweek.append(dd)


gamedates = []
dates = soup.findAll('span', attrs={'class': 'date etowah-schedule__event_datetime__date etowah-schedule__event--game__datetime__date'})
for date in dates:
	gameday = str(date.span.next_sibling)
	gameday = gameday.strip()
	gamedates.append(gameday)
print len(gamedates) #89


rows = zip(newdaysofweek, gamedates)

# Create column headers
headers = ['Weekday', 'Date']

with open("hornets_schedule_2016.csv", 'w') as w:
	writer = csv.writer(w)
	writer.writerow(headers)
	for row in rows:
		writer.writerow(row)


# Open the file
os.system("open hornets_schedule_2016.csv")
