import sys
var = 99

def local():
    var = 0
path = "/home/zhangll/github/pythondesignmodel/0.python基本知识汇总/动态导入模块.py"

# ml = sys.modules["动态导入模块"]
ml = __import__(path)

print(ml.var)

# 与sys.modules相关的动态导入模块的导入相关的关键字为__import__
# __import__("PATH") 把路径导入指定模块，用来加载到python运行时环境中的全局变量中
