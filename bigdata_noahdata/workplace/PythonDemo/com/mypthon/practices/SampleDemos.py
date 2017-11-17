'''
Created on 18-Aug-2017

@author: bigdata
'''
import requests
import json
from collections import OrderedDict

class catID:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
   
    def queryWithCatId(self, cat_id):
        endPointResponse = requests.get('http://search-price-no-upc-gqwereizkfhyzfarmk57wnjoge.us-east-1.es.amazonaws.com/product_index/product/_search?q=r.cndirect.CAT_ID:%s r.gearbest.CAT_ID:%s r.miniinthebox.CAT_ID:%s r.zapals.CAT_ID:%s r.banggood.CAT_ID:%s r.bulbhead.CAT_ID:%s r.realreal.CAT_ID:%s&size=10&pretty&default_operator=OR' %(cat_id,cat_id,cat_id,cat_id,cat_id,cat_id,cat_id))
        contentFromEndPoint = json.loads(endPointResponse.content) 
        numberOfResults = contentFromEndPoint['hits']['hits']
        productList = []
        sizeJson=len(numberOfResults)
        print "Length of the json",sizeJson
        for i in range(sizeJson):
            offers = contentFromEndPoint['hits']['hits'][i]['_source']['r']
            print offers
                            

obj = catID()
obj.queryWithCatId(13157)