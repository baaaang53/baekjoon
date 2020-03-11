#트리

import sys

tc = int(input())

class Node :
    def __init__(self):
        self.lchild = 0
        self.rchild = 0



for _ in range(tc):
    node = int(sys.stdin.readline())
    tree = [Node() for _ in range(node)]
    root = 0
    preorder = map(int, sys.stdin.readline().split())
    inorder = map(int, sys.stdin.readline().split())
    root = preorder[0]

