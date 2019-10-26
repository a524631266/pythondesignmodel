RDD - API

#### 创建RDD

接下来我们使用parallelize方法创建一个RDD：

>```python
>intRDD = sc.parallelize([3,1,2,5,5])
>stringRDD = sc.parallelize(['Apple','Orange','Grape','Banana','Apple'])
>```



#### RDD转换为Python数据类型

RDD类型的数据可以使用collect方法转换为python的数据类型：

>```python
>print (intRDD.collect())
>print (stringRDD.collect())
>```
>
>

输出为：

>[3, 1, 2, 5, 5]
>['APPLE', 'Orange', 'Grape', 'Banana','Apple']

#### map运算

map运算可以通过传入的函数，将每一个元素经过函数运算产生另外一个RDD。
比如下面的代码中，将intRDD中的每个元素加1之后返回，并转换为python数组输出：

>```python
>print (intRDD.map(lambda x:x+1).collect())
>```

结果为：

```json
[4, 2, 3, 6, 6]
```

#### filter运算

filter可以用于对RDD内每一个元素进行筛选，并产生另外一个RDD。
下面的例子中，我们筛选intRDD中数字小于3的元素，同事筛选stringRDD中包含ra的字符串：

```python
print (intRDD.filter(lambda x: x<3).collect())
print (stringRDD.filter(lambda x:'ra' in x).collect())
```

输出为：

```json
 [1, 2]
 ['Orange', 'Grape']
```

#### distinct运算

distinct运算会删除重复的元素，比如我们去除intRDD中的重复元素1：

```css
print (intRDD.distinct().collect())
```

输出为：

```json
[1, 2, 3, 5]
```

#### randomSplit运算

randomSplit 运算将整个集合以随机数的方式按照比例分为多个RDD，比如按照0.4和0.6的比例将intRDD分为两个RDD，并输出：

```go
sRDD = intRDD.randomSplit([0.4,0.6])
print (len(sRDD))
print (sRDD[0].collect())
print (sRDD[1].collect())
```

输出为：

```json
2
[3, 1]
[2, 5, 5]
```

#### groupBy运算

groupBy运算可以按照传入匿名函数的规则，将数据分为多个Array。比如下面的代码将intRDD分为偶数和奇数：

```python
result = intRDD.groupBy(lambda x : x % 2).collect()
print (sorted([(x, sorted(y)) for (x, y) in result]))
```

输出为：

```json
[(0, [2]), (1, [1, 3, 5, 5])]
```

## 3、多个RDD转换运算

RDD也支持执行多个RDD的运算，这里，我们定义三个RDD：

```undefined
intRDD1 = sc.parallelize([3,1,2,5,5])
intRDD2 = sc.parallelize([5,6])
intRDD3 = sc.parallelize([2,7])
```

#### 并集运算

可以使用union函数进行并集运算：

```css
print (intRDD1.union(intRDD2).union(intRDD3).collect())
```

输出为:

```json
[3, 1, 2, 5, 5, 5, 6, 2, 7] 
```

#### 交集运算

可以使用intersection进行交集运算：

```css
print (intRDD1.intersection(intRDD2).collect())
```

两个集合中只有一个相同元素5，所以输出为：

```json
[5] 
```

#### 差集运算

可以使用subtract函数进行差集运算：

```css
print (intRDD1.subtract(intRDD2).collect())
```

由于两个RDD的重复部分为5，所以输出为[1,2,3]:

```json
[2, 1, 3]
```

#### 笛卡尔积运算

可以使用cartesian函数进行笛卡尔乘积运算:

```css
print (intRDD1.cartesian(intRDD2).collect())
```

由于两个RDD分别有5个元素和2个元素，所以返回结果有10各元素：

```json
[(3, 5), (3, 6), (1, 5), (1, 6), (2, 5), (2, 6), (5, 5), (5, 6), (5, 5), (5, 6)]
```

## 4、基本“动作”运算

#### 读取元素

可以使用下列命令读取RDD内的元素，这是Actions运算，所以会马上执行：

```python
#取第一条数据
print (intRDD.first())
#取前两条数据
print (intRDD.take(2))
#升序排列，并取前3条数据
print (intRDD.takeOrdered(3))
#降序排列，并取前3条数据
print (intRDD.takeOrdered(3,lambda x:-x))
```

