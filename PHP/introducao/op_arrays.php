<?php

echo "-------------------------------------<br>";
// Declaração do array: 
$nomes = array('demetrios', 'reis', 'costa'); 
$numeros = [1,100, 4, 16, 25, 36, 49, 64];

echo "-------------------------------------<br>";
echo "Mostrando apenas um elemento do array: <br>";
echo $nomes[1];

echo "-------------------------------------<br>";
echo "Mostrando os valores do array e sua raiz quadrada: <br>";
for ($i=0; $i <7 ; $i++) { 
    echo "A raiz quadrada de ". $numeros[$i] ." é igual  ". sqrt($numeros[$i]). "<br>";
}

echo "-------------------------------------<br>";
echo "Mostrando os valores do array: <br>";
for ($i=0; $i < count($numeros) ; $i++) { 
     echo "$i ª posição tem o valor: ". $numeros[$i] ."<br>";
}

echo "-------------------------------------<br>";
echo "Mostrando informações do array: <br>";
print_r($numeros);
echo "<br>";

echo "-------------------------------------<br>";
echo "Mostrando informações do array: <br>";
var_dump($numeros);
echo "<br>";


echo "-------------------------------------<br>";
echo "Adicionando um novo valor no nosso array: 256 <br>";

$numeros[] = 256;
for ($i=0; $i <count($numeros) ; $i++) { 
    echo $numeros[$i]. "<br>";
}

echo "-------------------------------------<br>";
echo "Trabalhando com array multdimensional";

$lista_coisas = [];
$lista_coisas['frutas'] = array(1 => 'banana', 2 => 'melancia',3 => 'melao');
$lista_coisas['pessoas'] = [1 => 'joao', 2 => 'jose',3 => 'maria'];

echo "<br>";
echo print_r($lista_coisas);
echo "<br>";

echo "-------------------------------------<br>";
echo "<br>";
echo var_dump($lista_coisas);
echo "<br>";

echo "-------------------------------------<br>";
echo "<pre>";
echo print_r($lista_coisas);
echo "</pre>";

echo "-------------------------------------<br>";
echo "<pre>";
echo var_dump($lista_coisas);
echo "</pre>";


echo "-------------------------------------<br>";
echo "<hr>";
echo $lista_coisas['frutas'][3];
echo "<hr>";
echo $lista_coisas['pessoas'][2];
echo "<br>";

echo "-------------------------------------<br>";
echo "Usando a função nativa para saber o índice de um valor: <br>";
$senteca = array_search(25, $numeros);
echo "O numero está no índice : $senteca"; 
echo "<br>";


echo "-------------------------------------<br>";
echo "Usando a função nativa para saber o índice de um valor: <br>";
$existe = in_array(250, $numeros);
echo $existe; 
echo "<br>";



?>
