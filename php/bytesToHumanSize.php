<?php
      /**
       * Convert bytes to human readable format
       *
       * @param integer bytes Size in bytes to convert
       * @return string
       */
function bytesToHumanSize($bytes, $precision = 2) {
    $kilobyte = 1024;
    $megabyte = $kilobyte * 1024;
    $gigabyte = $megabyte * 1024;
    $terabyte = $gigabyte * 1024;

    if (($bytes >= 0) && ($bytes < $kilobyte)) {
        return $bytes . 'B';
    } elseif (($bytes >= $kilobyte) && ($bytes < $megabyte)) {
        return round($bytes / $kilobyte, $precision) . 'K';
    } elseif (($bytes >= $megabyte) && ($bytes < $gigabyte)) {
        return round($bytes / $megabyte, $precision) . 'M';
    } elseif (($bytes >= $gigabyte) && ($bytes < $terabyte)) {
        return round($bytes / $gigabyte, $precision) . 'G';
    } elseif ($bytes >= $terabyte) {
        return round($bytes / $terabyte, $precision) . 'T';
    } else {
        return $bytes . 'B';
    }
}

$datas = [
    0 => '0B',
    34 => '34',
    204 => '204B',
    272 => '272B',
    398 => '398B',
    476 => '476B',
    1020 => '1.0K',
    1061 => '1.0K',
    2924 => '2.9K',
    3141 => '3.1K',
    4096 => '4.0K',
    4335 => '4.3K',
    6148 => '6.1K',
    12333 => '12K',
    12886 => '13K',
    21508 => '21K',
    40960 => '40K',
    58487 => '57K',
    62019 => '61K',
    64249 => '63K',
    66777 => '65K',
    71863 => '70K',
    78849 => '77K',
    85410 => '83K',
    116256 => '114K',
    826478 => '807K',
    1740800 => '1.7M',
    2499707 => '2.4M',
    2499788 => '2.4M',
    9125437 => '8.7M',
    353657552 => '337M',
    1199666893 => '1.1G',
    1373870118 => '1.3G',
    1411625229 => '1.3G',
    1693261610 => '1.6G',
    8211330033 => '7.7G',
];

foreach ($datas as $bytes => $human) {
    $v = bytesToHumanSize($bytes, 1);
    echo sprintf("%s\t%s\t%s\t%s\n", $bytes, $human, $v, $human === $v ? 'good' : 'bad');
}

/*
[php (master)-]> php bytesToHumanSize.php
0   0B  0B  good
34  34  34B bad
204 204B    204B    good
272 272B    272B    good
398 398B    398B    good
476 476B    476B    good
1020    1.0K    1020B   bad
1061    1.0K    1K  bad
2924    2.9K    2.9K    good
3141    3.1K    3.1K    good
4096    4.0K    4K  bad
4335    4.3K    4.2K    bad
6148    6.1K    6K  bad
12333   12K 12K good
12886   13K 12.6K   bad
21508   21K 21K good
40960   40K 40K good
58487   57K 57.1K   bad
62019   61K 60.6K   bad
64249   63K 62.7K   bad
66777   65K 65.2K   bad
71863   70K 70.2K   bad
78849   77K 77K good
85410   83K 83.4K   bad
116256  114K    113.5K  bad
826478  807K    807.1K  bad
1740800 1.7M    1.7M    good
2499707 2.4M    2.4M    good
2499788 2.4M    2.4M    good
9125437 8.7M    8.7M    good
353657552   337M    337.3M  bad
1199666893  1.1G    1.1G    good
1373870118  1.3G    1.3G    good
1411625229  1.3G    1.3G    good
1693261610  1.6G    1.6G    good
8211330033  7.7G    7.6G    bad
*/
