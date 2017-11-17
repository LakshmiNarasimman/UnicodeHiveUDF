'''
Created on 25-Oct-2017

@author: bigdata
'''
import datetime
from datetime import date
import time
import os
import json
print time.time()
print date.fromtimestamp(time.time())
print date.fromordinal(10000)   
currentDate=date.fromtimestamp(time.time())
print currentDate.strftime("%d-%m-%Y")
print os.pardir
print date.today()
print time.strftime("%d-%m-%Y")
help(json)