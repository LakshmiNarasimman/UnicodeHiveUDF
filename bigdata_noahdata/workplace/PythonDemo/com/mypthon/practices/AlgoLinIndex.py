'''
Created on 04-Oct-2017

@author: bigdata
'''
import requests, json
from algoliasearch import algoliasearch
import sys
sys.setrecursionlimit(2500)
counter = 0
def add_new_records(json_data):
    """
    Method used to Add records in Algolia
    """
    client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
    index = client.init_index('products')
    res = index.add_objects(json_data)

def dump_es_data_to_algolia(url):
    """
    Method used to read data from ES server
    and insert in to Algolia indices.
    """
    global counter
    endPointResponse = requests.get(url) 
    contentFromEndPoint = json.loads(endPointResponse.content) 
    numberOfResults = len(contentFromEndPoint['hits']['hits'])
    jsonlist=[]
    counter +=1
    print (counter)
    for i in range(numberOfResults):
        try:
            requestDictionary = contentFromEndPoint['hits']['hits'][i]['_source']['r']
            addUPC = contentFromEndPoint['hits']['hits'][i]['_source']['upc']
            objectID = contentFromEndPoint['hits']['hits'][i]['_source']['price_id']
            key = requestDictionary.keys()[0].decode('utf8') 
            requestDictionary[key].pop('affiliate_url') 
            requestDictionary[key]['upc'] = addUPC
            requestDictionary[key]['objectID'] = int(objectID)
            requestDictionary[key]['favorite_count'] = ''
            requestDictionary[key]['description'] = ''
            requestDictionary[key]['brand'] = ''
            requestDictionary[key]['size'] = ''
            requestDictionary[key]['color'] = ''
            jsonlist.append(requestDictionary.values()[0])
        except:
            pass
    # Lets add records
    add_new_records(jsonlist)
    #print jsonlist
    del jsonlist
    #print ("Deleted ")
    scrollId = json.loads(endPointResponse.content)['_scroll_id']
    newUrl = 'http://search-price-staging-acdnexszocgkssstdqsmrfq4qq.us-east-1.es.amazonaws.com/_search/scroll/%s?scroll=1m'%(scrollId)
    dump_es_data_to_algolia(newUrl)
    
dump_es_data_to_algolia('http://search-price-staging-acdnexszocgkssstdqsmrfq4qq.us-east-1.es.amazonaws.com/product_index/_search?scroll=30m&pretty&size=10000')