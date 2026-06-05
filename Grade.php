<?php

    $average=79;
    switch($average)
    {
        case($average>70):
        echo"Grade=A";
        break;

        case($average>=60 && $average<=69):
        echo"Grade=B";
        break;

        case($average>=50 && $average<=59):
        echo"Grade=C";
        break;

        default:
        echo"Not given the exam!";
    }

?>