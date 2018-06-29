''' In link list the elements are inserted and deleted dynamically and that is the major advantage of link list. Earlier in languages like c and c++
we have to specify how many elements we are going to insert and that many elements only we could insert in the list but then link list allowed
elements to be inserted dynamically.'''




a = []                                              #an empty stack is formed inorder to form a link list
class node:                                         # basis of link list if formed with data and whom the data will point
    def __init__(self,data = 0):
        self.data = data
        self.next = 0
        self.prev = 0
class linklist:                                     #current node tells us about the location of our present node
    def __init__(self):
        self.currentnode = node()
    def insert(self,data):
        new = node(data)                            #value of node of data is given to new and now new = 0 where new refers to new node.
        c = self.currentnode
        while c.next != 0:
            c.prev = c
            c = c.next                              #linking prev to c to next c.prev -> c -> c.next
        c.next = new
                                                    #the last value is new which was initially zero
        while c.next != 0:
            c.prev = c
            c = c.next                              #inserting the data in a list
            a.append(c.data)
    def delete(self,data):
        dell = data
        c = self.currentnode
        while c:                                    #loop until c does not exist, i.e triversing through the list
            if c.data == dell:
                a.remove(c.data)
                c.prev = c.next                     #removing the data of c.data and then c.prev = 0 as c.prev = c.next and we know c.next=0
            c.prev = c
            c = c.next                              #incrementing the loop,thus c.prev , c and c.next are linked toghether due to it.
    def display(self):
        print(a)
l = linklist()
while(True):
    ch = int(input("1.insert\n 2.delete\n 3.display\n"))
    if ch == 1:
        data = int(input())
        l.insert(data)
    elif ch == 2:
        data = int(input())
        l.delete(data)
    elif ch == 3:
        l.display()