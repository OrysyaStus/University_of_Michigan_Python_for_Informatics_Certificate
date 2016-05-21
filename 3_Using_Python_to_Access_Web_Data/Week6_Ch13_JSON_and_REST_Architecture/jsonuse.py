# Extracting Data from JSON
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data
# you need to process for the assignment.
# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json (Sum=2553)
# Actual data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174252.json (Sum ends with 32)

import json
import urllib

count = 0
sum = 0

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174252.json'

while True:
	address = raw_input('Enter URL: ')
	if len(address) < 1 : break

	url = serviceurl + urllib.urlencode({"sensor": "false", "address": address})
	print 'Retrieving', url
	connection = urllib.urlopen(url)
	data = connection.read()
	length = len(data)
	print 'Retrieved:', length, 'characters'
	
	data1 = data.count("count")		#counts the number of occurences of "count" in the string data
	
	js = json.loads(data)
	
	#print json.dumps(js, indent=4)
		
	for i in range(0, data1):
		sum1 = js["comments"][i]["count"]		#must provide an integer number for the range of i to be iterated through
		count = count + 1
		sum = sum + sum1
	print 'Count:', count
	print 'Sum:', sum