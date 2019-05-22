#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: 2-dim-array-search.py
#     Author: Lina Hu
#     CreatedDate: Wed 22 May 2019 11:19:43 AM CST
#     
#=========================================================
import pdb


def search(arr, val):
    cols, rows = len(arr), len(arr[0])
    pdb.set_trace()    
    x = 0
    y = cols-1
    while(y>=0 and x<=rows-1):
        cur = arr[y][x]
        if val < cur:
            y -= 1    
        elif val > cur:
            x += 1
        else:
            return x, y

    return -1, -1

def main():
    target = 15
    arr = [[1,2,3],[4,5,6],[7,8,9],[10,12,13]]
    val = 2
    print(arr, val)
    x, y = search(arr, val)
    print(x, y)


if __name__ == '__main__':
    main()
