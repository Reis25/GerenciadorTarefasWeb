<?php  
	class Produto{     
		
		# Atributos(variáveis)
		public $codigo;
		public $descricao;
		public $preco;
		public $quantidade;

		# Métodos(Funções)	
		function imprimirEtiqueta(){
			echo 'Código: '.$this->codigo.'<br>';
			echo 'Descrição: '.$this->descricao.'<br>';
		}	
	}
	//Criando um objeto
	$produto1 = new Produto();
	$produto2 = new Produto();

	//Atribuindo valor ao objeto 1
	$produto1->codigo = 01;
	$produto1->descricao = 'CD - Death Magnet';

	//Atribuindo valor ao objeto 2
	$produto2->codigo = 10;
	$produto2->descricao = 'Zenphone 4';

	//imprimindo produto1
	$produto1->imprimirEtiqueta();
	echo '<hr>';
	$produto2->imprimirEtiqueta();


	//Imprimindo o objeto
	echo "<pre>";
		print_r($produto1);
	echo "</pre>";
	

?>

