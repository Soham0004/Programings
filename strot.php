<?php
    $d=strtotime("tomorrow");
    echo date("y-m-d h:i:sa",$d)."<br>";
    $d=strtotime("next Saturday");
    echo date("y-m-d h:i:sa",$d)."<br>";
    $d=strtotime("+3 Months");
    echo date("y-m-d h:i:sa",$d)."<br>";
?>
