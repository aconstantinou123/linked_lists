from node import Node

class CircularLinkedList:
    first = None
    last = None

    def is_empty(self):
        return self.first == None

    def insert_first(self, data):
        new_node = Node()
        new_node.data = data

        if self.is_empty():
            self.last = new_node
        new_node.next = self.first
        self.first = new_node

    def insert_last(self, data):
        new_node = Node()
        new_node.data = data

        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node #next value of last node will point to new node
            self.last = new_node #new node created is last in the list

    def delete_first(self):
        temp = self.first.data
        if self.first.next == None:
            self.last = None
        self.first = self.first.next 
        return temp

    def display_list(self):
        print('List (first --> last)')
        current = self.first
        while current != None:
            current.display_node()
            current = current.next
        print('End')