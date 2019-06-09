#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: 01-bag.py
#     Author: Lina Hu
#     CreatedDate: Thu 23 May 2019 05:38:38 PM CST
#     
#=========================================================
import pdb

def bag(n, c, w, v):
    res = [[-1 for j in range(c+1)] for i in range(n+1)]
    for j in range(c+1):
        res[0][j] = 0

    for i in range(n+1):
        res[i][0] = 0
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            res[i][j] = res[i-1][j]
            if j > w[i-1] and res[i][j] < res[][]

    return res

def show(n, c, w, res):
    

def main():
    n = 5
    c = 10
    w = [2,2,6,5,4]
    v = [6,3,5,4,6]
    bag(n, c, w, v)

if __name__ == '__main__':
    main()

