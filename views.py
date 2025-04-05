from flask import render_template, request, redirect, session, flash, url_for
from models import Musica, Usuario
from main import app, db

@app.route('/')

def lista_musica():
    if session.get('usuario_in') is None:
        return redirect(url_for('login'))
     
    lista = Musica.query.order_by(Musica.id)

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

#para pegar a imagem
    imagem = request.files['imagem']
#INDICANDO A PASTA QUE ESTÁ DESCRITA EM CONFIG.PY
    upload = app.config['UPLOAD']

    imagem.save(f'{upload}/album{nova.id}.jpg')


    return redirect('/')

@app.route('/editar/<int:id>')
def editar_musica(id):
    if 'usuario_in' not in session or session['usuario_in'] == None:
        return redirect('/login')
    
    busca = Musica.query.filter_by(id = id).first()
    
    #musica = Musica.query.get(id)
    #if musica is None:
     #   flash('Música não encontrada')
      #  return redirect('/')

    return render_template('editar_musica.html', titulo = 'Editar música', musica_edit = busca)

@app.route('/atualizar_musica', methods = ['POST',])
def atualizar():
    atual = Musica.query.filter_by(id = request.form['id_noform']).first()
    atual.titulo = request.form['titulo']
    atual.artista = request.form['artista']
    atual.genero = request.form['genero']

    db.session.add(atual)
    db.session.commit()

    return redirect('/')

@app.route('/deletar/<int:id>')
def excluir_musica(id):
    if 'usuario_in' not in session or session['usuario_in'] == None:
        return redirect('/login')
    
    Musica.query.filter_by(id = id).delete()

    db.session.commit()

    flash('Música excluída com sucesso!')
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