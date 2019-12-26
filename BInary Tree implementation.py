#!/usr/bin/env python
# coding: utf-8

class Bst:
    class Node:
        def __init__(self, data):
            self.data = data
            self.r_child = None
            self.l_child = None
    def __init__(self):
        self.root = None

    def insert_binary(self,root,child_node):
        if root is None:
            root = child_node            
        else:
            if root.data > child_node.data:
                if root.l_child is None:
                    root.l_child = child_node
                else:
                    self.insert_binary(root.l_child, child_node)
                    
            else:
                if root.r_child is None:
                    root.r_child = child_node
                else:
                    self.insert_binary(root.r_child, child_node)
                    
    
    def in_order_traversal(self, root):
        if not root:
            return 'No root provided'
        self.in_order_traversal(root.l_child)
        print(root.data)
        self.in_order_traversal(root.r_child)
