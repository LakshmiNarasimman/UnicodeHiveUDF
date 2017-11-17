'''
Created on 30-Oct-2017

@author: bigdata
'''
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import os

sparkConf = SparkConf().setAppName("WordCounts").setMaster("local")
sc = SparkContext(conf = sparkConf)
sqlContext = SQLContext(sc)
 
def write_to_ES():
    df = sqlContext.read.format('com.databricks.spark.csv').options(header='true').load('/user/bigdata/train.csv')
    df.head()
    df.registerTempTable("data")
    df.printSchema()
    kpi1 = sqlContext.sql("SELECT Pclass,Name,Age,Sex,Survived FROM data where Survived=1")
    print kpi1.show()
    es_conf = {"es.nodes" : "localhost","es.port" : "9200","es.nodes.client.only" : "true","es.resource" : "movies/set1"}
    #df.write.format("org.elasticsearch.spark.sql").option("es.nodes" ,"localhost").option("es.port",9200).save("titanic1/set2")
write_to_ES()    
'''    
    
    
#Configure the Spark environment
sparkConf = SparkConf().setAppName("WordCounts").setMaster("local")
sc = SparkContext(conf = sparkConf)
rdd_data=sc.textFile("/user/bigdata/train.csv")
for x in rdd_data.take(10):
    print x
header=rdd_data.take(1)    
def write_to_ES():
    sqlContext = SQLContext(sc)
    es_conf = {"es.nodes" : "localhost","es.port" : "9200","es.nodes.client.only" : "true","es.resource" : "movies/set1"}
    schemaString = header
    print schemaString
    fields = [StructField(field_name, StringType(), True) for field_name in str(schemaString).split(',').replace(']',',').replace('[')]
    schema = StructType(fields)
    es_df_p = sqlContext.read.csv("/user/bigdata/train.csv",inferSchema=True,schema=schema)
    print es_df_p.printSchema()
    es_df_pf= es_df_p.groupBy("Sex").count().map(lambda (a,b): ('id',{'element_id': a,'count': b}))
    es_df_pf.saveAsNewAPIHadoopFile(
    path='-',
    outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
    keyClass="org.apache.hadoop.io.NullWritable",
    valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
    conf=es_conf)    
if __name__ == "__main__":
    write_to_ES()    

#The WordCounts Spark program
# textFile = sc.textFile("hdfs://BigData:50000/user/bigdata/train.csv")
# wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
# for wc in wordCounts.collect(): print wc

'''