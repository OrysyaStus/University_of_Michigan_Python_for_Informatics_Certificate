# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
# and then converting the extracted strings to integers and summing up the integers.

file = raw_input('Please print file name: ')
handle = open(file)
count = 0
numbers = 0
import re
for line in handle:
	line = line.rstrip()
	num = re.findall('[0-9]+', line)
	for i in num:
		value = int(i)
		numbers = numbers + value
		count = count + 1
print 'There are', count, 'values with a sum =', numbers