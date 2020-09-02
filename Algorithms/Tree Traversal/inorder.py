class Node:
    def __init__(self,val):
        self.childLeft = None
        self.childRight = None
        self.nodedata = val

## Creating an instance of the Node class to construct a tree
root = Node(1)
root.childLeft = Node(2)
root.childRight = Node(3)
root.childLeft.childLeft = Node(4)
root.childLeft.childRight = Node(5)

## PreOrder Traversal algorithm
print("PreOrder Traversal")
def PreOrder(root):
    if(root):
        print(root.nodedata)
        PreOrder(root.childLeft)
        PreOrder(root.childRight)
PreOrder(root)

## Inorder Traversal algorithm
print("Inorder Traversal")
def InOrder(root):
    if(root):
        InOrder(root.childLeft)
        print(root.nodedata)
        InOrder(root.childRight)
InOrder(root)

## PostOrder Traversal algorithm
print("PostOrder Traversal")
def PostOrder(root):
    if(root):
        print(root.nodedata)
        PostOrder(root.childRight)
        PostOrder(root.childLeft)
PostOrder(root)