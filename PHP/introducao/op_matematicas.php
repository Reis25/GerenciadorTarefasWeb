<?php

$numero = 7.589;

// Funçao para arredondar para o próximo inteiro superior;
echo ceil($numero).'<br>';

// Função para arredondar para o próximo inteiro inferior 
echo floor($numero).'<br>';

// Função para arredondamento
echo round($numero, 2).'<br>';

// Gerar um valor aleatório: 
echo rand(1,9).'<br>';


// Raiz quadrada de um número; 
$calcular_raiz = 64;
echo sqrt($calcular_raiz).'<br>'; 

// vai calcular o dobro de uma raiz quadrada 
function dobro_da_raiz($num){
        $raiz = sqrt($num);
        $dobro = $raiz * 2;

        return $dobro;
}

$testando = dobro_da_raiz(100);
 
echo $testando;
?>