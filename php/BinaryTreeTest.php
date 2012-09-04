<?php
require_once './BinaryTree.php';

/**
 * Test suite for the BinaryTree class.
 */
class BinaryTreeTest extends PHPUnit_Framework_TestCase {
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

        http://bit.ly/OTZvS8
        All data providers are executed before the first call to the setUp function.
        Because of that you can't access any variables you create there from within a data provider.
*/
    public function componentProvider() {
        return array(
            array('(AA () ())',                                                        'AA', '()', '()'),
            array('(AA (BB () ()) ())',                                                'AA', '(BB () ())', '()'),
            array('(AA () (CC () ()))',                                                'AA', '()', '(CC () ())'),
            array('(AA (BB () ()) (CC () ()))',                                        'AA', '(BB () ())', '(CC () ())'),
            array('(AA (BB () (II () ())) (CC (DD () ()) (JJ () ())))',                'AA', '(BB () (II () ()))', '(CC (DD () ()) (JJ () ()))'),
            array('(F (B (A () ()) (D (C () ()) (E () ()))) (G () (I (H () ()) ())))', 'F', '(B (A () ()) (D (C () ()) (E () ())))', '(G () (I (H () ()) ()))'),
        );
    }

    public function preOrderProvider() {
        return array(
            array('(AA () ())',                                                        'AA'),
            array('(AA (BB () ()) ())',                                                'AA BB'),
            array('(AA () (CC () ()))',                                                'AA CC'),
            array('(AA (BB () ()) (CC () ()))',                                        'AA BB CC'),
            array('(AA (BB () (II () ())) (CC (DD () ()) (JJ () ())))',                'AA BB II CC DD JJ'),
            array('(F (B (A () ()) (D (C () ()) (E () ()))) (G () (I (H () ()) ())))', 'F B A D C E G I H'),
        );
    }

    public function inOrderProvider() {
        return array(
            array('(AA () ())',                                                        'AA'),
            array('(AA (BB () ()) ())',                                                'BB AA'),
            array('(AA () (CC () ()))',                                                'AA CC'),
            array('(AA (BB () ()) (CC () ()))',                                        'BB AA CC'),
            array('(AA (BB () (II () ())) (CC (DD () ()) (JJ () ())))',                'BB II AA DD CC JJ'),
            array('(F (B (A () ()) (D (C () ()) (E () ()))) (G () (I (H () ()) ())))', 'A B C D E F G H I'),
        );
    }

    public function postOrderProvider() {
        return array(
            array('(AA () ())',                                                        'AA'),
            array('(AA (BB () ()) ())',                                                'BB AA'),
            array('(AA () (CC () ()))',                                                'CC AA'),
            array('(AA (BB () ()) (CC () ()))',                                        'BB CC AA'),
            array('(AA (BB () (II () ())) (CC (DD () ()) (JJ () ())))',                'II BB DD JJ CC AA'),
            array('(F (B (A () ()) (D (C () ()) (E () ()))) (G () (I (H () ()) ())))', 'A C E D B H I G F'),
        );
    }
}
