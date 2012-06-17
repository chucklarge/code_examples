from BinaryTree import *

#          F
#        /   \
#      B       G
#    /   \       \
#  A      D       I
#       /   \    /
#      C     E  H

a = BinaryTree('A')
b = BinaryTree('B')
c = BinaryTree('C')
d = BinaryTree('D')
e = BinaryTree('E')
f = BinaryTree('F')
g = BinaryTree('G')
h = BinaryTree('H')
i = BinaryTree('I')

f.left  = b
f.right = g
b.left  = a
b.right = d
d.left  = c
d.right = e
g.right = i
i.left  = h

depthFirstPreOrder(f)
print

depthFirstInOrder(f)
print

depthFirstPostOrder(f)
print
