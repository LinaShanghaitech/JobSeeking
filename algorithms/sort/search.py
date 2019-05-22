#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: search.py
#     Author: Lina Hu
#     CreatedDate: Wed 22 May 2019 10:50:06 AM CST
#     
#=========================================================

#Sequential Search
def seq_search(arr, val):
    num = len(arr)
    for i in range(num):
        if arr[i] == val:
            return i
    return -1


# Binary Search
def binary_search(arr, val):
    num = len(arr)
    l = 0
    r = num-1
    n_search = 0
    while(l<=r):
        mid = int((l+r)/2)
        n_search += 1
        if arr[mid] < val:
            l = mid+1
        elif arr[mid] > val:
            r = mid-1
        else:
            print('search times:{}'.format(n_search))
            return mid
    print('search times:{}'.format(n_search))
    return -1



def main():
    arr = [20,4,5,7,9,3,2,12,4]
    arr.sort()
    print(arr)
    val = int(input('input search value:'))
    idx = seq_search(arr, val) 
    print(idx)
    idx = binary_search(arr, val) 
    print(idx)
if __name__ == '__main__':
    main()


