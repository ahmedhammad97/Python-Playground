class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def addChild(self, x):
        if x.val < self.val:
            if self.left is None:
                self.left = x
            else:
                self.left.addChild(x)
        else:
            if self.right is None:
                self.right = x
            else:
                self.right.addChild(x)

    def doSearch(self):
        if self.left : self.left.doSearch()
        print(self.val)
        if self.right : self.right.doSearch()