输出为：

```json
3
[3, 1]
[1, 2, 3]
[5, 5, 3]
```

#### 统计功能

可以将RDD内的元素进行统计运算：

```bash
#统计
print (intRDD.stats())
#最小值
print (intRDD.min())
#最大值
print (intRDD.max())
#标准差
print (intRDD.stdev())
#计数
print (intRDD.count())
#求和
print (intRDD.sum())
#平均
print (intRDD.mean())
```

输出为：

```css
(count: 5, mean: 3.2, stdev: 1.6, max: 5, min: 1)
1
5
1.6
5
16
3.2
```

## 5、RDD Key-Value基本“转换”运算

Spark RDD支持键值对运算，Key-Value运算时mapreduce运算的基础，本节介绍RDD键值的基本“转换”运算。

#### 初始化

我们用元素类型为tuple元组的数组初始化我们的RDD，这里，每个tuple的第一个值将作为键，而第二个元素将作为值。

```undefined
kvRDD1 = sc.parallelize([(3,4),(3,6),(5,6),(1,2)])
```

#### 得到key和value值

可以使用keys和values函数分别得到RDD的键数组和值数组：

```css
print (kvRDD1.keys().collect())
print (kvRDD1.values().collect())
```

输出为：

```json
[3, 3, 5, 1]
[4, 6, 6, 2]
```

#### 筛选元素

可以按照键进行元素筛选，也可以通过值进行元素筛选，和之前的一样，使用filter函数，这里要注意的是，虽然RDD中是以键值对形式存在，但是本质上还是一个二元组，二元组的第一个值代表键，第二个值代表值，所以按照如下的代码既可以按照键进行筛选，我们筛选键值小于5的数据：

```css
print (kvRDD1.filter(lambda x:x[0] < 5).collect())
```

输出为：

```json
[(3, 4), (3, 6), (1, 2)]
```

同样，将x[0]替换为x[1]就是按照值进行筛选，我们筛选值小于5的数据：

```css
print (kvRDD1.filter(lambda x:x[1] < 5).collect())
```

输出为：

```json
[(3, 4), (1, 2)]
```

#### 值运算

我们可以使用mapValues方法处理value值，下面的代码将value值进行了平方处理：

```css
print (kvRDD1.mapValues(lambda x:x**2).collect())
```

输出为：

```json
[(3, 16), (3, 36), (5, 36), (1, 4)]
```

#### 按照key排序

可以使用sortByKey按照key进行排序，传入参数的默认值为true，是按照从小到大排序，也可以传入参数false，表示从大到小排序：

```css
print (kvRDD1.sortByKey().collect())
print (kvRDD1.sortByKey(True).collect())
print (kvRDD1.sortByKey(False).collect())
```

输出为：

```json
[(1, 2), (3, 4), (3, 6), (5, 6)]
[(1, 2), (3, 4), (3, 6), (5, 6)]
[(5, 6), (3, 4), (3, 6), (1, 2)]
```

#### 合并相同key值的数据

使用reduceByKey函数可以对具有相同key值的数据进行合并。比如下面的代码，由于RDD中存在（3,4）和（3,6）两条key值均为3的数据，他们将被合为一条数据：

```css
print (kvRDD1.reduceByKey(lambda x,y:x+y).collect())
```

输出为

```json
[(1, 2), (3, 10), (5, 6)]
```

## 6、多个RDD Key-Value“转换”运算

#### 初始化

首先我们初始化两个k-v的RDD：

```undefined
kvRDD1 = sc.parallelize([(3,4),(3,6),(5,6),(1,2)])
kvRDD2 = sc.parallelize([(3,8)])
```

#### 内连接运算

join运算可以实现类似数据库的内连接，将两个RDD按照相同的key值join起来，kvRDD1与kvRDD2的key值唯一相同的是3，kvRDD1中有两条key值为3的数据（3,4）和（3,6），而kvRDD2中只有一条key值为3的数据（3,8），所以join的结果是（3，（4,8）） 和（3，（6，8））：

```css
print (kvRDD1.join(kvRDD2).collect())
```

输出为:

