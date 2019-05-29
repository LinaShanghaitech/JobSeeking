#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: BinaryTree.py
#     Author: Lina Hu
#     CreatedDate: Thu 23 May 2019 10:26:45 AM CST
#     
#=========================================================
import pdb


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#Traverse Recursive Methods
def preTraverse(root, plist):
    if root is None: return
#    print(root.val)
    if root.left is None and root.right is None:
        plist.append(root.val)
    preTraverse(root.left, plist)
    preTraverse(root.right, plist)

def midTraverse(root, plist):
    if root is None: return
    midTraverse(root.left, plist)
    plist.append(root.val)
    midTraverse(root.right, plist)

def afterTraverse(root, plist):
    if root is None: return
    afterTraverse(root.left, plist)
    afterTraverse(root.right, plist)
    plist.append(root.val)


def main():
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', None, Node('G', Node('F'))))
    plist = []
    preTraverse(root, plist)
    print(plist)
    plist = []
    midTraverse(root, plist)
    print(plist)
    plist = []
    afterTraverse(root, plist)
    print(plist)

    
if __name__ == '__main__':
    main()
