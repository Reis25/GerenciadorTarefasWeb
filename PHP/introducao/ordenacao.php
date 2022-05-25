<?php
$numeros = [1,100, 4, 16, 25, 36, 49, 64];

echo "-------------------------------------<br>";
echo "Ordenando um vetor: <br>";

echo "Vetor original: <br>";
for ($i=0; $i <count($numeros) ; $i++) { 
    echo "$numeros[$i], ";
}

echo "<br>";
echo "Vetor ordenado <br>";

sort($numeros);
for ($i=0; $i <count($numeros) ; $i++) { 
    echo "$numeros[$i], ";
}

echo "<br>";


?>
