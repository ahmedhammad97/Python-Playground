import sys
from node import Node

class BST:
    def __init__(self):
        self.root = None

    def add(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self.root.addChild(Node(x))

    def inOrderSearch(self):
        if not self.root:
            print("Empty Tree")
        else:
            self.root.doSearch()
