<?php
/* 
    When you start adding the values from the left side of an array and start 
    adding the values from the right side of an array, and the counts are 
    equal, and you have exactly one index in between, you have an array pivot.

    ex.  
    1|2|1                 left count = 1 ; right count = 1 ; array pivot = 2
    2|5|4|5|1|2|3|4|1     left count = 11; right count = 11; array pivot = 5
    1|4|3|2|1|5|4|5|2     left count = 11; right count = 11; array pivot = 5
    1|0|1                 left count = 1 ; right count = 1 ; array pivot = 2
    0|0                   no
    -1|0|0|0|-1           left count = 0 ; right count = 0 ; array pivot = 0
    -1|0|1|0|0|1|-1       depends on implementation, mine says no
    1 | 2 | 9 | 3         left count = 3 ; right count = 3 ; array pivot = 9
*/

function arraypivot($a) {
    if (sizeof($a) < 3) return null;

    $lpos = 0;
    $rpos = sizeof($a) - 1;

    $lcount = $a[$lpos];
    $rcount = $a[$rpos];
    while ($lpos <= $rpos) {
//echo sprintf("li=%d ri=%d : lc=%d rc=%d\n",$lpos, $rpos, $lcount, $rcount);
        
        // check for success
        if (($lcount == $rcount) && ($lpos + 1 == $rpos - 1)) {
            return $lpos + 1;  // or return $rpos - 1;
        }
        
        // increment both sides 
        if ($lcount == $rcount) {
            $lcount += $a[++$lpos];
            $rcount += $a[--$rpos];
        }
        // increment left side
        elseif ($lcount < $rcount) {
            $lcount += $a[++$lpos];
        }
        // increment right side
        else {
            $rcount += $a[--$rpos];
        }        
    }

    return null;
}

$as = array( 
    array(1,2,1),
    array(2,5,4,5,1,2,3,4,1),
    array(1,4,3,2,1,5,4,5,2),
    array(0,0,0),
    array(0,0),
    array(-1,0,0,0,-1),
    array(-1,0,1,0,0,1,-1),
    array(1,2,9,3),
);

foreach ($as as $index => $a) {
    echo implode(' ', $a). "\n";
    if ($i = arraypivot($a) ) {
      echo sprintf("pivot found : array[%d] = %d\n\n", $i, $a[$i]);
    }
    else {
      echo "nada\n\n";
    }
}

