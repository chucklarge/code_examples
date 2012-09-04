<?php
class BinaryTreeNode {
    public $value  = null;
    public $left   = null;
    public $right  = null;

    public function __construct($value=null) {
        $this->value = $value;
    }
}

class BinaryTree {
    protected $head;

    public function __construct($treeString=null) {
        if ($treeString) {
            $this->head = $this->createTree($treeString);
        }
    }

    /*
     * Grammar for Binary Trees
     * :tree -> (v :tree :tree) | ()
     */
    public function createTree($treeString) {
        $node = null;
        if ($treeString !== '()') {
            $components = $this->getComponents($treeString);
            $node = new BinaryTreeNode($components['value']);
            if ($components['left'] !== '()') {
                $node->left  = $this->createTree($components['left']);
            }
            if ($components['right'] !== '()') {
                $node->right = $this->createTree($components['right']);
            }
        }
        return $node;
    }

    public function getComponents($treeString) {
        $rawTree = substr($treeString, 1, strlen($treeString) - 2);  // strip the outer ( and )
        $treeArray = str_split($rawTree);
        $value = $this->getValue($treeArray);

        $treeArray = array_slice($treeArray, strlen($value)+1); // +1 for the space
        $left = $this->getBranch($treeArray);

        $treeArray = array_slice($treeArray, strlen($left));   // +1 for the space
        $right = $this->getBranch($treeArray);

        $components = array();
        $components['value'] = $value;
        $components['left']  = $left;
        $components['right'] = $right;

        return $components;
    }

    protected function getValue($treeArray) {
        $str = '';
        foreach ($treeArray as $index => $letter) {
            if ($letter === ' ') {
                break;
            }
            $str .= $letter;
        }
        return trim($str);
    }

    protected function getBranch($treeArray) {
        $str = '';
        $stack = array();
        foreach ($treeArray as $index => $letter) {
            $str .= $letter;
            if ($letter === '(') {
                $stack[] = '(';
            }
            else if ($letter === ')') {
                array_shift($stack); // pop
                if (!count($stack)) {
                    break;
                }
            }
        }
        return trim($str);
    }

    public function checkSyntax($treeString) {
        $treeArray = str_split($treeString);
        $stack = array();
        $success = false;
        $str = '';
        foreach ($treeArray as $index => $letter) {
            if ($letter === '(') {
                if ($str !== '') {
                    $stack[] = $str;
                    $str = '';
                }
                $stack[] = $letter;
            }
            else if ($letter === ')') {
                if ($str !== '') {
                    $stack[] = $str;
                    $str = '';
                }
                //$item = array_shift($stack);
                //if ($item !== '(') {
                    //break;
                //}
                $stack[] = $letter;
            }
            else if ($letter === ' ') {
                if ($str !== '') {
                    $stack[] = $str;
                    $str = '';
                }
            }
            else {
                $str .= $letter;
            }
        }
        //if (empty($stack)) {
           //$success = true;
        //}
        //var_dump($stack);
        return $success;
    }

    public function checkParenCount($treeString) {
        $left_paren_count = substr_count($treeString, '(');
        $right_paren_count = substr_count($treeString, ')');
        return $left_paren_count === $right_paren_count;
    }

    public function breadthFirst() {
        return trim($this->_breadthFirst($this->head));
    }

    public function breadthFirstLevel() {
        return trim($this->_breadthFirstLevel($this->head));
    }

    public function depthFirstPreOrder() {
        return trim($this->_depthFirstPreOrder($this->head));
    }

    public function depthFirstInOrder() {
        return trim($this->_depthFirstInOrder($this->head));
    }

    public function depthFirstPostOrder() {
        return trim($this->_depthFirstPostOrder($this->head));
    }


    // Breadth First
     protected function _breadthFirst(BinaryTreeNode $tree) {
        $return = '';
        $q = array();
        $q[] = $tree;
        while (!empty($q)) {
            $t = array_shift($q);
            $return .= $t->value . " ";

            $o = $t->left;
            if ($o != null) {
                $q[] = $o;
            }

            $o = $t->right;
            if ($o != null) {
                $q[] = $o;
            }
        }
        return $return;
    }

     protected function _breadthFirstLevel(BinaryTreeNode $tree) {
        $return = '';
        $q = array();
        $q[] = $tree;
        $level = 0;
        $currentCount = 1;
        $c = 0;
        while (!empty($q)) {
            $t = array_shift($q);
            $currentCount--;
            $return .= $t->value . " ";

            $o = $t->left;
            if ($o != null) {
                $q[] = $o;
                $c++;
            }

            $o = $t->right;
            if ($o != null) {
                $q[] = $o;
                $c++;
            }

            if ($currentCount == 0) {
                $return .= "\n";
                $currentCount = $c;
                $c = 0;
            }
        }
        return $return;
    }

    // Depth First
    //   Recursive
     protected function _depthFirstPreOrder(BinaryTreeNode $tree) {
        $return = $tree->value . " ";
        if ($tree->left) {
            $return .= $this->_depthFirstPreOrder($tree->left);
        }
        if ($tree->right) {
            $return .= $this->_depthFirstPreOrder($tree->right);
        }
        return $return;
    }

     protected function _depthFirstInOrder(BinaryTreeNode $tree) {
        $return = '';
        if ($tree->left) {
            $return .= $this->_depthFirstInOrder($tree->left);
        }
        $return .= $tree->value . " ";
        if ($tree->right) {
            $return .= $this->_depthFirstInOrder($tree->right);
        }
        return $return;
    }

     protected function _depthFirstPostOrder(BinaryTreeNode $tree) {
        $return = '';
        if ($tree->left) {
            $return .= $this->_depthFirstPostOrder($tree->left);
        }
        if ($tree->right) {
            $return .= $this->_depthFirstPostOrder($tree->right);
        }
        $return .= $tree->value . " ";
        return $return;
    }

     protected function treeHeight(BinaryTreeNode $tree=null) {
        if ($tree == null) {
            return 0;
        }
       return max($this->treeHeight($tree->left), $this->treeHeight($tree->right)) + 1;
    }
}
