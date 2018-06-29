class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
def insert(root,node):
    if root == None:
        root = node
    else:
        if node.data < root.data:
            if root.left == None:
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert(root.right,node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
r = node(10)
insert(r,node(20))
insert(r,node(30))
print("\n")
print("\n")
print("inorder\n")
inorder(r)
print(" \n")
print("\n")
print("preorder\n")
preorder(r)
print("\n")
print("\n")
print("postorder\n")
postorder(r)