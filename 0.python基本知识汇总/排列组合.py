import itertools
arr = ["a","b","c","d","e"]
count = len(arr)

def myownCombination(arr,i):
    totallen = len(arr)
    result =[]
    initwindow = list(range(0,i))
    window = list(range(i-1,-1,-1))
    for ii in window:
        print("sssssssss",ii)
        for jj in range(ii,totallen):
            print(ii,jj)


# ######### 版本1 ##########
# for i in range(1,count+1):
#     for y in itertools.combinations(arr,i):
#         print("".join(y))

# ######### 版本2 ##########
# for i in range(1,count+1):
#     for y in myownCombination(arr,i):
#         print("".join(y))


myownCombination(arr,3)