```json
[(3, (4, 8)), (3, (6, 8))] 
```

#### 左外连接

使用leftOuterJoin可以实现类似数据库的左外连接，如果kvRDD1的key值对应不到kvRDD2，就会显示None

```css
print (kvRDD1.leftOuterJoin(kvRDD2).collect())
```

输出为:

```json
[(1, (2, None)), (3, (4, 8)), (3, (6, 8)), (5, (6, None))]
```

#### 右外连接

使用rightOuterJoin可以实现类似数据库的右外连接，如果kvRDD2的key值对应不到kvRDD1，就会显示None

```css
print (kvRDD1.rightOuterJoin(kvRDD2).collect())
```

输出为：

```json
[(3, (4, 8)), (3, (6, 8))]
```

#### 删除相同key值数据

使用subtractByKey运算会删除相同key值得数据：

```css
print (kvRDD1.subtractByKey(kvRDD2).collect())
```

结果为：

```json
[(1, 2), (5, 6)] 
```

## 7、Key-Value“动作”运算

#### 读取数据

可以使用下面的几种方式读取RDD的数据：

```bash
#读取第一条数据
print (kvRDD1.first())
#读取前两条数据
print (kvRDD1.take(2))
#读取第一条数据的key值
print (kvRDD1.first()[0])
#读取第一条数据的value值
print (kvRDD1.first()[1])
```

输出为:

```csharp
(3, 4)
[(3, 4), (3, 6)]
3
4
```

#### 按key值统计：

使用countByKey函数可以统计各个key值对应的数据的条数：

```css
print (kvRDD1.countByKey().collect())
```

输出为：

```bash
defaultdict(<type 'int'>, {1: 1, 3: 2, 5: 1})
```

#### lookup查找运算

使用lookup函数可以根据输入的key值来查找对应的Value值：

```bash
print (kvRDD1.lookup(3))
```

输出为：

```json
[4, 6]
```

## 8、持久化操作

spark RDD的持久化机制，可以将需要重复运算的RDD存储在内存中，以便大幅提升运算效率，有两个主要的函数：

#### 持久化

使用persist函数对RDD进行持久化：

```css
kvRDD1.persist()
```

在持久化的同时我们可以指定持久化存储等级：

| 等级                                   | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| More ActionsMEMORY_ONLY                | 以反序列化的JAVA对象的方式存储在JVM中. 如果内存不够， RDD的一些分区将不会被缓存， 这样当再次需要这些分区的时候，将会重新计算。这是默认的级别。 |
| MEMORY_AND_DISK                        | 以反序列化的JAVA对象的方式存储在JVM中. 如果内存不够， RDD的一些分区将将会缓存在磁盘上，再次需要的时候从磁盘读取。 |
| MEMORY_AND_DISK                        | 以反序列化的JAVA对象的方式存储在JVM中. 如果内存不够， RDD的一些分区将将会缓存在磁盘上，再次需要的时候从磁盘读取。 |
| MEMORY_ONLY_SER                        | 以序列化JAVA对象的方式存储 (每个分区一个字节数组). 相比于反序列化的方式,这样更高效的利用空间， 尤其是使用快速序列化时。但是读取是CPU操作很密集。 |
| MEMORY_AND_DISK_SER                    | 与MEMORY_ONLY_SER相似, 区别是但内存不足时，存储在磁盘上而不是每次重新计算。 |
| DISK_ONLY                              | 只存储RDD在磁盘                                              |
| MEMORY_ONLY_2, MEMORY_AND_DISK_2, etc. | 与上面的级别相同，只不过每个分区的副本只存储在两个集群节点上。 |
| OFF_HEAP                               | 将RDD以序列化的方式存储在 Tachyon. 与 MEMORY_ONLY_SER相比, OFF_HEAP减少了垃圾回收。允许执行体更小通过共享一个内存池。因此对于拥有较大堆内存和高并发的环境有较大的吸引力。更重要的是，因为RDD存储在Tachyon上，执行体的崩溃不会造成缓存的丢失。在这种模式下.Tachyon中的内存是可丢弃的，这样 Tachyon 对于从内存中挤出的块不会试图重建它。如果你打算使用Tachyon作为堆缓存，Spark提供了与Tachyon相兼容的版本 |
|                                        |                                                              |
|                                        |                                                              |

