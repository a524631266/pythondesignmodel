import itertools
arr = ["a","b","c","d","e"]
count = len(arr)

# def myownCombination(arr,i):
#     totallen = len(arr)
#     result =[]
#     initwindow = list(range(0,i))
#     window = range(i-1,-1,-1)
#     for i in initwindow:
#         print(i)

for i in range(1,count+1):
    for y in itertools.combinations(arr,i):
        print("".join(y))

# myownCombination(arr,2)
