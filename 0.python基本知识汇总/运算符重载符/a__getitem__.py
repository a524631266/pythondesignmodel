# __getitem__方法为类中方法获取切片数据

class Indexer:
    data = [1,5,3,4,5,6,7]
    def __getitem__(self,sliceindex):
        print("重载符号:%s"%(sliceindex))
        return self.data[sliceindex]
def main():
    # 使用方法1
    print("111",Indexer()[1:3])
    # 使用方法2
    for i in Indexer():
        print("{}........".format(i))
    # 关系测试in
    print("78 关系是否在 {}".format( 5 in Indexer()))
    # 列表解析
    print("222",[i for i in Indexer()])
    # 内置函数 map
    print(*map(lambda x : x * 2,Indexer()))
    # 总结 有 for循环(迭代)语句的都会调用 getitem
    
if __name__ == '__main__':
    main()
