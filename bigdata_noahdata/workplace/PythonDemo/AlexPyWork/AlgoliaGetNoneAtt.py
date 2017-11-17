'''
Created on 10-Nov-2017

@author: bigdata
'''
import json
from algoliasearch import algoliasearch
import sys

class algoliaRecordsRetrieval:
    
    def getCBNotNull(self):
        client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
        index = client.init_index('products_v3')
        query = ""
        res = index.browse_from({"query": query}, None)
        i=0
        while "cursor" in res:
            json_string = json.dumps(res,sort_keys=False)
            tem_dicts=json.loads(json_string)
            dicts= json.loads(json.dumps(tem_dicts['hits']))
            for x in dicts:
                print x

#             cb_not_nul=[]
#             for cb in dicts:
#                 if("category_breadcrumb" in cb) :
#                     if((cb["category_breadcrumb"]!=None) and (cb["category_breadcrumb"]!='')):
#                         if(not cb.get('price_category')):
#                             cb['price_category']=cb.get('category_breadcrumb')
#                             
#                             cb_not_nul.append(cb)
#                         else:
#                             cb['price_category']=cb.get('category_breadcrumb')
#                             cb_not_nul.append(cb)
#                     
#             for x in cb_not_nul:
#                 print x["price_category"]            
#             print len(cb_not_nul)           
#             res = index.browse_from(None, res["cursor"])
            i+=1
            if(i==1):
                sys.exit()   
obj = algoliaRecordsRetrieval()
obj.getCBNotNull()                               