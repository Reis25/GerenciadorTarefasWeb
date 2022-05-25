# Desenvovolvimento de sistemas 

Repositório  para sistema de gerenciamento de tarefas. Usando as stack de desenvolvimento: HTML, CSS, PHP, SQL e MySQL. 

O sistema operacional para a construção da aplicação foi o Linux-Ubuntu 18.04. 

Além da stck de desenvolvimento precisamos fazer a instalação do LAMP. 

* LAMP é uma combinação de quatro softwares de código aberto: *Linux*, *Apache*, *MySQL* e *PHP*. Juntos, eles formam uma plataforma poderosa, que facilita e otimiza a construção e o gerenciamento de serviços e aplicativos web.

Para fazer a instalçaõ do LAMP no Ubuntu segue o tutorial: 

Abrir terminal linux:
~~~
Ctrl + t
~~~

liberando o super usuário (só para ambientes locais): 
~~~Shell script
$ sudo passwd root
~~~

Digita a senha de usuário: 
~~~
$ <Digita a senha>
~~~ 
Digita a senha do Unix: 

~~~Shell script
$ < senha do Unix>
~~~

Desbloquendo usuário (onlocked): 

~~~Shell script
$ sudo passwd -u root 
~~~

Entrando no modo super-usuário: 

~~~Shell script
$ su
~~~

* Usuário com o sifrão na frente é o usuário comum, para # significa que estamos no modo root.

Atualizando sistema:

~~~Shell script
# apt-get update
~~~

Restaurando pacote e fazendo upgrade de sistema: 

~~~Shell script
# apt-get upgrade
~~~

Instalando o LAMP: 
~~~
# apt-get install lamp-server^
~~~

Dando permissão na pasta: 

~~~Shell script
# chmod -R 777 /var/www/
~~~

Saindo do modo super usuario:

~~~Shell script
# exit 
~~~

Vá até a pasta www e crie um diretório para teste: 
~~~Shell script
$ cd /var/www/ && mkdir teste 
~~~

Para conferir as versões e pacote instalados, crir um arquivo teste.php na pasta que foi criada com o seginte conteúdo: 
~~~php
<?php

phpinfo();

?> 
~~~

Vá até o navegador e digite na URL: 

~~~Shell script
$ localhost/teste/teste.php 
~~~

Enjoy! :D



