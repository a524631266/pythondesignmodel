from multiprocessing import Pool,Manager
import os
# q存储队列名字
q = Manager().Queue()

def copyf(name,rf,insertdirname,q):
    # print("copyf",name,os.getpid())
    with open(os.path.join(rf,name),"r") as f:
        data = f.read()
    with open(os.path.join(insertdirname,name),"w") as f:
        f.write(data)
    q.put(name)
# def readf(q,rf,insertdirname):
#     os.mkdir(insertdirname)
#     filenames = os.listdir(rf)
#     for name in filenames:
#         print("readf",os.getpid())
#         q.put(name)

def main():
    rf = input("输入要拷贝的文件夹: ")
    insertdirname = rf+"copy"
    os.mkdir(insertdirname)
    # 开启一个池子
    p = Pool(2)
    # 这里还是两个任务
    filenames = os.listdir(rf)
    for name in filenames:
        # print("readf",os.getpid())
        p.apply_async(copyf, args=(name,rf,insertdirname,q))
    # 方法一
    # p.close()
    # p.join()
    # 方法二，功能解耦，查看信息
    num = 0
    totalnum = len(filenames)
    while True:
        q.get()
        num += 1
        print("\r进度条 %f %%"%(num/totalnum * 100),end="")
        if num == totalnum:
            break
if __name__ == "__main__":
    main()