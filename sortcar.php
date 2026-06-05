<?php 
    $cars=array("Volvo","BMW","Toyota","Audi","Bentz","Suzuki"); 
    $car=$cars; 
    sort($car); 
    rsort($cars);
    $clength=count($car); 
    for($x=0;$x<$clength;$x++)
    { 
        echo $car [$x]; echo"<br>"; 
    }
    echo"<br>";
    $clength=count($cars); 
    for($x=0;$x<$clength;$x++)
    { 
        echo $cars [$x]; 
        echo"<br>"; 
    } 
?>
