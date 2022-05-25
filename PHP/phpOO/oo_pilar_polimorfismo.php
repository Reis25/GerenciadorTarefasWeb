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

		function trocarMarcha(){
			echo "Desengatar embreagem com o pé e engatar a marcha com a mão <br>";
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

		function trocarMarcha(){
			echo "Desengatar embreagem com o mão e engatar a marcha com a pé <br>";
		}
	}

	$carro = new Carro('ABD-1234', 'Branco');
	$carro->trocarMarcha();
	$moto = new Moto('DEF-4321','Preta');
	$moto->trocarMarcha();

?>