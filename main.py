from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'satorarepotenetoperarotas'

# Configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'tenet',
        servidor = 'localhost',
        database = 'play_musica'
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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_us = db.Column(db.String(40), nullable=False)
    login_us = db.Column(db.String(10), nullable=False)
    senha_us = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.nome_us
    
@app.route('/')
#def lista_musica():
    #if session['usuario_in'] == None or 'usuario_in' not in session:
        #return redirect(url_for('login'))

def lista_musica():
    if session.get('usuario_in') is None:
        return redirect(url_for('login'))
     
    lista = Musica.query.order_by(Musica.id_musica)

    return render_template('lista_musica.html', titulo = 'Lista de músicas', musicas = lista)

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

    se_repetida = Musica.query.filter_by(titulo=titulo).first()

    if se_repetida:
        flash ('Música já cadastrada')
        return redirect(url_for('cadastro_musica'))
    
    nova = Musica(titulo = titulo, artista = artista, genero = genero)

    db.session.add(nova)
    db.session.commit()

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():

    user = Usuario.query.filter_by(login_us = request.form['usuario']).first()

    if user:
        if request.form['senha'] == user.senha_us:
            session['usuario_in'] = request.form['usuario']
            flash(f'Olá {user.nome_us}, seja bem-vindo(a)')
            return redirect('/') 
        else:
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))

@app.route('/sair')
def sair():
    session['usuario_in'] = None
    return redirect ('/login')
       

app.run(debug=True)
