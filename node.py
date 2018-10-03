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

    def doInOrder(self):
        if self.left : self.left.doInOrder()
        print(self.val)
        if self.right : self.right.doInOrder()

    def doPreOrder(self):
        print(self.val)
        if self.left : self.left.doPreOrder()
        if self.right : self.right.doPreOrder()

    def doPostOrder(self):
        if self.left : self.left.doPostOrder()
        if self.right : self.right.doPostOrder()
        print(self.val)
