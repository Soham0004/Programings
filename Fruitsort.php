<?php
    $fruits=array("Apple", "Banana", "Guava", "Orange", "Mango", "Watermelon");
    $fruit=$fruits;
    sort($fruit);
    rsort($fruits);
    $clength=count($fruit);
    for($x=0;$x<$clength;$x++)
    {
        echo $fruit [$x];
        echo"<br>";
    }
    echo"<br>";
    $clength=count($fruits);
    for($x=0; $x<$clength; $x++)
    {
        echo $fruits [$x];
        echo"<br>";
    }
?>
