class node:                                             #basic structure of binary search tree
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
class tree:
    def __init__(self):
        self.root = None                                #initially root node is set to none
    def insert(self,data):
        if self.root == None:                           #normal insertion is done here i.e only at level 1
            self.root = node(data)
        else:
            self._insert(self.root,data)                #calling the private function
    def _insert(self,current,data):                     #all the recursive insertion is done in this function
        if data < current.data:
            if current.left == None:
                current.left = node(data)
            else:
                self._insert(current.left,data)         #recursive loop calling the private function
        else:
            if current.right == None:
                current.right = node(data)
            else:
                self._insert(current.right,data)
    def display(self):                                  #display the first root element
        if self.root != None:
            self._display(self.root)
    def _display(self,current):                         #display recursive elements in the loop
        if current.data != None:
            if current.left != None:
                self._display(current.left)
            print(current.data)
            if current.right != None:
                self._display(current.right)
t = tree()
t.display()
t.insert(10)
t.insert(20)
t.insert(30)
t.insert(5)
t.insert(15)
t.display()

