'''
Created on 09-Nov-2017

@author: bigdata
'''
from pyspark import SparkConf,SparkContext
from pyspark.sql import *
from time import time
sparkConf = SparkConf().setAppName("Titanic").setMaster("local")
sc = SparkContext(conf = sparkConf)
sqlContext = SQLContext(sc)
    
# 
# rdd_data=sc.textFile("file:///tmp/mozilla_bigdata0/train.csv")
# header = rdd_data.first()
# print header.collect()
# new_rdd=rdd_data.subtract(header)
# 
# print new_rdd.take(10)
# result=rdd_data.map(lambda s:s.split(','))
# df=sqlContext.createDataFrame(result.map(lambda p:Row(PassengerId=int(p[0]),Survived=int(p[1]),Pclass=int(p[2]),Name=p[3],Sex
# =p[4],Age=int(p[5]),SibSp=int(p[6]),Parch=int(p[7]),Ticket=p[8],Fare=float(p[9]),Cabin=p[10],Embarked=p[11])))
# print df.head(10)
t0 = time()
df = sqlContext.read.format('com.databricks.spark.csv').options(header='true').load('file:///tmp/mozilla_bigdata0/train.csv')
print df.count()
results = df.groupBy(df['Age']).count().sort("count",ascending=False)
for x in results.collect():
    print x
    
tt = str(time() - t0)
print "DataFrame performed in " + tt + " seconds"
df.registerTempTable("orders")   
results = sqlContext.sql("SELECT Age, count(*) AS total_count FROM orders GROUP BY Age ORDER BY total_count DESC") 
results.show()
tt = str(time() - t0)

print "DataFrame performed in " + tt + " seconds"