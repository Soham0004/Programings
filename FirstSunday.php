<?php
    echo "Display sunday as first day of the week";
    echo"<br>";
    $res=date('1-d/m/y',strtotime("Sunday 0 week"));
    echo "First day (next week)=",$res." ";
    echo"<br>";
    var_dump(filter_var($res,FILTER_VALIDATE_BOOLEAN));
?>
