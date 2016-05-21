# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

file = raw_input('Please enter file name: ')
handle = open(file)
data1 = list()
data2 = dict()
for line in handle:
	line = line.rstrip()
	if not line.startswith('From '):
		continue
	line = line.split()
	line = line[1]
	data1.append(line)
for i in data1:
	data2[i] = data2.get(i,0)+1

word = None
max = None

for aa, bb in data2.items():
	if max is None or bb > max:
		word = aa
		max = bb

print word, max

# Expected result: cwen@iupui.edu 5