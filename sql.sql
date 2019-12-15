create database erp;

create table cadastros(

nome varchar(50) not null,
senha varchar(20) not null,
nivel int not null


);

insert into cadastros values ('admin', 'admin', 2);

drop table produtos;

create table produtos(
id int auto_increment not null primary key,
nome varchar(100) not null,
ingredientes varchar(1000),
grupo varchar(100),
preco float

);

drop table pedidos;

create table pedidos(
id int not null primary key auto_increment,
nome varchar(100) not null,
ingredientes varchar(1000),
grupo varchar(100),
localEntrega varchar(500),
observacoes varchar(1000)

);

select	 * from produtos;

insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes) values ('pizza de mussarela', 'mussarela', 'pizzas', '', 'sem cebola');
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes) values ('coca', '', 'bebidas', '', '');

drop table estatisticaVendido;

create table estatisticaVendido(

id int not null primary key auto_increment,
nome varchar(100) not null,
grupo varchar(100),
preco float
	

);

select * from estatisticaVendido;

insert into estatisticaVendido(nome, grupo, preco) values ('pizza de mussarela', 'pizzas', 34.90);

insert into estatisticaVendido(nome, grupo, preco) values ('coca', 'bebidas', 6);

insert into estatisticaVendido(nome, grupo, preco) values ('pizza de portuguesa', 'pizzas', 34.90);

insert into estatisticaVendido(nome, grupo, preco) values ('suco de laranja', 'pizzas', 7);

select * from cadastros;

