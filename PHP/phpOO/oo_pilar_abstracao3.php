<?php  
//Getters e setters mágicos

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
		public $cargo = null;
		public $salario = null;

		//overloading sobrecarga dos métodos
		function __set($atributo, $valor){
			$this->$atributo = $valor;
		}

		function __get($atributo){
			return $this->$atributo;
		}

		//Metodos getters e setters
		//setters => tipo void
		/*function setNome($nome){
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
		}*/

		//Métodos
		function resumirCadFunc (){
			//return 'Esse é o resumo do cadastro do funcionario';
			return "$this->nome possui $this->numFilhos filhos(a) e seu telefone é $this->telefone, seu cargo $this->cargo e seu salário $this->salario";
		}

		function modificarNumFilhos($numFilhos){
			$this->numFilhos = $numFilhos;
		}
	}

	$y = new Funcionario();
	$y->__set('nome','Carlos');
	$y->__set('numFilhos', 4);
	$y->__set('telefone', '(82)99999-8888');
	$y->__set('cargo', 'Gerente');
	$y->__set('salario', 2000);
	echo $y->resumirCadFunc();
	echo '<br>';
	echo $y->__get('nome').' possui '.$y->__get('numFilhos').' filhos(a) e seu telefone é '.$y->__get('telefone').' Seu cargo '.$y->__get('cargo').' e seu salário é: '.$y->__get('salario');
	
	echo '<br>';
?>