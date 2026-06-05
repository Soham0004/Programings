<?php
    $arr1 = array("My", "name","is");
    $arr2 = array("Soham", "Sarkar");
    $arr1= array_merge($arr1, $arr2);
    echo "INTRODUCTION: ";
    foreach($arr1 as $value)
    {
        echo $value . "\n";
    }
?>
