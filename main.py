import sys
import random
import gcd
import BSTree

#print(gcd.gcd(150,85))

myTree = BSTree.BST()

for i in range(10):
    myTree.add(random.randint(1,100))

myTree.inOrderSearch()
