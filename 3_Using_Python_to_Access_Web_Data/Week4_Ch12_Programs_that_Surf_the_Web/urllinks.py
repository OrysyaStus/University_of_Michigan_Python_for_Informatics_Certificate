# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the
# process a number of times and report the last name you find.

# ie. urls to use: http://python-data.dr-chuck.net/known_by_Leiten.html 

import urllib
from BeautifulSoup import *
import re

text = list()
ref = list()

url = raw_input('Enter - ')
first = re.findall('_([a-zA-Z]+).html', url)
text = text + first

count = raw_input('Count - ')
count = int(count)
position = raw_input('Position - ')
position = int(position)

for i in range (0, count):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	tags = soup('a')
	for tag in tags:
		bam = tag.get('href', None)
		bam = str(bam)
		ref.append(bam)
	
	url = ref[position - 1]
	
	ref = list()
	
	first = re.findall('_([a-zA-Z]+).html', url)
	text = text + first
print 'Sequence: ', text