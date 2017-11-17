'''
Created on 23-Oct-2017

@author: bigdata
'''
import mysql.connector
from mysql.connector import Error
import json
from itertools import product

 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='test',
                                       user='root',
                                       password='root')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 

def query_with_fetchone():
    
    try:
        conn = mysql.connector.connect(host='crawler.ccnwaqixfpyj.us-east-1.rds.amazonaws.com',
                                       database='PRICE_DOT_COM_STAGING',
                                       user='crawler',
                                       password='price123')
        if conn.is_connected():
            print('Connected to MySQL database')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ASIN_TO_UPC limit 10")
 
        row = cursor.fetchone()
        product={}
        while row is not None:
            
            #print(row[0])#add it in objectID
            #print(row[1])#add it in UPC
            product['objectID']=row[0]
            product['UPC']=row[1]
            
            row = cursor.fetchone()
        print json.dumps(product)
       
            #    
 
    except Error as e:
        print(e)


if __name__ == '__main__':
    query_with_fetchone()