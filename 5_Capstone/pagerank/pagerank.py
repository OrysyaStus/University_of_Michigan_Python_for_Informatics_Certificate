#Page Rank

#First you will spider 100 pages from http://python-data.dr-chuck.net/ run the page rank algorithm and take some screen shots. Then you will reset the spider process and spider 100 pages from any other site on the Internet, run the page rank algorithm, and take some screen shots.

#Don't take off points for little mistakes. If they seem to have done the assignment give them full credit. Feel free to make suggestions if there are small mistakes. Please keep your comments positive and useful. 
#Sample solution: http://www.dr-chuck.net/pythonlearn/code/pagerank.zip

# Steps:
# Run spider.py which spiders the links from intitial page & creates an database in SQLite Browser; builds a lot of links really fast. Creates a many-many relationships. Is time consuming unfortunately, and depends on the network bandwidth.
# Once enough links/data points are collected, use the sprank.py algorithm. Where the page rank stabilizes through reading data from spider.sql and replacing old_rank with new_rank through copy iterations. The ranks stabilizes over many repetitions. With increasing iterations, the amount of change between interations decreases -> new_rank = old_rank therefore stabilization. 
# Run spdump.py which retrieves the first 50 rows by linking the data up for the retrieved pages.
# Run spjson.py which takes the data from the spider.sql and input it into the spider.js file. 