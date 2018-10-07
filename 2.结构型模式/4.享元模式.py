# why?
# 享元模式 (FlyWeight)
# 多个模块共享一个内存中的数据对象(不变状态对象)
# 目的是为了最小化内存的使用
# way: 1.3d模型的一些通用3D信息(房子,森林,士兵外在表现以及相应的动作,(but 生命状态,枪支类型,地理位置))

# 所以 FW是用来优化的设计方案

# 享元则是一种特定于面向对象编程优化的设计模式,关注的是共享对象数据 与 memorization(缓存)相区别[应用
# 于方法或函数]

from enum import Enum
# this type of the tree enum store the share data
Tree_type = Enum("Tree_type","Atree Btree Ctree")
class Tree:
    pool = {}
    def __new__(cls,tree_type,**keywards):
        obj = cls.pool.get(tree_type,None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type]= obj
        return obj
    def __init__(self,tree_type):
        self.type = tree_type
    def __str__(self):
        return str(self.type)
    def render(self,age,x,y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.type,
age, x, y))
    
def main():
    for i in range(10):
        tree = Tree(Tree_type.Atree)
        tree.render(10,9,8)
        # print(tree)
        # print(Tree.pool)
    print(len(Tree.pool))
    for i in range(5):
        tree = Tree(Tree_type.Btree)
        # print(tree)
        # print(Tree.pool)
    print(len(Tree.pool))
    for i in range(8):
        tree = Tree(Tree_type.Ctree)
        # print(tree)
    print(len(Tree.pool))

Skin = Enum("Skin","yellow white black")

class FPSoldier:
    # variable height weight 
    
if __name__ == '__main__':
    main()