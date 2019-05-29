#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: IsPopOrder.py
#     Author: Lina Hu
#     CreatedDate: Wed 22 May 2019 11:19:43 AM CST
#     
#=========================================================
import pdb

def IsPopOrder(pushV, popV):
    # write code here
    if len(pushV)==0 or len(popV)==0:
        return True
    stack = []
    popv = popV[0]
    pop_i = 0
    
    for val in pushV:
        if val != popv:
            stack.append(val)
        elif stack:
            pop_i += 1
            popv = popV[pop_i]

    while(stack):
        if stack.pop() != popV[pop_i]:
            return False
        pop_i += 1
    return True

def main():
    pushV = [1,2,3,4,5]
    popV = [4,5,3,2,1]
    IsPopOrder(pushV, popV) 

if __name__ == '__main__':
    main()
