import sys
import datetime
import urllib2
import urllib
import csv
from bs4 import BeautifulSoup

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# Feel free to remove these 4 lines of code

# url = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=Tempe%2C+AZ'
# content = urllib2.urlopen(url).read()
# content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
# soup = BeautifulSoup(content)

# f = open('tempeyelppage.html', 'r')
# content = f.read()
# soup = BeautifulSoup(content)

parameters={}
parameters['find_desc']='restaurants'
parameters['find_loc']='Phoenix, AZ'
parameters['l']='p:AZ:[Anthem::,Apache_Junction::,Arizona_City::,Avondale::,Buckeye::,Carefree::,Casa_Grande::,Cave_Creek::,Central_City::,Central_City_Village::,Coolidge::,El_Mirage::,Eloy::,Florence::,Fort_McDowell::,Fountain_Hills::]'

def tenpages_both(pagestart): 

	parameters['start']=pagestart

	data=urllib.urlencode(parameters)
	url = 'http://www.yelp.com/search'

	url = url + '?' + data

	content = urllib2.urlopen(url).read()
	content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
	soup = BeautifulSoup(content)
	
	businessnames = soup.find_all("a", {"class": "biz-name"})
	businesscategories = soup.find_all("span", {"class": "category-str-list"})
	businessaddresses = soup.find_all("address")

	rated=[]
	rated2=[]
	rated3=[]

	for i in businessnames:
		rated.append(i.text)
		
	for i in businesscategories:
		rated2.append(i.text)

	for i in businessaddresses:
		rated3.append(i.text)
	
	zipped = zip(rated, rated2, rated3)
	
	return zipped

globallist2 = []

for i in range(0, 1000, 10):
	globallist2.extend(tenpages_both(i))	


def write_csv(file_name, data=[], columns=()):
    with open(file_name, 'wb') as f:
        writer = csv.writer(f)
        data_to_write = []
        for i in data:
            tup = []
            for j in i:
                tup.append(unicode(j).encode('utf-8'))
            data_to_write.append(tuple(tup))
        writer.writerows(data_to_write)
	
write_csv("anthem, apache junction, az city, avondale, buckeye, carefree, casa grande, cave creek, central city village, coolidge, el mirage, eloy, florence, fort mcdowell, fountain hills.csv", data = globallist2)
# def tenpages(pagestart): 
	# parameters['start']=pagestart

	# data=urllib.urlencode(parameters)
	# url = 'http://www.yelp.com/search'

	# url = url + '?' + data

	# content = urllib2.urlopen(url).read()
	# content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
	# soup = BeautifulSoup(content)
	
	# businessnames = soup.find_all("a", {"class": "biz-name"})
	# businessaddresses = soup.find_all("address")
	
	# rated=[]
	
	# for item in businessnames:
		
		# rated.append(item.text)
		
	# for item in businessaddresses:
		
		# rated.append(item.text)
	
	# adfind = soup.find_all("span", {"class": "yloca-tip" })

	# for i in adfind:
		# dlinks = i.find_next_siblings("a")

	# adtext=[]

	# for i in adlinks:
		# adtext.append(i.text)

	# adtext = set(adtext)
	# rated = [r for r in rated if r not in adtext]
	
	# return rated
	
# globallist = []

# for i in range(0, 100, 10):
	# globallist.extend(tenpages(i))

# f = open('tempe.csv', 'w')
# for item in globallist:
	# f.write("%s\n" % item.encode('utf-8'))


	






