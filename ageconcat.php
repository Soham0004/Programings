<?php
    $age=array("Peter" => "35", "Ben" => "37", "Joe" => "43",);
    echo "Peter is ".$age['Peter']." years old.<br>";
    foreach($age as $x=> $x_value)
    {
        echo "Key = ".$x.", value =".$x_value;
        echo "<br>";
    }
?>