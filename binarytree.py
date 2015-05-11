#!/usr/bin/env python

class BinaryTree:
    def __init__(self, root):
        self.name = root
        self.left_child = None
        self.right_child = None
        self.val_dict = {}

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def check_val(self,k):
        return k in self.val_dict.keys()

    def get_val(self,k):
        return self.val_dict[k]

    def add_val(self,k,v):
        self.val_dict[k] = v

    def set_name(self, name):
        self.name = name

    #def get_rootval(self):
    #    return self.key

