from a__getitem__ import Indexer

class Indexer2(Indexer):
    def __setitem__(self,index,value):
        self.data[index] = value
def main():
    ind = Indexer2()
    ind[1:3] = [20,21,22,23,24]
    print(ind.data)
    
if __name__ == '__main__':
    main()

