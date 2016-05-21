# Extracting Data from XML
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data
# you need to process for the assignment.
# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml (Sum=2553)
# Actual data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174248.xml (Sum ends with 82)

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174248.xml'
count = 0
sum = 0

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : break

	url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'
	#print data
	tree = ET.fromstring(data)
	bam = tree.findall('comments/comment')
	for item in bam:
		counts = item.find('count').text
		sum = sum + int(counts)
		count = count + 1
	print 'Count: ', count
	print 'Sum: ', sum

# data = '''<commentinfo>
#		<comments>
#			<comment>
#				<name>Romina</name>
#				<count>97</count>
#			</comment>
#		</comments>
#	</commentinfo>'''