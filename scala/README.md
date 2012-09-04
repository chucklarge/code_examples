  mkdir classes
  scalac -d classes BinaryTree.scala tree.scala
  scala -classpath classes Tree
