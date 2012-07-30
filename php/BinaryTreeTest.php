<?php
require_once './BinaryTree.php';

/**
 * Test suite for the BinaryTree class.
 */
class BinaryTreeTest extends PHPUnit_Framework_TestCase {
    protected $tree;

    protected function setUp() {
        $this->tree = new BinaryTree();
    }

    /**
     * @dataProvider syntaxProvider
     */
    public function testParenCountEqual($a, $expected) {
        $actual = $this->tree->checkParenCount($a);
        $this->assertEquals($expected, $actual);
    }

    /**
     * @dataProvider syntaxProvider
     */
    //public function testCheckSyntax($a, $expected) {
        //$actual = $this->tree->checkSyntax($a);
        //$this->assertEquals($expected, $actual);
    //}

    /**
     * @dataProvider componentProvider
     */
    public function testGetCompnents($treeString, $value, $left, $right) {
        $components= $this->tree->getComponents($treeString);
        $this->assertEquals($value, $components['value']);
        $this->assertEquals($left,  $components['left']);
        $this->assertEquals($right, $components['right']);
    }

    public function componentProvider() {
        return array(
            array('(AA () ())', 'AA', '()', '()'),
            array('(AA (BB () ()) ())', 'AA', '(BB () ())', '()'),
            array('(AA () (CC () ()))', 'AA', '()', '(CC () ())'),
            array('(AA (BB () ()) (CC () ()))', 'AA', '(BB () ())', '(CC () ())'),
            array('(AA (BB () (II () ())) (CC (DD () ()) (JJ () ())))', 'AA', '(BB () (II () ()))', '(CC (DD () ()) (JJ () ()))'),
        );
    }

    public function syntaxProvider() {
        return array(
            array('()',     true),
            array('(',      false),
            array('(()())', true),
            array('(()',    false),
            array('((((())))(()))', true),
            array('((((()))(()))', false),
        );
    }


}
