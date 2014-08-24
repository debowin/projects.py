"""
This script lets users perform various operations using the bit.ly API such as:
1. shorten: Takes a long link as an input and provides a short link.
2. hits: Allows a query on how many times the short link has been clicked.
3. referrers: Allows a query on who the referrers are to the short link and the number of hits by each.
4. search: Allows a query on all the short links in bit.ly
		*** Make sure you paste in your own client credentials in the script before running it ***
"""

import requests
import json
import sys


def main():
    if len(sys.argv)<3:
        print "Usage: python bit.py URL/query operation"
    query_params = {'apiKey': 'YOUR API KEY', 'login':'YOUR LOGIN'}

    if sys.argv[2]=="shorten":
        endpoint = 'https://api-ssl.bitly.com/v3/shorten'
        query_params['longUrl'] =  sys.argv[1]
        response = requests.get(endpoint, params=query_params, verify=False)
        data = json.loads(response.content)
        print "Short Link:", data['data']['url']
    elif sys.argv[2]=="hits":
        endpoint = 'https://api-ssl.bitly.com/v3/link/clicks'
        query_params['link'] =  sys.argv[1]
        query_params['access_token']= 'YOUR ACCESS TOKEN'
        response = requests.get(endpoint, params=query_params, verify=False)
        data = json.loads(response.content)
        print "Hits:",data['data']['link_clicks']
    elif sys.argv[2]=="referrers":
        endpoint = 'https://api-ssl.bitly.com/v3/link/referrers'
        query_params['access_token']= 'YOUR ACCESS TOKEN'
        query_params['link'] =  sys.argv[1]
        response = requests.get(endpoint, params=query_params, verify=False)
        data = json.loads(response.content)
        referrers = [(referrer['referrer'],referrer['clicks']) for referrer in data['data']['referrers']]
        for referrer in referrers:
            print "Referrer: %s Hits: %s" % (referrer[0],referrer[1])
    elif sys.argv[2]=="search":
        endpoint = "https://api-ssl.bitly.com/v3/search"
        query_params = {
            'access_token': "YOUR ACCESS TOKEN",
            'query': sys.argv[1],
            'fields': "aggregate_link,title,url",
            'limit': 10 }
        response = requests.get(endpoint, params=query_params, verify=False)
        data = json.loads(response.content)
        for result in data['data']['results']:
            print "#\tTitle:",result['title']
            print "\tURL:",result['url']
            print "\tShort Link:",result['aggregate_link']


if __name__=="__main__":
    main()
