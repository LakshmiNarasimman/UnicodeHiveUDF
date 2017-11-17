'''
Created on 07-Nov-2017

@author: bigdata
'''
from algoliasearch import algoliasearch
import pandas as pd

alg_data=pd.read_csv("G:\\Alex_py\\price_categorization_part1_uniq_100lines.csv", sep=',',doublequote=True,engine='python')
print alg_data.count()
print alg_data.columns
#nan_filter= alg_data['product_url'].dropna(how='all')
alg_data=alg_data.dropna(subset=['product_url'])
print alg_data.count()
client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
query=""
index = client.init_index('products_v3')
alg_data.loc[alg_data['crumb.1']=='Uncategorized', 'crumb.1'] = None

for x in range(len(alg_data['product_url'])):
    queryStr={"query": query,"filters":"product_url:"+"'"+alg_data['product_url'].iloc[0]+"'"}
    res=index.browse_from(queryStr,None)
    res['hits'][0]['price_crumb']=alg_data['crumb.1'].iloc[x]
    res['hits'][0]['price_cat_id']=alg_data['cat_id'].iloc[x]