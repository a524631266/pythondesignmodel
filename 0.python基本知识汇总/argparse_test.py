#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import argparse
    parser = argparse.ArgumentParser()
    # parser.parse_args()
    parser.add_argument("ecooo",help="导出内容")
    parser.add_argument("square",help="显示平方和",type=int)
    parser.add_argument("-v","--verbosity",help="显示冗余    信息",action="store_true") # -v是--versbosity的缩写,同时如果命令行中没有--verbosity就会返回false
    parser.add_argument("-s","--some",choices=[0,1,2],type=int)# -s=1/2/0 --some=1/2/0 指定的参数只能在0-2中选择
    args = parser.parse_args()
    print(args.ecooo)
    print(args.square ** 2)
    print(args.verbosity)
    print(args.some)
    print(args)
    # import argparse
    # parser= argparse.ArgumentParser()
    # parser.add_argument("echo",help="echo the string")
    # args=parser.parse_args()
    # print(args.echo)

if __name__ == '__main__':
    main()

