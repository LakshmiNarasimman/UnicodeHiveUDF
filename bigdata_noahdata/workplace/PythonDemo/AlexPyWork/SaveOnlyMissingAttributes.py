'''
Created on 07-Nov-2017

@author: bigdata
'''
import sys
import json
import pandas as pd   
from algoliasearch import algoliasearch
def saveAsFile():
    client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
    index = client.init_index('products_v3')
    query = ""
    res = index.browse_from({"query": query}, None)
    i=0
    while "cursor" in res:
        json_string = json.dumps(res,sort_keys=False)
        tem_dicts=json.loads(json_string) 
        dicts= json.loads(json.dumps(tem_dicts['hits']))
        limit_att=["price_category","price_cat_id"]
        valid_data=[]
        for x in range(len(dicts)):
            if (("price_category" not in dicts[x]) and ("price_cat_id" not in dicts[x])):
                valid_data.append(dicts[x])
                print dicts[x]
                
        df=pd.DataFrame(valid_data,columns=dicts[0].keys()) 
        print "Iteration number: %i"%i
        print df.columns
        filename="G:\\Alex_py\\products_v3.csv"
        cols=["title","description","product_url","image_url","list_price","offer_price","category_breadcrumb","brand","color","size","click_count","fav_count","objectID"]
        if(i==0):
            df.to_csv(filename,index=False,encoding='utf-8',columns=cols)
        else:
            df.to_csv("G:\\Alex_py\\products_v3.csv",index=False,encoding='utf-8',mode='a',columns=cols,header=False)
        res = index.browse_from(None, res["cursor"])
        i+=1    
        if(i==20):
            sys.exit()