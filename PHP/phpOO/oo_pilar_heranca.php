<?php

	class Veiculo{
		public $placa = null;
		public $cor = null;

		function acelerar(){
			echo "Acelerar";
		}
		function freiar(){
			echo "Freiar";
		}
	}
	
	class Carro extends Veiculo{
		public $teto_solar = true;

		function __construct($placa, $cor){
			$this->placa = $placa;
			$this->cor = $cor;

		}

		function abrirTetoSolar(){
			echo "Abrir teto solar";
		}

		function autrarPosicaoVolante(){
			echo "Alterar posição volante";
		}
	}

	class Moto extends Veiculo{
		public $contraPesoGuidao = true;

		function __construct($placa, $cor){
			$this->placa = $placa;
			$this->cor = $cor;
		}

		function empinar(){
			echo 'empinar';
		}
	}

	//Objeto Carro
	$carro = new Carro('ABD-1234', 'Branco');
	echo '<pre>';
		print_r($carro);
	echo "</pre>";

	//Objeto Moto
	$moto = new Moto('DEF-4321','Preta');
	echo '<pre>';
		print_r($moto);
	echo "</pre>";

	echo "<hr>";

	$carro->abrirTetoSolar();
	echo "<br>";
	$carro->acelerar();
	echo "<br>";
	$carro->freiar();

	echo "<hr>";
	$moto->empinar();
	echo "<br>";
	$moto->acelerar();
	echo "<br>";
	$carro->freiar();
?>