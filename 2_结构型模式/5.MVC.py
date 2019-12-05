# -*- coding: utf-8 -*-
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
# 同时根据模型进行对 m v c进行分别的扩展

quotes = ['你很帅','你怎么知道我很帅','我就是帅','太帅也是一种罪']
class QuoteModel:
    """
        只关注与后台交互的数据交互，获取数据,以及业务逻辑
    """
    def get_quotes(self,index):
        """
            选择大于等于１编号的验证逻辑
        """
        try:

            if index == "r":
                import random 
                value = random.choice(quotes)
            elif int(index)<1:
                value = "请选择大于１的数"
            else:
                value = quotes[int(index)]
        except IndexError as err:
            value = '找不到'
        except ValueError as err2:
            value = '请输入数值'
        return value
    def set_quote(self,quote):
        """
            给数据库添加字符串
        """
        quotes.append(quote)
    def update_quote(self,quote,index):
        """
            更新数据库
        """
        quotes[index] = quote
    def delete_quote(self,index):
        """
            删除指定位置数据
        """
        quotes.pop(index) 

class TerminalQuoteView:
    """
        专注于命令行的视图
    """
    def show(self,quote):
        terminalshowText(quote)
    def error(self,mesg):
        print("错误信息:{}".format(mesg))
    def select_quote_index(self):
        return input("请选择数据位置大小")
    def set_quote(self):
        return input("请选择你要插入的数据")

class PygameQuoteView:
    """
        专注于pygame的视图
    """
    def show(self,quote):
        pygameshowText(quote,500,400)
    def error(self,mesg):
        print("错误信息:{}".format(mesg))
    def select_quote_index(self):
        return input("请选择数据位置大小")
    def set_quote(self):
        return input("请选择你要插入的数据")

class QuoteControl1:
    """
        然而这里的数字验证部分应该不是control做的
    """
    def __init__(self):
        controlindex = int(input("choose your view index in 0=>终端　1=>pygame : "))
        self.model = QuoteModel()
        self.view = [TerminalQuoteView(),PygameQuoteView()][controlindex]

    def run(self):
        """
            控制器只专注于model与view之间的交互
        """
        valid_input = False
        while not valid_input:# 验证用户输入是否是数字
        # 用户选择的大小
            operation = int(input("请选择你要操作的序号0=>获取数据 1=>添加数据"))
            if operation == 0:
                n = self.view.select_quote_index()
                # 验证模块最好放在module中
                # try:
                #     n = int(n)
                # except ValueError as err:
                #     self.view.error("问题id{}".format(n))
                # else:
                #     valid_input = True
                quote = self.model.get_quotes(n)
                self.view.show(quote)
            elif operation == 1:
                quote2 = self.view.set_quote()
                self.model.set_quote(quote2)
            else:
                print("请选择 0 或 1 ")


def terminalshowText(text):
    print("你选择的名言为:{}".format(text))


def pygameshowText(text,width,height):
    """
        给视图添加一个pygame视图窗口
    """
    # 
    # from pygame.locals import * 
    import pygame
    import random
    pygame.init()

    ZiTi=pygame.font.get_fonts()
    fontlist = []
    for i in ZiTi:
        fontlist.append(i)
    font = random.choice(fontlist)
    
    print("选择的字体是{}".format(font))
    DISPLAYSURF = pygame.display.set_mode((width,height)) #长400，宽300
    pygame.display.set_caption('window show word')
    # BLACK = (0,0,0)
    # GREEN = (0,255,0)
    # BLUE = (0,0,128)
    blue  =  0,0,255
    white = 255,255,255
    # 一下为测试过的中文字体支持
    # arplumingcn arplumingtwmbe arplumingtw（宋体细体） 
    # notosanscjktc notosanscjkkr 宋体浅体 notosanscjksc 中体 notosanscjkjp（大粗体）
    # notosansmonocjkjp notosansmonocjksc notosansmonocjkkr（中体）  notosansmonocjktc（中体）
    # notoserifcjksc（宋体） notoserifcjkkr（宋体大粗体） notoserifcjkjp
    # droidsansfallback （中体） 
    # arplukaitwmbe arplukaihk(比较帅气，行楷) arplukaicn
    
    
    # fontObj = pygame.font.Font(my_font,32)
    my_font = pygame.font.SysFont("arplukaitwmbe",38)
    textSurfaceObj = my_font.render(u'{}'.format(text),True,white)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center=(width/2,height/2)
    DISPLAYSURF.fill(blue)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    pygame.display.update()

def main():
    app = QuoteControl1()
    app.run()
if __name__ == '__main__':
    main()