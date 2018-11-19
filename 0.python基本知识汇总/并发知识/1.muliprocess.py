import os 

# fork 为当前代码执行的进程中创建一个子进程,是公用一个cpu的不同时间段

ret = os.fork() # 
print(ret)
if ret>0:
    print("ret > 0 是父亲id还是子id","当前id:",os.getpid(),",父pid:",os.getppid())
else:
    print("ret == 0 是父亲id还是子id？","当前id:",os.getpid(),",父pid:",os.getppid())

#　打印结果如下
# 32268
# ret > 0 是父亲id还是子id 当前id: 32267 ,父pid: 22174
# 0
# ret == 0 是父亲id还是子id？ 当前id: 32268 ,父pid: 32267

# 可以发现 主进程会返回一个子进程的id值
# 附进程会返回一个０值