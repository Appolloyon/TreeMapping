#!/usr/bin/env python

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        if not tree.get_left_child() and not tree.get_right_child():
            pass
        else:
            try:
                tl = tree.get_left_child()
                tr = tree.get_right_child()
            except:
                pass
            for val in tree.get_rootval():
                if tl.get_rootval() or tr.get_rootval():
                    tree.set_rootval()
