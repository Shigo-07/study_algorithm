class Node(object):
    def __ini__(self,value:int) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node,value: int) -> Node:
    if node is None:
        return Node(value)

if __name__ == "__main__":
    root = None
    root = insert(root,3)