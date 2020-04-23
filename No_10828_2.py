#스택
import sys

stack = []
def push(X) :
    stack.append(X)

def pop() :
    if len(stack) == 0 :
        print(-1)
    else :
        k = stack.pop(-1)
        print(k)

def size() :
    print(len(stack))

def empty() :
    if (len(stack) == 0) :
        print(1)
    else :
        print(0)

def top() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack[len(stack)-1])


N = int(input())

for _ in range(N) :
    inp = sys.stdin.readline().split()
    if inp[0] == "push" :
        push(inp[1])

    elif inp[0] == "top" :
        top()

    elif inp[0] == "size" :
        size()

    elif inp[0] == "empty" :
        empty()

    elif inp[0] == "pop" :
        pop()