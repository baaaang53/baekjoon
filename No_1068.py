#트리

def preorder(node) :
    global count
    if node.child == [] : #자식이 없다면
        count +=1
    for child in node.child :
        preorder(tree[child])


class Node :
    def __init__(self):
        self.child = []
    def setChild(self, node) :
        self.child.append(node)
    def removeChild(self, node):
        self.child.remove(node)


N = int(input())
tree = [Node() for _ in range(N)] #노드들이 들어있는 트리 리스트를 만든다.
count = 0
parent = list(map(int, input().split()))

for i in range(N) :
    if parent[i] != -1 :# 루트가 아니라면
        tree[parent[i]].setChild(i)

if N != 1 :
    delnode = int(input())
    if parent[delnode] == -1 : #루트를 지우는 거라면
        count = 0
    else :
        tree[parent[delnode]].removeChild(delnode)
        preorder(tree[parent.index(-1)])
print(count)