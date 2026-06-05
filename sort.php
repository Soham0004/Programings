<?php
    $age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43","Milan"=>"29","Rohan"=>"31");
    ksort($age);
    arsort($age);
    krsort($age);
    asort($age);
    $alength=count($age);
    foreach($age as $x=>$val)
    {
        echo "key=" .$x.",value=".$val;
        echo"<br>";
    }
?>
