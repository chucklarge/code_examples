require 'BinaryTree'
=begin

        F
      /   \
    B       G
  /   \       \
A      D       I
     /   \    /
    C     E  H

=end


a = BinaryTree.new('A')
b = BinaryTree.new('B')
c = BinaryTree.new('C')
d = BinaryTree.new('D')
e = BinaryTree.new('E')
f = BinaryTree.new('F')
g = BinaryTree.new('G')
h = BinaryTree.new('H')
i = BinaryTree.new('I')

f.left  = b
f.right = g
b.left  = a
b.right = d
d.left  = c
d.right = e
g.right = i
i.left  = h


breadthFirstLevel(f)
puts

depthFirstPreOrder(f)
puts

depthFirstInOrder(f)
puts

depthFirstPostOrder(f)
puts
