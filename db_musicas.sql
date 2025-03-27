create database play_musica;
use play_musica;
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