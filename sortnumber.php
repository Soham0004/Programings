<?php
    $numbers=array(4,6,2,22,11,15,19);
    $number=$numbers;
    sort($number);
    rsort($numbers);
    $clength=count($number);
    for($x=0; $x<$clength; $x++)
    {
        echo $number [$x];
        echo"<br>";
    }
    echo"<br>";
    $clength=count($numbers);
    for($x=0; $x<$clength; $x++)
    {
        echo $numbers [$x];
        echo"<br>";
    }
?>
