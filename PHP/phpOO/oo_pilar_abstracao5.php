<?php  
	class Pessoa {

		public $nome = null;

		function __construct($nome){
			echo "Objeto foi criado";			
			$this->nome = $nome;
		}

		function __destruct(){
			echo "Objeto removido";
		}

		function __get($atributo){
			return $this->$atributo;
		}

		function correr(){
			return $this->__get('nome').' está correndo';
		}

	}

	$pessoa = new Pessoa('Carlos');
	echo '<br>Nome: '.$pessoa->__get('nome');
	echo '<br>'.$pessoa->correr();
	//$pessoa->__get('nome');
	echo "<br>";
	unset($pessoa); //proposital
 
?>