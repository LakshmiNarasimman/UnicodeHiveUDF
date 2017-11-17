'''
Created on 23-Oct-2017

@author: bigdata
'''
from algoliasearch import algoliasearch
import json
import pandas as pd
from collections import OrderedDict
import csv
'''
def connect_algoliaSearch():
    client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
    index = client.init_index('products_v3')
    hits = []
    print "Querying the index..."
    for hit in index.browse_all({"query": "iphone 6 64 gb"}):
        hits.append(hit)
    print "Finished Querying.."    
    json_string = json.dumps(hits,sort_keys=False)
    dicts= json.loads(json_string, object_pairs_hook=OrderedDict) 
    df=pd.DataFrame(dicts,columns=dicts[0].keys()) 
    print "Downloading the file.."
    df.to_csv("/home/bigdata/bigdata_noahdata/Alex_Py/cal.csv",chunksize=100000,index=False,encoding='utf-8')
    print json.dumps(hits,indent=4,sort_keys=False) 
connect_algoliaSearch()    
'''

with open('/home/bigdata/bigdata_noahdata/Alex_Py/test_encode_output.csv', 'wb') as csvfile:
    output_file = csv.writer(csvfile)
    client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
    index = client.init_index('products_v3')
    hits = []
    print "Querying the index..."
    for hit in index.browse_all({"query": "iphone 6 64 gb"}):
        output_file.writerow([hit])