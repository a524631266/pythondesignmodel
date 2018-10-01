# builder模式类似与快餐模式
# 快餐模式有三个参与者 ,假定用户购买一种汉堡包(可能会有多种)
# 1. 客户(发起者) ==> 负责发起购买 汉堡包1
# 2. 收营员(指挥者) ==> 确认订单并通知餐厅员工制作订单
# 3. 餐厅员工(制作者) ==> 制作汉堡包1 并送给 客户
### 在这里 汉堡包1的构建
# 1.需要通过一长串的步骤(环环相扣)才能生产,
# 2.同时这个同一个过程能够产生不同的表现(汉堡包1,2...)
# 这也是区别不factory直接生成的区别

# 工厂模式与builder模式的区别

########工厂模式########
MINI4 = "MINI4"

class ComputerFactory:
    class Computer:
        def __init__(self,name):
            self.computername = name
            self.cpu = "2GHZ"
            self.memory = "12G"
        def __str__(self):
            return "name:{},cpu:{},memory:{}".format(self.computername,self.cpu,self.memory)

    def build_computer(self,model):
        if model == MINI4:
            return self.Computer(model)
        else:
            print("i dont know how to build {}".format(model))
def main():
    afac = ComputerFactory()
    computer = afac.build_computer(MINI4)
    print(computer)


########快餐模式########
### 定制电脑  
### 1.创建一个电脑模型
class Computer:
    def __init__(self,name):
        self.computername = name
        self.cpu = "2GHZ"
        self.memory = "12G"
    def __str__(self):
        return "name:{},cpu:{},memory:{}".format(self.computername,self.cpu,self.memory)
###２．创建一个可以制作者
class ComputerBuilder:
    def __init__(self,name):
        self.computer = Computer(name)
    def confi_cpu(self,cpu):
        self.computer.cpu = cpu
    def confi_memory(self,memory):
        self.computer.memory = memory

#### 3.创建一个收营员或则厂商 引擎
class HardwareEnginer:
    def __init__(self):
        self.builder = None
    def construct_compouter(self,computername,cpu,memory):
        self.builder = ComputerBuilder(computername)
        self.builder.confi_cpu(cpu)
        self.builder.confi_memory(memory)
    @property
    def computer(self):
        return self.builder.computer

def main2():
    enginer = HardwareEnginer()
    enginer.construct_compouter("imac","10GHZ","20G")
    print(enginer.computer)
if __name__ == '__main__':
    print("工厂模式")
    main() 
    print("快餐模式")
    main2()