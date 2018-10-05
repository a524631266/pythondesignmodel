import sys
var = 99

def local():
    var = 0
path = "/home/zhangll/github/pythondesignmodel/0.python基本知识汇总/动态导入模块.py"
ml = sys.modules["动态导入模块"]
print(ml.var)