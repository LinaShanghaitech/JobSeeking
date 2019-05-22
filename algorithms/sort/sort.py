#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: sort.py
#     Author: Lina Hu
#     CreatedDate: Wed 22 May 2019 06:31:21 AM CST
#     
#=========================================================

import random
import pdb
# BubbleSort
def bubble_sort(arr, flag=1):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(0, n-i-1):
            if flag > 0:
                idx1, idx2 = j, j+1
            else:
                idx2, idx1 = j, j+1
            if arr[idx1] > arr[idx2]:
                b = arr[idx1]
                arr[idx1] = arr[idx2]
                arr[idx2] = b
                is_sorted = False
        if is_sorted:
            return arr
    return arr

# SelectionSort
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        max_v = arr[0]
        max_idx = 0
        for j in range(1, n-i):
            if max_v < arr[j]:
                max_idx = j
                max_v = arr[j]
        arr[max_idx], arr[n-i-1] = arr[n-i-1], arr[max_idx]

    return arr

# InsertionSort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_v = arr[i]
        insert_idx = i
        for j in range(i,-1,-1):
#            pdb.set_trace()
            if insert_v <= arr[j]:
                insert_idx = j
            else:
                break
        if insert_idx < i:
            arr[insert_idx+1:i+1] = arr[insert_idx:i]
            arr[insert_idx] = insert_v

    return arr 

# ShellSort

# MergeSort
def merge(arr1, arr2):
    idx1, idx2 = 0,0
    arr = []
    while 1:
        if arr1[idx1] < arr2[idx2]:
            arr.append(arr1[idx1])
            idx1 += 1
        else:
            arr.append(arr2[idx2])
            idx2 += 1
        if idx1 == len(arr1):
            arr.extend(arr2[idx2:])
            return arr
        elif idx2 == len(arr2):
            arr.extend(arr1[idx1:])
            return arr

def merge_sort(arr):
    if len(arr) <= 1: return arr
    num = int(len(arr)/2) 
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)


#QuickSort

def q_sort(arr, start, end):
    if start >= end: return arr
    pivot = Partition(arr, start, end)
    q_sort(arr, start, pivot-1)
    q_sort(arr, pivot+1, end)
    return arr

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

def quick_sort(arr):
    return q_sort(arr, 0, len(arr)-1)

#HeapSort

def heap_sort(arr):
    return arr



def main():
#    flag = int(input())
    arr = [20,4,5,7,9,3,2,12,4]
#    arr = bubble_sort(arr, flag)
#    arr = selection_sort(arr)
#    arr = insertion_sort(arr)
#    arr = merge_sort(arr)
    arr = quick_sort(arr)
    print(arr)
    
if __name__ == '__main__':
    main()

