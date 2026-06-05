<?php
    $directions = array("East", "West", "South", "North");
    $directionCount = count($directions);
    foreach ($directions as $direction)
    {
        echo "Direction name ===> $direction <br>";
    }
    echo "Total number of directions: $directionCount";
?>
