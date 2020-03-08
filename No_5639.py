#이진 검색 트리

import sys

class Node :
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

class BST :
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root == None :
            self.root = Node(key)
        else :
            current = self.root
            while True :
                if current.key > key : #왼쪽으로 탐색해야 함.
                    if current.lchild == None :
                        current.lchild = Node(key)
                        break
                    current = current.lchild
                if current.key < key : #오른쪽으로 탐색해야 함
                    if current.rchild == None : # 자리를 찾음
                        current.rchild = Node(key)
                        break
                    current = current.rchild #계속해서 타고 내려가기

    def postorder(self,root):
        stack = []
        while True :
            while root :
                if root.rchild :
                    stack.append(root.rchild)
                stack.append(root)
                root = root.lchild
            root = stack.pop()

            if root.rchild and (stack[-1] if len(stack) else None) == root.rchild :
                stack.pop()
                stack.append(root)
                root = root.rchild
            else :
                print(root.key)
                root = None
            if not stack :
                break

bst = BST()

while True :
    try :
        num = int(sys.stdin.readline())
        bst.insert(num)
    except :
        break

bst.postorder(bst.root)
