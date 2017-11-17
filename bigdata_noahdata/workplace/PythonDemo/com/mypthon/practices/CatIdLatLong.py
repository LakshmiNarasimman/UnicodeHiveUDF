'''
Created on 24-Aug-2017

@author: bigdata
'''
import requests
import json
from collections import OrderedDict

# print(r.status_code)
# print(r.text)
# payload = {"query":{"bool":{"must":{"match":{"CAT_ID":"25459"}},"filter":{"geo_distance":{"distance":"50km","r.offerup.pin":{"lat":37.3892,"lon":-122.0639}}}}},"sort":[{"r.offerup.price2":{"order":"desc"}}]}
# print payload
# cat_id=10000
# distance="20km"
# lat="45.3892"
# longi="-144.0639"
# class CatIdClass:
#     def calCulation(self,catid,dis,lati,longi):
#         url = 'http://search-price-no-upc-gqwereizkfhyzfarmk57wnjoge.us-east-1.es.amazonaws.com/product_index/product/_search?pretty'
#         payload = {"query":{"bool":{"must":{"match":{"CAT_ID":"%d" % catid}},"filter":{"geo_distance":{"distance":"%s"%dis,"r.offerup.pin":{"lat":"%s"%lati,"lon":"%s"%longi}}}}},"sort":[{"r.offerup.price2":{"order":"desc"}}]}
#         print payload
#         r = requests.post(url, data=json.dumps(payload))
#         
# obj = CatIdClass()
# obj.calCulation(cat_id, distance, lat, longi)

class CatIdClass:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getOffers(self, catid, dis, lati, longi):
        url = 'http://search-price-no-upc-gqwereizkfhyzfarmk57wnjoge.us-east-1.es.amazonaws.com/product_index/product/_search?pretty'
        payload = {"query":{"bool":{"must":{"match":{"CAT_ID":"%d" % catid}}, "filter":{"geo_distance":{"distance":"%s" % dis, "r.offerup.pin":{"lat":"%s" % lati, "lon":"%s" % longi}}}}}, "sort":[{"r.offerup.price2":{"order":"desc"}}]}
        endPointResponse = requests.post(url, data=json.dumps(payload))
        contentFromEndPoint = json.loads(endPointResponse.content, object_pairs_hook=OrderedDict)
        numberOfResults = contentFromEndPoint['hits']['hits']
        for i in range(len(numberOfResults)):
            offers = contentFromEndPoint['hits']['hits'][i]['_source']['r']['offerup']
            print json.dumps(offers)
        
obj = CatIdClass()
obj.getOffers(25459, "200km", "37.3892", "-122.0639")   
