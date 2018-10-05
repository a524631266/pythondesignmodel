# 常见的列表解析表达式
M = [[1,2,3],[4,5,6],[7,8,9]]

print([(i[0],i[1]) for i in M])

#添加条件的条件表达式
print([i for i in M if i[0] >3])

# 生成器
print((i for i in M if i[0] >3)) #<generator object <genexpr> at 0x7fd9ae9c63b8>
gen1 = (i for i in M if i[0] >3)
print(next(gen1))
print(next(gen1))
print(next(gen1))



a,*c = [1,2,3,4,5]
print(c)

a,b,c =[1,2]
print(c)