# MVC model-view-control
# 模型 视图 控制
# 为什么会出现三者？
# 为了解耦，也是关注点分离(SOC separation of concerns)，简化程序的维护成本
# 虽然在代码量上往往会增加一些，但是维护才是重头！！ 
# 1.model(核心)模型只关注对数据的交互部分，数据更改，只要该模型的部分就行。正
# 所谓巧妇无米之炊，没有数据哪来的展示？这里的数据包含实体的或者业务逻辑的数据
# 状态
# 2.view 视图关注的是跟用户进行交互的代码段，也就是说，视图更改，用户的接触面
# 一旦改了，那么只要改视图部分就行。主要有终端界面，ｐｄｆ文档，ｗｅｂ网页。。。
# 按照正常情况，视图不应该处理数据，然而在实际过程中，由于业务逻辑的日益变得复
# 杂，在某种无关紧要的逻辑的更改，在核心部分修改源码反而很麻烦，所以往往可能会在
# ｖｉｅｗ层写一些无关痛痒的处理逻辑
# 3.control 就是控制视图和模型之间的数据交互机制和通信，就像一个管道
# 但是MVC并不属于设计模式范畴，它更多地关注一种框架搭建（架构模式）
# 作者本意上说，因为MVC实在是太重要，所以，需要介绍
# 本人也认为很重要，因为现在目前主流的框架boot spring ,React ,django
# 都离不开MVC的思想，它更注重房子的搭建


# 名人名言打印机
# 要求　输入一个数字，就能得到一句存储在某个位置的名人名言

quotes = ('你很帅','你怎么知道我很帅','我就是帅','太帅也是一种罪')
class QuoteModel:
    """
        只关注与后台交互的数据交互，获取数据,以及业务逻辑
    """
    def get_quotes(self,index):
        """
            选择大于等于１编号的验证逻辑
        """
        try:
            if index<1:
                value = "请选择大于１的数"
            else:
                value = quotes[index]
        except IndexError as err:
            value = '找不到'
        return value
class QuoteView:
    def show(self,quote):
        print("你选择的名言为:{}".format(quote))
    def error(self,mesg):
        print("错误信息:{}".format(mesg))
    def select_quote_index(self):
        return input("请选择数据位置大小")
class QuoteControl1:
    """
        然而这里的数字验证部分应该不是control做的
    """
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteView()

    def run(self):
        valid_input = False
        while not valid_input:# 验证用户输入是否是数字
        # 用户选择的大小
            n = self.view.select_quote_index()
            try:
                n = int(n)
            except ValueError as err:
                self.view.error("问题id{}".format(n))
            else:
                valid_input = True
        quote = self.model.get_quotes(n)
        self.view.show(quote)
class QuoteControl2:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteView()
    def run(self):
        n = self.view.select_quote_index()
        quote = self.model.get_quotes(n)
        self.view.show(quote)



import pygame

from pygame.locals import * 
# pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,500)) #长400，宽300
pygame.display.set_caption('Hello World!')



def main():
    app = QuoteControl1()
    while True:
        app.run()
if __name__ == '__main__':
    main()