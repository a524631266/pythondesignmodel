class Computer(object):
    def __init__(self,name):
        self.name = name
    
    def execute(self):
        print("computer calling")

class Human(object):
    def __init__(self,name):
        self.name = name
    
    def say(self):
        print("human calling")
class Animal(object):
    def __init__(self,name):
        self.name = name
    def play(self):
        print("animal   playpaly")

class Adapter(object):
    def __init__(self,obj,object_method):
        """
            the object_method must be the dict object
            the key of this dict must be the adaptername of this adapter
            that every one should only know the adapter api ,so that it 
            can easy to use and understand for anyone else.
        """
        self.obj = obj
        self.__dict__.update(object_method)
    
    # def execute(self):
    #     print()


def main():
    objects = []
    computer = Computer("computer name 1")
    human = Human("human name1")
    animal = Animal("animal name1")
    objects.append(computer)
    huamadapter = Adapter(human,{"execute":human.say,"name":human.name})
    animaldapter = Adapter(animal,{"execute":animal.play,"name":animal.name})
    objects.append(huamadapter)
    objects.append(animaldapter)
    for i in objects:
        print("execute the function / or method :::::::{}".format(i.execute()))
        print("name is ::::  {} ".format(i.name))

if __name__ == '__main__':
    main()