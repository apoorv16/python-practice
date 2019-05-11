''' In link list the elements are inserted and deleted dynamically and that is the major advantage of link list. Earlier in languages like c and c++
we have to specify how many elements we are going to insert and that many elements only we could insert in the list but then link list allowed
elements to be inserted dynamically.'''



                   
class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class ll:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new = node(data)
        if self.head == None:
            self.head = node(data)
        else:
            c = self.head
            while c.next != None:
                c = c.next
            c.next = new

    def display(self):
        c = self.head
        while c.next != None:
            print(c.data, c.next.data)
            c = c.next
l = ll()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(None)
