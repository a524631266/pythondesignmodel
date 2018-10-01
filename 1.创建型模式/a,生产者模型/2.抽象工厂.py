#一组用于创建一系列相关事物对象的工厂方法
# 工厂函数只是创建一个简单的对象
# 抽象工厂是建立在工厂函数之上的,是工厂函数的一般化(泛化)
# 简单地说,抽象工厂负责 各个生产函数(不同对象)的场所


#########################抽象工厂生成一个青蛙世界########### 
class Frog:
    '''
    一个青蛙的实例
    '''
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return '\n\n\t-------青蛙世界...'
    def interact_with(self,obstacle):
        print('{} 青蛙遇到了 {} 并且 {}'.format(self,obstacle,obstacle.action()))

class Bug:
    '''
    障碍物1 青蛙
    '''
    def __init__(self):
        pass
    def __str__(self):
        return "一只青蛙"
    def action(self):
        return '吃了它'

# 抽象工厂,这个工厂是用来生成 两个对象的
class FrogWorld:
    def __init__(self,frogname):
        print("生成一只青蛙")
        self.palyername = frogname
    
    def make_charactor(self):
        return Frog(self.palyername)
    
    def make_obstacle(self):
        return Bug()
    

#########################抽象工厂生成一个成年人的男巫大战怪兽########### 

class Wizard:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return '\n\n\t-------男巫世界...'
    def interact_with(self,obstacle):
        print('{} 男巫遇到了 {} 并且 {}'.format(self,obstacle,obstacle.action()))

class Ork:
    def __init__(self):
        pass
    def __str__(self):
        return "一只怪兽"
    def action(self):
        return '打败了怪兽'

# 抽象工厂,这个工厂是用来生成 两个对象的
class WizardWorld:
    def __init__(self,frogname):
        print("生成一个男巫")
        self.palyername = frogname
    
    def make_charactor(self):
        return Wizard(self.palyername)
    
    def make_obstacle(self):
        return Ork()

################我们的目标是根据年龄来判断是玩青蛙世界还是男巫世界#####################
class GamePlayGround:
    def __init__(self,factory):
        self.hero = factory.make_charactor()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.hero.interact_with(self.obstacle)


def main():
    pass
# 验证年龄
def validate_age(name):
    try:
        age = input("欢迎{},请问你多大?".format(name))
        age = int(age)
    except ValueError as err:
        print(err)
        return (False,age)
    return (True,age)
if __name__ == '__main__':
    name = input("请输入你的姓名")
    valid_input = False
    while not valid_input:
        valid_input,age = validate_age(name)
    world = FrogWorld if age <18 else WizardWorld
    GamePlayGround(world(name)).play()
