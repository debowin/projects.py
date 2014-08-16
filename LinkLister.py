__author__ = 'debowin'
from bs4 import BeautifulSoup
import urllib2

def main():
    """
    Takes a web link as input and displays its title and lists all the http(s) links contained within.
    """
    url = "http://www.google.com"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    #print soup.prettify()
    print "Title:\t"+soup.title.string
    print "Links:"
    for link in soup.find_all('a'):
        if link.get('href') and link.get('href')[0]=='h':
            print "\t\t"+link.get('href')


if __name__=="__main__":
    main()