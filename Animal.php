<?php
    $animals = array(
            "Lion" => "carnivorous",
            "Bear" => "omnivorous",
            "Human" => "omnivorous",
            "Dog" => "omnivorous",
            "Raccoon" => "omnivorous",
            "Crow" => "omnivorous"
        );
    $animalCount = count($animals);
    foreach ($animals as $animal => $diet) 
    {
        echo "$animal are $diet.<br>";
    }
    echo "Total number of animals: $animalCount";
?>
