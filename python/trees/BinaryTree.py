import sys

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left  = None
    self.right = None

def depthFirstPreOrder(tree):
  sys.stdout.write(tree.value + ' ')

  if tree.left is not None:
    depthFirstPreOrder(tree.left)

  if tree.right is not None:
    depthFirstPreOrder(tree.right)

def depthFirstInOrder(tree):
  if tree.left is not None:
    depthFirstInOrder(tree.left)

  sys.stdout.write(tree.value + ' ')

  if tree.right is not None:
    depthFirstInOrder(tree.right)

def depthFirstPostOrder(tree):
  if tree.left is not None:
    depthFirstPostOrder(tree.left)

  if tree.right is not None:
    depthFirstPostOrder(tree.right)
  sys.stdout.write(tree.value + ' ')
