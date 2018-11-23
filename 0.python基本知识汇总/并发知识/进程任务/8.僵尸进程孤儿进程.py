import os
import time
ret = os.fork()
# 孤儿进程
if ret > 0:
    print("主进程",os.getpid())
else:
    print("子进程",os.getpid())
    time.sleep(100)
    #  通过 ps -ef | grep 子进程id发现，其父亲进程变成了1 1号进程就是托儿所，所有进程由托儿所创建，如果
    # 子进程有父亲在,那么由父亲管理,所以叫做孤儿进程
# 僵尸进程
# 在父进程还存在的时候,儿子已经死掉了,但是父亲还不知道,但是同时儿子进程还会占用一定的资源
#  同时通过 top 看到 有个zombie 为1