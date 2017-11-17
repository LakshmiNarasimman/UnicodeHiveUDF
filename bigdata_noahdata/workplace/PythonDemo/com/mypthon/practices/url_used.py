'''
Created on 15-Sep-2017

@author: bigdata
'''
import requests
import json
from collections import OrderedDict
from requests.exceptions import ConnectionError

class urlUsedNew:
    '''
    classdocs
    '''
    
    def urlUsed(self, url):
        try:
            esurl = 'http://search-price-used-production-wrobho4tskcnz4mxygweriempe.us-east-1.es.amazonaws.com/_search?&pretty'
            payload = {"query":{"multi_match":{"query":"%s"%url,"fields":["r.*.product_url.keyword"]}}}
            endPointResponse = requests.post(esurl, data=json.dumps(payload))
            contentFromEndPoint = json.loads(endPointResponse.content, object_pairs_hook=OrderedDict) 
            numberOfResults = contentFromEndPoint['hits']['hits'][0]['_source']['upc']
            print numberOfResults
            upcEndPointResponse = requests.get('http://search-price-used-production-wrobho4tskcnz4mxygweriempe.us-east-1.es.amazonaws.com/_search?q=upc:%s&pretty' % numberOfResults) 
            contentFromEndPoint = json.loads(upcEndPointResponse.content, object_pairs_hook=OrderedDict) 
            numberOfResults = contentFromEndPoint['hits']['hits'][0]['_source']['r'].keys()
   
            productList = []
            for i in range(len(numberOfResults)):
                b = contentFromEndPoint['hits']['hits'][0]['_source']['r'][numberOfResults[i]]
                for j in range(len(b)):
                    product = {}
                    product['product_attributes'] = {}
                    product['product_images'] = b[j]['image_url']
                    product['product_attributes']['product_url'] = b[j]['product_url']
                    product['product_attributes']['title'] = b[j]['title']
                    product['product_attributes']['price1'] = b[j]['price1']
                    product['product_attributes']['price2'] = b[j]['price2']
                    productList.append(product)
            print json.dumps(productList,indent=4)
        except (ConnectionError,IndexError):
            print '*****Failed to open url*******!'    
    
    def urlNew(self, url):
        try:
            esurl = 'http://search-price-staging-acdnexszocgkssstdqsmrfq4qq.us-east-1.es.amazonaws.com/product_index/_search?&pretty'
            payload = {"query":{"multi_match":{"query":"%s"%url,"fields":["r.*.product_url.keyword"]}}}
            endPointResponse = requests.post(esurl, data=json.dumps(payload))
            contentFromEndPoint = json.loads(endPointResponse.content, object_pairs_hook=OrderedDict)
            init = contentFromEndPoint['hits']['hits'][0]['_source']['upc']
            print init
            upcEndPointResponse = requests.get('http://search-price-staging-acdnexszocgkssstdqsmrfq4qq.us-east-1.es.amazonaws.com/product_index/_search?q=upc:%s&pretty' % init) 
            contentFromUPCEndPoint = json.loads(upcEndPointResponse.content, object_pairs_hook=OrderedDict)
            initd = contentFromUPCEndPoint['hits']['hits']
            numberOfResults = len(initd)
            productList = []
            for i in range(numberOfResults):
                b = initd[i]['_source']['r']
                key = b.keys()
                for j in range(len(key)):
                    product = {}
                    product['product_attributes'] = {}
                    product['product_images'] = b[key[j]]['image_url']
                    product['product_attributes']['product_url'] = b[key[j]]['product_url']
                    product['product_attributes']['title'] = initd[i]['_source']['title']
                    product['product_attributes']['upc'] = initd[i]['_source']['upc']
                    product['product_attributes']['price1'] = b[key[j]]['price1']
                    product['product_attributes']['price2'] = b[key[j]]['price2']
                    productList.append(product)
            print json.dumps(productList,indent=4)
        except (ConnectionError,IndexError):
            print '*****Failed to open url*******!'         
    def __init__(self):
        '''
        Constructor
        ''' 

# RUN
obj = urlUsedNew()
obj.urlUsed('http://rover.ebay.com/rover/1/711-53200-19255-0/1?toolid=10029&campid=CAMPAIGNID&customid=CUSTOMID&catId=1&type=2&ext=401401193159&item=401401193159')
obj.urlNew('http://www.walmart.com/ip/Uno-No-Es-Uno/12534049')