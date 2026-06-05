<?php
    $student=array("Name" => "Soham", "Email" => "ssarkar041999@gmail.com", "Age" => "23", "Gender" => "Male");
    foreach($student as $key => $element)
    {
        echo $key. ":".$element;
        echo "<br>";
    }
?>