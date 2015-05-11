#!/usr/bin/env python

from stack import Stack
from binarytree import BinaryTree

def build_newick_tree(string):
    string = string.replace(' ','')
    tstack = Stack()
    tree = BinaryTree('')
    tstack.push(tree)
    current_tree = tree

    for char in string:
        if char == '(':
            current_tree.insert_left('')
            tstack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif char == ')':
            current_tree = tstack.pop()
        elif char == ',':
            current_tree = tstack.pop()
            current_tree.insert_right('')
            tstack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif char == ';':
            pass
        else:
            current_tree.set_name(char)
