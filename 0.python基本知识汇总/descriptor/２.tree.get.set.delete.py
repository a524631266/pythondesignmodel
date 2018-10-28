# __getattribute__

# __get__ __set__ __delete__

class Desc:
    def __get__(self,instance,owner):
        print("__get__")

