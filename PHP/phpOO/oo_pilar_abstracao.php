<?php  
	//Definir o modelo
	//Nome da classe Funcionario
	class Funcionario{	
		//Atributos
		/*public $nome = null; 
		public $telefone = null;
		public $numFilhos = null;*/

		public $nome = 'Carlos'; 
		public $telefone = '11 99999-8888';
		public $numFilhos = 2;

		//Métodos
		function resumirCadFunc (){
			//return 'Esse é o resumo do cadastro do funcionario';
			return "$this->nome possui $this->numFilhos filhos(a)";
		}

		function modificarNumFilhos($numFilhos){
			$this->numFilhos = $numFilhos;
		}
	}

	$y = new Funcionario();
	echo $y->resumirCadFunc();
	echo "<br>";
	$y->modificarNumFilhos(8);
	echo $y->resumirCadFunc();
	echo "<hr>";

	$x = new Funcionario();
	echo $x->resumirCadFunc();
	echo "<br>";
	$x->modificarNumFilhos(1);
	echo $x->resumirCadFunc();

?>