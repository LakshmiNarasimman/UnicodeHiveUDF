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
        for i in range(len(numberOfResults)):
            product[numberOfResults[i]]=contentFromEndPoint['hits']['hits'][0]['_source']['r'][numberOfResults[i]]
            comp_list=[]
            comp_list.append(product[numberOfResults[i]]['price1'])    
            comp_list.append(product[numberOfResults[i]]['price2'])
            product[numberOfResults[i]]['price1']=max(comp_list)
            product[numberOfResults[i]]['price2']=min(comp_list)
        
        #print  json.dumps(product,indent=4,sort_keys=False)
        #print  json.dumps(product,indent=4,sort_keys=False)
        key_min = min(product.keys(), key=(lambda k: product[k]['price2']))
        porduct_minprice={}
        porduct_minprice[key_min]=product[key_min]
        print  json.dumps(porduct_minprice,indent=4,sort_keys=False)
    
obj=url_minPrice()
obj.get_minPrice(667880922282)
