# 给出一个数组 范围是1到10 一共21个数字
# 然后其中要对他进行组合 规定只能连续三个数字可以组合一次 同样3个数字可以组合一次 
# 要求:
# 1.要么连续如1,2,3   3,4,5  4,5,6
# 2.要么一样如1,1,1   3,3,3  5,5,5
# 3.长度至少为三组
# 如给出一个数组[1,2,3,3,3,3,4,5,6];
# 可以得出【1,2,3】【3,3,3】，【4,5,6】


import random
initarr = list(range(1,11))
arr = []
for i in range(21):
    arr.append(random.choice(initarr))
arr=  [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 7, 8, 8, 8, 9, 9, 10,10,10,10]
arr1 = sorted(arr) #升序数据
arr2 = list(set(arr1)) #剔除重复升序数据
def ifconitueincrease(arr):# 判断是否连续增加
    count =len(arr)
    for i in range(count-1,0,-1):
        if arr[i]-arr[i-1] != 1:
            return False
    else:
        return True
def ifduplicate(arr):# 判断是否重复
    count = len(arr)
    for i in range(count-1,0,-1):
        if arr[i]-arr[i-1] != 0:
            return False
    else:
        return True
result = set() # 定义不重复的set结构
def check(arr,count,oncelen): # 对升序不剔除数据进行判断是否重复
    end_positon = count + oncelen
    if end_positon>len(arr) and (oncelen==3):
        return 0
    win = arr[count:end_positon]
    if (ifduplicate(win) or ifconitueincrease(win)) :
        if end_positon>len(arr) and oncelen>3:
            check(arr,count+1,3)
        else:
            print("正确",win)
            result.add(tuple(win))
            check(arr,count,oncelen+1)
    else:
        print("错误",win)
        check(arr,count+1,3)

check(arr1,0,3)
print("arr1:\n",arr1)
check(arr2,0,3)
print("arr2:\n",arr2)
print("result\n",result)

