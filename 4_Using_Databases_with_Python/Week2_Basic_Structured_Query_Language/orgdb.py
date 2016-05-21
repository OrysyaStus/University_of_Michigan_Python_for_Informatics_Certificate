# Counting Organizations
# This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain name of the email address)
# using a database with the following schema to maintain the counts.
# CREATE TABLE Counts (org TEXT, count INTEGER)

import sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()
	org1 = pieces[1]
	pieces2 = org1.split('@')
	org = pieces2[1]
	#org = re.findall('@(.+)', org1)		#alternative to parsing, but was giving back list instead of string and str conversion caused ['_'] to remain
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', ( org, ) )
	else : 
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
	conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()