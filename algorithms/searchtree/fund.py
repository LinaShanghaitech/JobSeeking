#coding=utf-8
#=========================================================
#     Copyright (C) 2019 Shanghaitech SVIP Lab. All rights reserved.
#     
#     ScriptName: fund.py
#     Author: Lina Hu
#     CreatedDate: Wed 29 May 2019 01:12:54 PM CST
#     
#=========================================================

class BinarySearchTree:
    def __init__(self):
        self.count = 0
        self.root = None

    def count(self):
        return self.count

    def insert(self, key, value):
        if (self.count == 0):
            self.root = Node(key, value)
            self.count = self.count + 1
            return
        else:
            node = self.root
            while True:
                if (node.key > key)
                    if (node.lnode == None):
                        node.lnode = Node(key, value)
                    else:
                        node = node.lnode
                elif (node.key < key):
                    if (node.rnode == None):
                        node.rnode = Node(key, value)
                    else:
                        node = node.rnode

    def contains(self, node, key):
        return _contains(self, node, key)
    
    def _contains(self, node, key):
        if (node == None):
            return False
        if (node.key > key):
            return self._contains(node.lnode, key)
        elif (node.key < key):
            return self._contains(node.rnode, key)
        else:
            return True
    





