<?php

$n=0;
$a=0;
$b=1;
echo "Fibonacci series upto 15: ";
echo "$a,$b";

while($n<16)
    {
        $c=$b + $a;
        echo " , ";
        echo "$c";
        $a=$b;
        $b=$c;
        $n=$n+1;
    }

?> 