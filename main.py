from flask import Flask, render_template, request, redirect, session, flash, url_for

# Classe Musica
class Musica:
    def __init__(self, titulo, artista, genero):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

musica1 = Musica('Ouro de Tolo', 'Raul Seixas', 'Rock')
musica2 = Musica('Garganta', 'Ana Carolina', 'MPB')
musica3 = Musica('Radioactive', 'Imagine Dragons', 'Rock')

lista_musicas = [musica1, musica2, musica3]

# classe para instanciar usuarios
class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

#instanciando usuarios
user1 = Usuario('Lorem Ipsum', 'lorem', 'ipsum')
user2 = Usuario('Dolor Sit', 'dolor', 'sit')
user3 = Usuario('Amet Consectetur', 'amet', 'consectetur')

#atribuindo chave para o usuario dentro de um dicionario
usuarios = {user1.login: user1,
            user2.login: user2,
            user3.login: user3}

app = Flask(__name__)

app.secret_key = 'satorarepotenetoperarotas'

@app.route('/')
def lista_musica():
    if 'usuario_in' not in session or session['usuario_in'] == None:
        return redirect(url_for('login'))
     
    return render_template('lista_musica.html', titulo = 'Lista de músicas', musicas = lista_musicas)

@app.route('/cadastro')
def cadastro_musica():
    if 'usuario_in' not in session or session['usuario_in'] == None:
        return redirect('/login')
    return render_template('cadastro_musica.html', titulo = 'Cadastro de músicas')

@app.route('/salvar_musica', methods = ['POST',])
def salvar_musica():

    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']

    nova_musica = Musica(titulo, artista, genero)

    lista_musicas.append(nova_musica)

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():
     
    if request.form['usuario'] in usuarios and usuarios[request.form['usuario']].senha == request.form['senha']:
   
        user_encontrado = usuarios[request.form['usuario']]


        session['usuario_in'] = request.form['usuario']

        flash(f'Olá {user_encontrado.nome}, seja bem-vindo(a)')

        return redirect('/')
            
    else:
        flash('Usuário ou senha inválidos')
        return redirect(url_for('login'))

@app.route('/sair')
def sair():
    session['usuario_in'] = None
    return redirect ('/login')
       

app.run(debug=True)