'''
Created on 02-Nov-2017

@author: bigdata
'''
from algoliasearch import algoliasearch
import pandas as pd


alg_data=pd.read_csv("/tmp/mozilla_bigdata0/price_categorization_part1_uniq_100lines.csv")

print alg_data.columns
nan_filter= alg_data['product_url'].dropna(how='all')
client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
query=""
index = client.init_index('products_v3')
mask=alg_data['crumb.1']=='Uncategorized'
alg_data[mask]="null"
alg_data = alg_data.drop(alg_data[alg_data['product_url']=='NaN'].index)
for x in range(len(nan_filter)):
    queryStr={"query": query,"filters":"product_url:"+"'"+nan_filter.iloc[0]+"'"}
    res=index.browse_from(queryStr,None)
    res['price_crumb_crum']=alg_data['crumb.1'].iloc[x]
    res['price_cat_id']=alg_data['cat_id'].iloc[x]
    print res['hits'][0]
    print x
