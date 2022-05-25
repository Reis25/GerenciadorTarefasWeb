<?php

$a = 1;
$b =-5; 
$c = 6;

$delta = $b*$b - 4*$a*$c; 

echo "O valor de delta é: $delta <br>";

if($a != 0){

    if($delta < 0){
        echo "A equação com os coeficientes $a $b e $c não possui raízes reais <br>";
    }elseif ($delta == 0) {
        echo "A equação com os coeficientes $a $b e $c possui duas raízes identicas.<br>";
        $x1 = (-$b)/2*$a;
        echo "Sendo $x1<br>";

    }else{
        echo "A equação com os coeficientes $a $b e $c possui raízes reais: <br>";
        $x1 = (-$b - sqrt($delta))/2*$a;
        $x2 = (-$b + sqrt($delta))/2*$a;
        echo "Sendo $x1 a primeira raiz <br>";
        echo "Sendo $x2 a segunda raiz <br>";

    }
}else{
    echo "O valor de A não pode ser igual a zero!<br>";
}

?>