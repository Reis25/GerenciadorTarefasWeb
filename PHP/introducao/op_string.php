<?php
$texto = 'Aula de funcoes nativas PHP';

echo '<br>';

// Função para deixar todas as letras maiúsculos  
echo strtoupper($texto);

echo '<br>';

// Função para deixar todas as letras minúsculas 
echo strtolower($texto);

echo '<br>';

// Função para deixar todas as letras iniciais maiúsculas 
echo ucfirst($texto); 

echo '<br>';

// Funçao que conta quantos caracteres a string possui:
echo strlen($texto); 
echo '<br>';

// Função que irá substituit uma cadeia de caracteres exatamente igual:
echo str_replace('PHP', 'JavaScript', $texto);
echo '<br>';

// Função que mostra somente a quantidade de caracteres de texto que foi determinada:
echo substr($texto, 5, 10); 
echo '<br>';

?>