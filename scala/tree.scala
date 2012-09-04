object Tree {
/*
        F
      /   \
    B       G
  /   \       \
A      D       I
     /   \    /
    C     E  H

*/

  def main(args: Array[String]) {
    var a = new BinaryTreeNode("A");
    var b = new BinaryTreeNode("B");
    var c = new BinaryTreeNode("C");
    var d = new BinaryTreeNode("D");
    var e = new BinaryTreeNode("E");
    var f = new BinaryTreeNode("F");
    var g = new BinaryTreeNode("G");
    var h = new BinaryTreeNode("H");
    var i = new BinaryTreeNode("I");

    f.left  = b
    f.right = g
    b.left  = a
    b.right = d
    d.left  = c
    d.right = e
    g.right = i
    i.left  = h

    var t = new BinaryTree(f);
    t.depthFirstInOrderPrint();
    println();
    t.depthFirstPreOrderPrint();
    println();
    t.depthFirstPostOrderPrint();
    println();
    println();
    t.breadthFirstLevelOrderPrint();
  }
}
