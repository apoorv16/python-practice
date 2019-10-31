class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def front(self,data):
        front_node = node(data)
        front_node.next = self.head
        self.head = front_node

    def middle(self,data,prev_node):
        c = self.head
        while c.data != prev_node:
            c = c.next
        middle_node = node(data)
        middle_node.next = c.next
        c.next = middle_node

    def back(self,data):
        if self.head == None:
            self.head = node(data)
        else:
            self._back(self.head,data)
    def _back(self,c,data):
        if c.next is not None:
            self._back(c.next,data)
        else:
            c.next = node(data)

    def display(self):
        if self.head is None:
            print("No Linkedlist")
        else:
            self._display(self.head)
    def _display(self,c):
        if c is not None:
            print(c.data,c.next)
            self._display(c.next)

    def delete(self,data):
        c = self.head
        while c.next.data != data:
            c = c.next
        c.next = c.next.next

if __name__ == '__main__':
    l = linkedlist()
    l.back(10)
    l.back(20)
    l.back(30)
    l.front(5)
    l.middle(15,10)
    l.delete(15)
    l.display()
