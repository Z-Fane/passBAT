"""
对于两棵彼此独立的二叉树A和B，请编写一个高效算法，检查A中是否存在一棵子树与B树的拓扑结构完全相同。

给定两棵二叉树的头结点A和B，请返回一个bool值，代表A中是否存在一棵同构于B的子树。
"""
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_travel(x):
    if x is None:
        return '#'
    s = str(x.val)
    s += pre_travel(x.left)
    s += pre_travel(x.right)
    return s


class IdenticalTree:
    def chkIdentical(self, A, B):
        # write code here
        # 得到前序遍历的字符串
        a = pre_travel(A)
        b = pre_travel(B)
        if b in a:
            return True
        else:
            return False
