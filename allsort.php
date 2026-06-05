<?php
    $age=array("James"=>"25","Rama"=>"10","Alice"=>"15","Mary"=>"30","Radha"=>"20");
    //asort($age);
    //arsort($age);
    //ksort($age);
    //krsort($age);
    shuffle($age);
    $alength=count($age);
    foreach($age as $x=>$val)
    {
        echo "key=" .$x.",value=".$val;
        echo"<br>";
    }
?>
