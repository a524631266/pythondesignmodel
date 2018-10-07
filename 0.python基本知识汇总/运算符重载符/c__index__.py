from b__setitem__ import Indexer2
class Index3(Indexer2):
    def __index__(self):
        return 12223344444

def main():
    print(oct(Index3()))
    print(hex(Index3()))
    print(bin(Index3()))
    # print(int(Index3()))

if __name__ == '__main__':
    main()