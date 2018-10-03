import sys
import random
import gcd
import BSTree

#print(gcd.gcd(150,85))

myTree = BSTree.BST()

nums = []
for i in range(10):
    num = random.randint(1,100)
    nums.append(num)
    myTree.add(num)

print(nums)

myTree.preOrderSearch()
print("-----------------------------")
myTree.inOrderSearch()
print("-----------------------------")
myTree.postOrderSearch()
