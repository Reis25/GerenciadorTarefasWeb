<?php  
	class Pai{
		private $nome = 'Carlos';
		protected $sobrenome = 'Vasconcelos';
		public $humor = 'Feliz';

		//Manipulando Atibuto public
		function Humor($humor){
			$this->humor = $humor;
		}

		//Manipulando Atributo private
		public function getNome(){
			return $this->nome;
		}

		public function setNome($value){
			
			if(strlen($value) >=3){
				$this->nome = $value;
			}
		}

		//Manipulando atributo protected
		public function getSobrenome(){
			return $this->sobrenome;
		}

		public function setSobrenome($value){
			
			if(strlen($value) >=3){
				$this->sobrenome = $value;
			}
		}

	}

	$pai = new Pai();
	//Manipulando atributo public
	echo $pai->humor.'<br>';
	$pai->Humor('Triste');
	echo "$pai->humor <br>";

	//Manipulando atributo privado
	echo $pai->getNome();
	$pai->setNome('Wilton');
	echo "<br>";
	echo $pai->getNome();
	echo "<br>";

	//Manipulando atributo Protected
	echo $pai->getSobrenome();
	$pai->setSobrenome('Fonseca');
	echo "<br>";
	echo $pai->getSobrenome();
	echo "<br>";

?>