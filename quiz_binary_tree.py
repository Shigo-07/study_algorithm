# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/7/ALDS1_7_B
import io
import sys
_INPUT = """\
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""
sys.stdin = io.StringIO(_INPUT)
 
class Node:
    def __init__(self):
        self.parent = -1
        self.left = None
        self.right = None

def set_depth(node:Node) -> None:

    def _set_depth(node:Node,depth:int) -> None:
        node.depth = depth
        if node.left != -1:
            _set_depth(Tree[node.left],depth + 1)
        if node.right != -1:
            _set_depth(Tree[node.right],depth + 1)

    _set_depth(node,0)

def set_height(node:Node) -> None:
    left_h = 0
    right_h = 0
    if node.left != -1:
        left_h = set_height(Tree[node.left]) + 1
    if node.right != -1:
        right_h = set_height(Tree[node.right]) + 1
    max_h = max(left_h,right_h)
    node.height = max_h
    return max_h

def cal_sibling(index:int) -> int:
    node = Tree[index]
    if node.parent == -1:
        return -1
    parent_node = Tree[node.parent]
    if index != parent_node.left:
        return parent_node.left
    if index != parent_node.right:
        return parent_node.right

def cal_kind(node:Node) -> str:
    if node.parent == -1:
        return "root"
    elif node.left == -1 and node.right == -1:
        return "leaf"
    else:
        return "internal node"
    
def cal_degree(node:Node)->int:
    count = 0
    if node.left != -1:
        count += 1
    if node.right != -1:
        count += 1
    return count


N = int(input())
Tree = [Node() for _ in range(N)]

for _ in range(N):
    node_info = map(int,input().split())
    node_index,node_left,node_right = node_info
    
    Tree[node_index].left,Tree[node_index].right = node_left,node_right
    
    # 親ノードを定義
    if node_left != -1:
        Tree[node_left].parent = node_index
    if node_right != -1:
        Tree[node_right].parent = node_index

root_index = [i for i,n in enumerate(Tree) if n.parent == -1][0]
set_depth(Tree[root_index])
set_height(Tree[root_index])

for i,node in enumerate(Tree):
    print(f"node {i}: parent = {node.parent}, sibling = {cal_sibling(i)}, degree = {cal_degree(node)}, depth = {node.depth}, height = {node.height}, {cal_kind(node)}")