from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Musica, Usuario
from main import app, db
from definicoes import recupera, deleta
import time

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

#quebrando o nome da imagem para poder salvar em jpg e png
#abaixo, o nome do arquivo é separado da extensão
#ex: album1.jpg -> album1
    arquivo = imagem.filename.split('.')
#pegando apenas a extensão do arquivo
#ex: jpg
    extensao = arquivo[-1]
#pegando o nome do arquivo sem a extensão e somando a extensão, que pode ser jpg ou png
#ex: arquivo_completo = f'algum{10}.{jpg ou png}'
    momento = time.time()
    arquivo_completo = f'album{nova.id}_{momento}.{extensao}'

    imagem.save(f'{upload}/{arquivo_completo}')


    return redirect('/')

@app.route('/editar/<int:id>')
def editar_musica(id):
    if 'usuario_in' not in session or session['usuario_in'] == None:
        return redirect('/login')
    
    busca = Musica.query.filter_by(id = id).first()

    album = recupera(id)

    return render_template('editar_musica.html', titulo = 'Editar música', musica_edit = busca, album_musica = album)

@app.route('/atualizar_musica', methods = ['POST',])
def atualizar():
    atual = Musica.query.filter_by(id = request.form['id_noform']).first()
    atual.titulo = request.form['titulo']
    atual.artista = request.form['artista']
    atual.genero = request.form['genero']

    db.session.add(atual)
    db.session.commit()

    nova_imagem = request.files['imagem_nova']

    upload = app.config['UPLOAD']

    arquivo = nova_imagem.filename.split('.')
    extensao = arquivo[-1]

    momento = time.time()
    arquivo_completo = f'album{atual.id}_{momento}.{extensao}'

    nova_imagem.save(f'{upload}/{arquivo_completo}')

     #deletando a imagem antiga
    deleta(atual.id)
   

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

@app.route('/uploads/<nome_imagem>')
def imagem(nome_imagem):
    return send_from_directory('uploads', nome_imagem)

  