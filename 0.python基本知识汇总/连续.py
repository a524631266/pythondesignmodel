
arr = [2,3,5,6,2,3,5,6,1,5,6,2,2,2]
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
    if end_positon>len(arr):
        return
    win = arr[count:end_positon]
    if ifduplicate(win) or ifconitueincrease(win):
        result.add(tuple(win))
        check(arr,count,oncelen+1)
    else:
        check(arr,count+1,3)
check(arr1,0,3)
print("arr1",arr1)
print("arr2",arr2)
check(arr2,0,3)
print(result)

