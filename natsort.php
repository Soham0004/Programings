<?php
    $arr1=array("Srija", "Munil", "Akasha", "bhanu");
    $arr2=$arr1;
    sort($arr1);
    echo "Standard sorting: ";
    print_r($arr1);
    echo "<br>";
    //natsort($arr2);
    natcasesort($arr2);
    echo "Natural ordering case insensitive: ";
    print_r($arr2);
?>
