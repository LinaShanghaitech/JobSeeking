#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: template.py
#     Author: Lina Hu
#     CreatedDate: Wed 22 May 2019 11:19:43 AM CST
#     
#=========================================================

import pdb

def getleastnumbers(arr, k):
#    pdb.set_trace()
    if arr is None:
        return None
    Find_k(arr, 0, len(arr)-1, k)
    return arr[:k]

def Partition(arr, l, r):
    pivotkey = arr[l]
    while(l<r):
        while(arr[r] >= pivotkey and l < r):
            r -= 1
        arr[l] = arr[r]
        while(arr[l] <= pivotkey and l < r):
            l += 1
        arr[r] = arr[l]
    arr[l] = pivotkey
    return l        
    

def Find_k(arr, left, right, k):
    pivot = Partition(arr, left, right)
#    print(arr, pivot)
    if pivot < k-1:
        Find_k(arr, pivot+1, right, k)
    elif pivot > k-1:
        Find_k(arr, left, pivot-1, k)
    else:
        return 
    
        



def main():
    arr = [4,5,1,6,2,7,3,8]
    topk = 3
    print(arr, topk)
    leastlist = getleastnumbers(arr, topk)
    print(leastlist)

if __name__ == '__main__':
    main()
