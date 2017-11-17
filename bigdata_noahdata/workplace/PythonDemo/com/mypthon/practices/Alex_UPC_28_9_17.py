'''
Created on 04-Oct-2017

@author: bigdata
'''
import requests
import json
from collections import OrderedDict

class upcUsedNew:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
   
    def upcUsed(self, upcCode):
        endPointResponse = requests.get('http://search-price-used-production-wrobho4tskcnz4mxygweriempe.us-east-1.es.amazonaws.com/_search?q=upc:%s&size=10000&pretty' % upcCode) 
        contentFromEndPoint = json.loads(endPointResponse.content, object_pairs_hook=OrderedDict) 
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
            print productList
    
    def upcNew(self, upcCode):
            endPointResponse = requests.get('http://search-price-staging-acdnexszocgkssstdqsmrfq4qq.us-east-1.es.amazonaws.com/product_index/_search?q=upc:%s&size=100&pretty' % upcCode) 
            contentFromEndPoint = json.loads(endPointResponse.content, object_pairs_hook=OrderedDict)
            init = contentFromEndPoint['hits']['hits']
            numberOfResults = len(init)
            productList = []
            for i in range(numberOfResults):
                product = {}
                product['product_attributes'] = {}
                b = init[i]['_source']['r']
                key = b.keys()
                for j in range(len(key)):
                    product['product_images'] = b[key[j]]['image_url']
                    product['product_attributes']['product_url'] = b[key[j]]['product_url']
                    product['product_attributes']['title'] = init[i]['_source']['title']
                    product['product_attributes']['upc'] = init[i]['_source']['upc']
                    product['product_attributes']['price1'] = b[key[j]]['price1']
                    product['product_attributes']['price2'] = b[key[j]]['price2']
                    if(b[key[j]].get('description')):
                        product['product_attributes']['description'] = b[key[j]]['description']
                    else:
                        product['product_attributes']['description'] = ''
                    productList.append(product)
                    print productList
                

obj = upcUsedNew()
#obj.upcUsed(759606024612)
obj.upcNew(276300)