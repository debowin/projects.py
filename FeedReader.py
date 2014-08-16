__author__ = 'debowin'
import urllib2
import re

def main():
    """
    Parses the RSS feed for most news feed providers and lists various news items by title, short description and a link
    for further reading.
    """
    webpage = urllib2.urlopen('http://feeds.feedburner.com/NdtvNews-TopStories?format=xml').read()
    # print webpage
    patFinderTitle = re.compile('<title>(.*?)</title>')
    patFinderLink = re.compile('<link>(.*?)</link>')
    patFinderDesc = re.compile('<description>(.*?)&lt;')

    findPatTitle = re.findall(patFinderTitle,webpage)
    findPatLink = re.findall(patFinderLink,webpage)
    findPatDesc = re.findall(patFinderDesc,webpage)

    print "Feed Contents:", len(findPatTitle), "items..."
    for i in range(2,len(findPatLink)):
        print str(i-1)+")\tHeadline:",findPatTitle[i]
        print "\tLink:",findPatLink[i]
        print "\tDesc:",findPatDesc[i-1]
        articlePage = urllib2.urlopen(findPatLink[i]).read()
        divBegin = articlePage.find('<div class="pdl200">')

if __name__=="__main__":
    main()
