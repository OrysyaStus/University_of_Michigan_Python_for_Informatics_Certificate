# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file = raw_input('Please input file name:')
handle = open(file)
data1 = list()
data2 = dict()
for line in handle:
	line = line.rstrip()
	if not line.startswith('From '):
		continue
	line = line.split()
	line = line[5]
	line = line.split(':')
	line = line[0]
	data1.append(line)
for i in data1:
	data2[i] = data2.get(i,0) + 1

hour = None
count = None
data3 = list()

for aa, bb in data2.items():
	data3.append( (aa,bb) )

data3.sort()

for key, val in data3:
	print key, val

# Expected result:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1