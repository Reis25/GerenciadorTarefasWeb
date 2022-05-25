<?php  
	//Definir o modelo
	//Nome da classe Funcionario
	class Funcionario{	
		//Atributos
		/*public $nome = null; 
		public $telefone = null;
		public $numFilhos = null;*/

		public $nome = null;
		public $telefone = null;
		public $numFilhos = null;

		//Metodos getters e setters
		//setters => tipo void
		function setNome($nome){
			$this->nome = $nome;
		}
		function setNumFilhos($numFilhos){
			$this->numFilhos = $numFilhos;
		}
		function setTelefone($telefone){
			$this->telefone = $telefone;
		}

		//Getters
		function getNome(){
			return $this->nome;
		}
		function getNumFilhos(){
			return $this->numFilhos;
		}
		function getTelefone(){
			return $this->telefone;
		}

		//Métodos
		function resumirCadFunc (){
			//return 'Esse é o resumo do cadastro do funcionario';
			return "$this->nome possui $this->numFilhos filhos(a) e seu telefone é $this->telefone";
		}

		function modificarNumFilhos($numFilhos){
			$this->numFilhos = $numFilhos;
		}
	}

	$y = new Funcionario();
	$y->setNome('Carlos');
	$y->setNumFilhos(3);
	$y->setTelefone('11 99998-8998');
	echo $y->resumirCadFunc();
	echo '<br>';
	echo $y->getNome().' possui '.$y->getNumFilhos().' filhos(a) e seu telefone é '.$y->getTelefone();
	
	echo '<br>';

	$x = new Funcionario();
	$x->setNome('Alexandra');
	$x->setNumFilhos(5);
	$x->setTelefone('82 99925-4591');
	echo $x->resumirCadFunc();

?>