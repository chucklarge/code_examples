import scala.collection.mutable.Queue

class BinaryTreeNode(v: String) {
  var value: String = v;
  var left:  BinaryTreeNode = null;
  var right: BinaryTreeNode = null;
}

class BinaryTree(h: BinaryTreeNode) {
  var head: BinaryTreeNode = h;

  def breadthFirstLevelOrderPrint(tree: BinaryTreeNode = head) {
    var q = new Queue[BinaryTreeNode];
    q.enqueue(tree);
    var currentCount: Int = 1;
    var c: Int = 0;
    while (q.length > 0) {
      var node: BinaryTreeNode = q.dequeue;
      currentCount -= 1;
      print(node.value + " ");

      if (node.left != null) {
        q.enqueue(node.left);
        c += 1;
      }
      if (node.right != null) {
        q.enqueue(node.right);
        c += 1;
      }

      if (currentCount == 0) {
        println;
        currentCount = c;
        c = 0;
      }
    }
  }

  def depthFirstPreOrderPrint(tree: BinaryTreeNode = head) {
    print(tree.value + " ");
    if (tree.left != null) {
      depthFirstPreOrderPrint(tree.left);
    }
    if (tree.right != null) {
      depthFirstPreOrderPrint(tree.right);
    }
  }

  def depthFirstInOrderPrint(tree: BinaryTreeNode = head) {
    if (tree.left != null) {
      depthFirstInOrderPrint(tree.left);
    }
    print(tree.value + " ");
    if (tree.right != null) {
      depthFirstInOrderPrint(tree.right);
    }
  }

  def depthFirstPostOrderPrint(tree: BinaryTreeNode = head) {
    if (tree.left != null) {
      depthFirstPostOrderPrint(tree.left);
    }
    if (tree.right != null) {
      depthFirstPostOrderPrint(tree.right);
    }
    print(tree.value + " ");
  }
}
