<?php
require_once './BinaryTree.php';

/**
 * Test suite for the BinaryTree class.
 */
class BinaryTreeTest extends PHPUnit_Framework_TestCase {

/*

           AA


           AA
         /
       BB

           AA
              \
               CC

           AA
         /    \
       BB      CC

           AA
         /    \
       BB      CC
     /       /    \
   II      DD      JJ

            F
          /   \
        B       G
      /   \       \
    A      D       I
         /   \    /
        C     E  H

*/
    protected $tree1 = '(AA () ())',
              $tree2 = '(AA (BB () ()) ())',
              $tree3 = '(AA () (CC () ()))',
              $tree4 = '(AA (BB () ()) (CC () ()))',
              $tree5 = '(AA (BB () (II () ())) (CC (DD () ()) (JJ () ())))',
              $tree6 = '(F (B (A () ()) (D (C () ()) (E () ()))) (G () (I (H () ()) ())))';

    protected function setUp() {
    }

    /**
     * @dataProvider componentProvider
     */
    public function testGetComponents($treeString, $value, $left, $right) {
        $bt = new BinaryTree();
        $components = $bt->getComponents($treeString);
        $this->assertEquals($value, $components['value']);
        $this->assertEquals($left,  $components['left']);
        $this->assertEquals($right, $components['right']);
    }

    /**
     * @dataProvider preOrderProvider
     */
    public function testPreOrder($treeString, $expected) {
        $tree = new BinaryTree($treeString);
        $actual = $tree->depthFirstPreOrder();
        $this->assertEquals($expected, $actual);
    }

    /**
     * @dataProvider inOrderProvider
     */
    public function testInOrder($treeString, $expected) {
        $tree = new BinaryTree($treeString);
        $actual = $tree->depthFirstInOrder();
        $this->assertEquals($expected, $actual);
    }

    /**
     * @dataProvider postOrderProvider
     */
    public function testPostOrder($treeString, $expected) {
        $tree = new BinaryTree($treeString);
        $actual = $tree->depthFirstPostOrder();
        $this->assertEquals($expected, $actual);
    }

    // Data Providers
    public function componentProvider() {
        return array(
            array($this->tree1, 'AA', '()',                                    '()'),
            array($this->tree2, 'AA', '(BB () ())',                            '()'),
            array($this->tree3, 'AA', '()',                                    '(CC () ())'),
            array($this->tree4, 'AA', '(BB () ())',                            '(CC () ())'),
            array($this->tree5, 'AA', '(BB () (II () ()))',                    '(CC (DD () ()) (JJ () ()))'),
            array($this->tree6, 'F',  '(B (A () ()) (D (C () ()) (E () ())))', '(G () (I (H () ()) ()))'),
        );
    }

    public function preOrderProvider() {
        return array(
            array($this->tree1, 'AA'),
            array($this->tree2, 'AA BB'),
            array($this->tree3, 'AA CC'),
            array($this->tree4, 'AA BB CC'),
            array($this->tree5, 'AA BB II CC DD JJ'),
            array($this->tree6, 'F B A D C E G I H'),
        );
    }

    public function inOrderProvider() {
        return array(
            array($this->tree1, 'AA'),
            array($this->tree2, 'BB AA'),
            array($this->tree3, 'AA CC'),
            array($this->tree4, 'BB AA CC'),
            array($this->tree5, 'BB II AA DD CC JJ'),
            array($this->tree6, 'A B C D E F G H I'),
        );
    }

    public function postOrderProvider() {
        return array(
            array($this->tree1, 'AA'),
            array($this->tree2, 'BB AA'),
            array($this->tree3, 'CC AA'),
            array($this->tree4, 'BB CC AA'),
            array($this->tree5, 'II BB DD JJ CC AA'),
            array($this->tree6, 'A C E D B H I G F'),
        );
    }
}
