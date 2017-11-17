'''
Created on 24-Oct-2017

@author: bigdata
'''
from algoliasearch import algoliasearch
import sys
import json
import pandas as pd


client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
index = client.init_index('products_v3')
query = ""
res = index.browse_from({"query": query}, None)
col_list=[]
i=0
j=0
while "cursor" in res:
    json_string = json.dumps(res,sort_keys=False)
    tem_dicts=json.loads(json_string) 
    dicts= json.loads(json.dumps(tem_dicts['hits']))
    df=pd.DataFrame(dicts,columns=dicts[0].keys()) 
    print "Downloading the file.."
    cols=[u'title',u'description',u'product_url',u'image_url',u'list_price',u'offer_price',u'category_breadcrumb',u'brand',u'color',u'size',u'click_count',u'fav_count']
    if(i==0):
        df.to_csv("/home/bigdata/bigdata_noahdata/Alex_Py/testpy.csv",index=False,encoding='utf-8',columns=cols)
        
    else:
        df.to_csv("/home/bigdata/bigdata_noahdata/Alex_Py/testpy.csv",index=False,encoding='utf-8',mode='a',columns=cols,header=False)
            
    #print json.dumps(res,indent=4,sort_keys=False) 
    #print res +"\n"
    # Filters are embeded in the cursor
    res = index.browse_from(None, res["cursor"])
    i+=1    
    if(i==2):
        sys.exit()
    print col_list    
    