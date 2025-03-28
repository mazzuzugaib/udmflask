create database play_musica;
use play_musica;

/*tabela das musicas que serao cadastradas*/
create table musica(
	id int primary key auto_increment not null,
    titulo varchar(50) not null,
    artista varchar(50) not null,
    genero varchar(50) not null);
insert into musica(titulo, artista, genero)
values ('Saturday Night', 'Elton John', 'Rock'),
	('Bohemian Rhapsody', 'Queen', 'Rock'),  
    ('Billie Jean', 'Michael Jackson', 'Pop'),  
    ('Shape of You', 'Ed Sheeran', 'Pop');  
select * from musica;
delete from musica where id = 1;

/*tabela dos usuarios*/
create table usuario(
	id int primary key auto_increment not null,
    nome_us varchar(40) not null,
    login_us varchar(10) not null,
    senha_us varchar(10) not null);
    
/*adicionando usuarios na tabela*/
insert into usuario(nome_us, login_us, senha_us)
values ('Lorem Ipsum', 'lorem', 'ipsum'),
('Dolor sit', 'Dolor', 'Sit'),
('Amet Consectetur', 'Amet', 'Consec');