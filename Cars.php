<?php
    $cars=array("Volvo", "BMW", "Toyota", "Audi", "Swift Dzire");
    echo"I like ".$cars[0].", ".$cars[1]." and ".$cars[2].".<br>";
    echo count($cars)."<br>";
    $arrlength = count($cars);
    for($x=0; $x<$arrlength; $x++)
    {
        echo $cars[$x];
        echo "<br>";
    }
?>
