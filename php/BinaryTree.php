<?php


class BinaryTreeNode {
    public $value  = null;
    public $left   = null;  // left pointer
    public $right  = null;  // right pointer

    public function __construct($value=null) {
        $this->value = $value;
    }
}


class BinaryTree {
    protected $head;

    public function __construct() {
    }

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
        $treeArray = array_slice($treeArray, strlen($value)+1);      // +1 for space between value and left

        $left = $this->getBranch($treeArray);
        $treeArray = array_slice($treeArray, strlen($left)+1);       // +1 for space between left and right

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
}
