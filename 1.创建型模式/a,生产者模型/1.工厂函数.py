#　工厂函数在python中代表一个函数
#  通过不同函数输入输出不同对象 
# python django field(max_length="" )
# http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns?responseToken=b46ed23cd6b6b08db75e28493c1b5566

# 多数据源对象管理
# 比如数据源多样化,最后想通过一个函数(工厂函数)进行对象的统一管理

import json
import xml.etree.ElementTree as etree
import abc
import six
class A():
    pass

## 定义抽象类 1
class Connector1(object,metaclass=abc.ABCMeta):
    def __init__(self,filepath):
        pass

    @abc.abstractproperty
    def parsed_data(self):
        pass

    @abc.abstractproperty
    def print(self):
        pass
## 定义抽象类 2
@six.add_metaclass(abc.ABCMeta)
class Connector(object):
    def __init__(self,filepath):
        pass

    @abc.abstractproperty
    def parsed_data(self):
        pass

    @abc.abstractproperty
    def print(self):
        pass


class JsonConnector(Connector):
    def __init__(self,filepath):
        self.data = dict()
        with open(filepath,mode="r",encoding="utf-8") as f:
            self.data = json.load(f)
    @property
    def parsed_data(self):
        return self.data

    def print(self):
        pass
    
class XmlConnector(Connector):
    def __init__(self,filepath):
        self.data = etree.parse(filepath)
        
    @property
    def parsed_data(self):
        return self.data
    def print(self):
        pass

## 工厂方法统一管理数据库链接
def errorcatch(func):
    def warper(filepath):
        try:
            return func(filepath)
        except ValueError as ve:
            print(ve)
    return warper


@errorcatch
def connector_factory(filepath):
    if filepath.endswith("json"):
        connector = JsonConnector
    elif filepath.endswith("xml"):
        connector = XmlConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

if __name__ == '__main__':
    #######不同对象
    # a = A()
    # b = A()
    # print(id(a)==id(b))
    #######
    js_factory = connector_factory("/home/zhangll/github/pythondesignmodel/1.创建型模式/a,生产者模型/data/other.js")
    xml_factory = connector_factory("/home/zhangll/github/pythondesignmodel/1.创建型模式/a,生产者模型/data/person.xml")
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//person[lastName='{}']".format('Liar')) 
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({}):'.format(p.attrib['type']),
        p.text) for p in liar.find('phoneNumbers')]

    ## 当我们新增一个数据库链接的时候比如mysql,我们操作就变得相对简单合理