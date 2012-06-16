class BinaryTree
  attr_reader :value, :right, :left
  attr_writer :right, :left

  def initialize(value)
    @value = value
    @left  = nil
    @right = nil
  end

end

def breadthFirstLevel(tree)
  q = Array.new
  q << tree
  print = Array.new
  level = 0
  currentCount = 1
  c = 0
  while q.length > 0
    t = q.shift
    currentCount -= 1
    print t.value + " "

    if not t.left.nil?
      q << t.left
      c += 1
    end

    if not t.right.nil?
      q << t.right
      c += 1
    end

    if currentCount == 0
      print "\n"
      currentCount = c
      c = 0
    end
  end
end

def depthFirstPreOrder(tree)
  print tree.value + " "
  if not tree.left.nil?
    depthFirstPreOrder(tree.left)
  end
  if not tree.right.nil?
    depthFirstPreOrder(tree.right)
  end
end

def depthFirstInOrder(tree)
  if not tree.left.nil?
    depthFirstInOrder(tree.left)
  end
  print tree.value + " "
  if not tree.right.nil?
    depthFirstInOrder(tree.right)
  end
end

def depthFirstPostOrder(tree)
  if not tree.left.nil?
    depthFirstPostOrder(tree.left)
  end
  if not tree.right.nil?
    depthFirstPostOrder(tree.right)
  end
  print tree.value + " "
end
