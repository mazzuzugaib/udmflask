from main import db
#classes integradas com o bd
class Musica(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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