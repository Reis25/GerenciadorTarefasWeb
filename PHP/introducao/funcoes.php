<?php

$texto = 'Aula de funcoes nativas PHP';

// Função para deixar todas as letras maiúsculos  
echo strtoupper($texto).'<br>';

// Função para deixar todas as letras minúsculas 
echo strtolower($texto).'<br>';

// Função para deixar a letra inicial maiúscula 
echo ucfirst($texto).'<br>'; 

// Funçao que conta quantos caracteres a string possui:
echo strlen($texto).'<br>';

// Função que irá substituit uma cadeia de caracteres exatamente igual:
echo str_replace('PHP', 'JavaScript', $texto).'<br>';

// Função que mostra somente a quantidade de caracteres de texto que foi determinada:
echo substr($texto, 5, 10).'<br>'; 

// Fazer uma função para calcular o dobro de uma raiz quadrada; 
function dobro_raiz($numero){
    $raiz = sqrt($numero);
    $dobro = $raiz * 2; 

    return $dobro;
}

$valor_calculado = dobro_raiz(100);

echo $valor_calculado.'<br>'; 

?>