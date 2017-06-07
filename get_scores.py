import urllib2
from bs4 import BeautifulSoup

url = raw_input("url: ")

page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

scores = soup.find('div', id='scoreboardMatchups').findAll('table')

#scores = soup.findAll('table')

print scores
