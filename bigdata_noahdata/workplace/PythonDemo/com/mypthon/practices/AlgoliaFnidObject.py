'''
Created on 30-Oct-2017

@author: bigdata
'''
from algoliasearch import algoliasearch
import sys
import json


client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
index = client.init_index('products_v3')
query = ""
res = index.browse_from({"query": query}, None)
objectId_list=[]
i=0
while "cursor" in res:
    json_string = json.dumps(res,sort_keys=False,indent=4)
    tem_dicts=dicts= json.loads(json_string) 
    dicts= json.loads(json.dumps(tem_dicts['hits']))
    for objId in dicts:
        objectId_list.append(objId['objectID'])
    print len(objectId_list)    
    for l in objectId_list:
        print "Object_Id:",l     
        
#     print json.dumps(dicts,sort_keys=False,indent=4)
    i+=1    
    if(i==1):
        sys.exit()
        