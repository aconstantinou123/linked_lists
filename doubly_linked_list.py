from node import Node

class DoublyLinkedList:
    first = None
    last = None

    def is_empty(self):
        return self.first == None

    def display_list(self):
        print('List (first --> last)')
        current = self.first
        while current != None:
            current.display_node()
            current = current.next
        print('End')

    def insert_first(self, data):
        new_node = Node()
        new_node.data = data
        if self.is_empty():
            self.last = new_node
        else:
            self.first.previous = new_node
        new_node.next = self.first
        self.first = new_node

    def insert_last(self, data):
        new_node = Node()
        new_node.data = data
        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node
            new_node.previous = self.last
        self.last = new_node

    #assume non-empty list
    def delete_first(self):
        temp = self.first
        if self.first.next == None:
            self.last = None
        else:
            self.first.next.previous = None
        self.first = self.first.next
        return temp

    #assume non-empty list
    def delete_last(self):
        temp = self.last
        if self.first.next == None:
            self.first = None
        else:
            self.last.previous.next = None
        self.last = self.last.previous
        return temp

    #assume non-empty list
    def insert_after(self, key, data):
        current = self.first
        while current.data != key:
            current = current.next
            if current == None:
                return False
        new_node = Node()
        new_node.data = data
        if current == self.last:
            current.next = None
            self.last = new_node
        else:
            new_node.next = current.next
            current.next.previous = new_node
        new_node.previous = current
        current.next = new_node
        return True

    #assume non-empty list
    def delete_key(self, key):
        current = self.first
        while current.data != key:
            current = current.next
            if current == None:
                return None
        if self.first == current:
            self.first = current.next
        else:
            current.previous.next = current.next
        if self.last == current:
            self.last = current.previous
        else:
            current.next.previous = current.previous    
        return current

        
