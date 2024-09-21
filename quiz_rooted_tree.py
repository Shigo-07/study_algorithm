# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/7/ALDS1_7_A

import io
import sys
_INPUT = """\
13
0 3 1 4 10
1 2 2 3
2 0
3 0
4 3 5 6 7
5 0
6 0
7 2 8 9
8 0
9 0
10 2 11 12
11 0
12 0
"""
sys.stdin = io.StringIO(_INPUT)

class Node:
    def __init__(self):
        self.parent = -1
        self.children = []
        self.depth = None
        self.kind = None
N = int(input())
Tree = [Node() for _ in range(N)]

def set_depth(node:Node) -> None:

    def _set_depth(node:Node,depth: int) -> None:
        node.depth = depth
        for child in node.children:
            _set_depth(Tree[child],depth+1)

    _set_depth(node,0)


for _ in range(N):
    node_info = list(map(int,input().split()))
    index = node_info[0]
    childs = node_info[1]

    if childs > 0:
        Tree[index].children = node_info[2:]
        
    for child_index in Tree[index].children:
        Tree[child_index].parent = index
    
root_index = [i for i,n in enumerate(Tree) if n.parent == -1][0]
set_depth(Tree[root_index])

for i,node in enumerate(Tree):
    if node.parent == -1:
        node.kind = "root"
    elif node.parent != -1 and len(node.children) == 0:
        node.kind = "leaf"
    else:
        node.kind = "internal node"
    
    print(f"node {i}: parent = {node.parent}, depth = {node.depth}, {node.kind}, {node.children}")