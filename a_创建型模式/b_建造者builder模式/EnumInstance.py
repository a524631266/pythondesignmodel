from enum import Enum

class A(Enum):
    names = 1
    na = 2
    # def __getitem__(self,key):  实例可以获取A()[key]
    #     return "hellow"[key]
def main():
    print(A.__members__)

if __name__ == '__main__':
    main()