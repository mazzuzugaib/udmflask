from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'satorarepotenetoperarotas'

# Configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{DB}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'tenet',
    senha = 'tenet',
    servidor = 'localhost',
    DB = 'play_musica'
)

#instanciando o banco de dados
db = SQLAlchemy(app)

#classes integradas com o bd
class Musica(db.Model):
    id_musica = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    artista = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuario(db.Model):
    id_usuarioo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_us = db.Column(db.String(40), nullable=False)
    login_us = db.Column(db.String(10), nullable=False)
    senha_us = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
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