首先我们导入相关函数：

```jsx
from pyspark.storagelevel import StorageLevel
```

在scala中可以直接使用上述的持久化等级关键词，但是在pyspark中封装为了一个类，
StorageLevel类，并在初始化时指定一些参数，通过不同的参数组合，可以实现上面的不同存储等级。StorageLevel类的初始化函数如下：

```ruby
    def __init__(self, useDisk, useMemory, useOffHeap, deserialized, replication=1):
        self.useDisk = useDisk
        self.useMemory = useMemory
        self.useOffHeap = useOffHeap
        self.deserialized = deserialized
        self.replication = replication
```

那么不同的存储等级对应的参数为:

```python
StorageLevel.DISK_ONLY = StorageLevel(True, False, False, False)
StorageLevel.DISK_ONLY_2 = StorageLevel(True, False, False, False, 2)
StorageLevel.MEMORY_ONLY = StorageLevel(False, True, False, False)
StorageLevel.MEMORY_ONLY_2 = StorageLevel(False, True, False, False, 2)
StorageLevel.MEMORY_AND_DISK = StorageLevel(True, True, False, False)
StorageLevel.MEMORY_AND_DISK_2 = StorageLevel(True, True, False, False, 2)
StorageLevel.OFF_HEAP = StorageLevel(True, True, True, False, 1)

"""
.. note:: The following four storage level constants are deprecated in 2.0, since the records \
will always be serialized in Python.
"""
StorageLevel.MEMORY_ONLY_SER = StorageLevel.MEMORY_ONLY
""".. note:: Deprecated in 2.0, use ``StorageLevel.MEMORY_ONLY`` instead."""
StorageLevel.MEMORY_ONLY_SER_2 = StorageLevel.MEMORY_ONLY_2
""".. note:: Deprecated in 2.0, use ``StorageLevel.MEMORY_ONLY_2`` instead."""
StorageLevel.MEMORY_AND_DISK_SER = StorageLevel.MEMORY_AND_DISK
""".. note:: Deprecated in 2.0, use ``StorageLevel.MEMORY_AND_DISK`` instead."""
StorageLevel.MEMORY_AND_DISK_SER_2 = StorageLevel.MEMORY_AND_DISK_2
""".. note:: Deprecated in 2.0, use ``StorageLevel.MEMORY_AND_DISK_2`` instead."""
```

#### 取消持久化

使用unpersist函数对RDD进行持久化：

```css
kvRDD1.unpersist()
```

## 9、整理回顾

哇，有关pyspark的RDD的基本操作就是上面这些啦，想要了解更多的盆友们可以参照官网给出的官方文档：[http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD](https://link.jianshu.com/?t=http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD)

今天主要介绍了两种RDD，基本的RDD和Key-Value形式的RDD，介绍了他们的几种“转换”运算和“动作”运算，整理如下：

|RDD运算 | 说明 |
| ------------- |:-------------:| -----:|
|基本RDD“转换”运算 | map（对各数据进行转换），filter（过滤符合条件的数据），distinct（去重运算），randomSplit（根据指定的比例随机分为N各RDD），groupBy（根据条件对数据进行分组），union（两个RDD取并集），intersection（两个RDD取交集），subtract（两个RDD取差集）。cartesian（两个RDD进行笛卡尔积运算） |
| 基本RDD“动作”运算 | first（取第一条数据），take（取前几条数据），takeOrdered（排序后取前N条数据），统计函数 |
| Key-Value形式 RDD“转换”运算 | filter（过滤符合条件的数据），mapValues（对value值进行转换），sortByKey（根据key值进行排序），reduceByKey（合并相同key值的数据），join（内连接两个KDD），leftOuterJoin（左外连接两个KDD），rightOuterJoin（右外连接两个RDD），subtractByKey（相当于key值得差集运算） |
| Key-Value形式 RDD“动作”运算 | first（取第一条数据），take（取前几条数据），countByKey（根据key值分组统计），lookup（根据key值查找value值） |
| RDD持久化 |persist用于对RDD进行持久化，unpersist取消RDD的持久化，注意持久化的存储等级 |