class Node:
    data = None
    next = None
    previous = None

    def display_node(self):
        print(f'( {self.data} )')