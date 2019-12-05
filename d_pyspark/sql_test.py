#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from pyspark.sql import SparkSession

if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = 'D:\green\spark-2.2.1-bin-2.6.0-cdh5.14.2' 

spark = SparkSession     .builder     .appName("spark_read_from_hive")     .master("local[2]")     .enableHiveSupport()     .getOrCreate()


# In[2]:


from pyspark.sql import *


# In[3]:


# 读取机场数据
'''
如果hdfs上的数据是按照一定的分隔符结构化数据，是可以直接使用功能read.csv读取的
'''
airports = spark.read.csv(
    'hdfs://cdh03:/input/airport-codes-na.csv',
    header='true',
    inferSchema='true',
    sep='\t'
)

airports.show(5)

# 读取起飞延迟数据
flightPref = spark.read.csv(
    'hdfs://cdh03:/input/departuredelays.csv',
    header='true'
)

flightPref.show(5)

# 读取完整的宽表数据
usa_flight = spark.read.csv(
    'hdfs://cdh03:/input/usa_flights.csv',
    header='true'
)
usa_flight.show(5)


# In[4]:


# 使用sql方式进行开发
# 注册为临时视图
airports.createOrReplaceTempView("airport")

# 注册为临时视图
flightPref.createOrReplaceTempView('flight')


# 联合两个视图数据，查询华盛顿州，各个城市的各家航空公司，起飞航班延迟的总数
spark.sql('''
select a.City,f.origin,sum(f.delay) as Delays 
   from flight f
   join airport a
   on a.IATA = f.origin
   where a.State = 'WA'
   group by a.City,f.origin
   order by sum(f.delay) desc
''').show()


# In[13]:


# 一般练习
import time

# 查看元数据信息
usa_flight.printSchema()


# In[5]:


usa_flight.schema


# In[6]:


usa_flight.columns


# In[7]:


usa_flight.count()


# In[8]:


# 手动创建一个dataframe
d = [{'name':'Alice','age':1},{'name':'Bob','age':5}]

df = spark.createDataFrame(d)

df.show()


# In[9]:


df.select('age','name')
df.select(df['age'].alias('age_value'),'name').show()
df.filter(df['name']=='Alice').show()


# In[12]:


from pyspark.sql import functions 
# 增加列
df.select(df.age +1,'age','name')

df.select(functions.lit(0).alias('id'),'age','name')

# 采用row numbuer
win = Window.partitionBy().orderBy(df['age'])
df.withColumn("id",functions.row_number().over(win)).select('id','name','age')

df.groupBy('name').agg(functions.max(df['age'])).show()


# In[10]:


usa_flight.printSchema()


# In[100]:


#usa_flight.select(functions.split('flight_date','/')[2]).show(5)

# 重新处理表结构
usa_flight.select(functions.split(functions.split('flight_date','/')[2],' ')[0].alias('year'),
                  functions.split('flight_date','/')[1].alias('month'),
                  functions.split('flight_date','/')[1].alias('day'),
                  functions.split(functions.split('flight_date','/')[2],' ')[1].alias('min'),
                 ) #.show(5)


# 计算有多少家航空公司
usa_flight.agg(functions.countDistinct('unique_carrier')) #.show(5)

# 计算每家航空公司各有多少个航班
usa_flight.groupBy('unique_carrier').agg(functions.countDistinct('flight_num').alias('num')) #.show()

# 计算每家航空公司各有多少个航班
a = usa_flight.groupBy('unique_carrier','flight_num').agg(functions.count('flight_num').alias('num')) #.show()
# 辅助验证
a.filter(a['unique_carrier']  == 'UA').orderBy(a['num'].desc()) # .show()

usa_flight.groupBy('unique_carrier','flight_num') .agg(functions.count('flight_num').alias('num')) .filter(usa_flight['unique_carrier']=='UA') #.show()

# 利用窗口函数来处理
win1 = Window.partitionBy('unique_carrier').orderBy(a['num'].desc())

# 计算各家航班延迟最高的前5个班次
a.select('unique_carrier','flight_num','num',functions.row_number().over(win1).alias('rank')) .where(functions.col('rank') <= 10) #.show()


#计算始发城市延迟的最多的班次的城市
usa_flight.groupBy('origin').agg(functions.count(functions.lit(1)).alias('num')).orderBy(functions.col('num').desc()) #.show()


# 计算每个航空公司的每个航班的平均实际花费的时间
usa_flight.groupBy('unique_carrier','flight_num')  .agg(functions.avg('actual_elapsed_time').alias('avg_time'))  .show()
 #.where(functions.col('unique_carrier')=='AA') \
 #.filter(usa_flight['flight_num']=='1') \
 #.show()


# [pyspark的udf官方文档](https://docs.databricks.com/spark/latest/spark-sql/udf-python.html#use-udf-with-dataframes)
# 
# 
# *语法格式*
# ```python
# def funx(s):
#    return xxx
# 
# spark.udf.register('自定义函数名',funx,返回类型【可选】)
# ``` 
# 
# ## 案例
# ```python
# def squared(s):
#   return s * s
# spark.udf.register("squaredWithPython", squared)
# ```
# 可选的可以定义函数的返回类型，默认是StringType
# ```python
# from pyspark.sql.types import LongType
# def squared_typed(s):
#   return s * s
# spark.udf.register("squaredWithPython", squared_typed, LongType())
# ```
# ## 在sql中调用
# ```sql
# spark.range(1, 20).registerTempTable("test")
# sql select id, squaredWithPython(id) as id_squared from test
# ```
# 
# ## 在udf中调用
# ```python
# from pyspark.sql.functions import udf
# from pyspark.sql.types import LongType
# squared_udf = udf(squared, LongType())
# df = spark.table("test")
# display(df.select("id", squared_udf("id").alias("id_squared")))
# ```
# 

# In[ ]:


from pyspark.sql.types import LongType
# 使用自定义函数
def selfRpund(x):
    return  round(x,2)

# 注册自定义函数
spark.udf.register("self_round",selfRpund,LongType())

usa_flight.createOrReplaceTempView('ua')

# 使用sql方式进行调用
spark.sql("""
select 
""")

