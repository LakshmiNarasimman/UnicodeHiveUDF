'''
Created on 17-Oct-2017

@author: bigdata
'''
import requests
import json
from collections import OrderedDict

class url_minPrice:
    def __init__(self):
        '''
        Constructor
        '''
    def get_minPrice(self,upcCode):
        endPointResponse = requests.get('https://search-alex-test-wjdpovi7koep7jeg2z73oordey.us-east-1.es.amazonaws.com/product_index/_search?q=upc:%s&pretty' % upcCode) 
        contentFromEndPoint = json.loads(endPointResponse.content, object_pairs_hook=OrderedDict)
        numberOfResults = contentFromEndPoint['hits']['hits'][0]['_source']['r'].keys()
        product={}
        product_final={}
        minPriceLs=[]
        for i in range(len(numberOfResults)):
            minPriceLs.append(contentFromEndPoint['hits']['hits'][0]['_source']['r'][numberOfResults[i]])
        minPricedItem = min(minPriceLs, key=lambda x:x['price1'])
        
        for i in range(len(numberOfResults)):
            product[numberOfResults[i]]=contentFromEndPoint['hits']['hits'][0]['_source']['r'][numberOfResults[i]]
        key_min = min(product.keys(), key=(lambda k: product[k]['price1']))
        product_final[key_min]= minPricedItem
        print  json.dumps(product_final,indent=4,sort_keys=False)
    
obj=url_minPrice()
obj.get_minPrice(667880922282)