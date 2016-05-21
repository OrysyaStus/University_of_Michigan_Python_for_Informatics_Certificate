#Gmane

#Mailing List Data - Part I
#In this assignment you will download some of the mailing list data from http://mbox.dr-chuck.net/ and run the data cleaning / modeling process and take 
#some screen shots.

#Don't take off points for little mistakes. If they seem to have done the assignment give them full credit. Feel free to make suggestions if there are small 
#mistakes. Please keep your comments positive and useful. 
#Sample solution: http://www.dr-chuck.net/pythonlearn/code/gmane.zip

#Steps:

#Run gmane.py from http://mbox.dr-chuck.net/, data is large so give time for the sql to be created.
#Run gmodel.py which compresses/cleanups the content.sqlite file.
#Run gbasic.py dump top 15 people and organizations for finding anomolies.
#For visualization:
#Run gword.py to determine the top words (without any punctuation, numbers, or words less than 4); range of lowest and highest words outputted. Then writes to gword.js and open gword.htm in browser to see visualization. Code was taken from D3 website.
#Run gyear.py by counting senders, determining 10 organizations who are senders, get keys for highest senders, then create a histogram for top organization for each year (year, domain name is a tuple and is used as a key in the dictionary). Creates gline.js and open gline.htm.
#Or run gline.py (which is almost identical as gyear.py but asks for the month vs the year). Creates a new gline.js and new gline.htm.