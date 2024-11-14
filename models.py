from database import db

class Artistas(db.Model):
    __tablename__ = 'artistas'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    genero = db.Column(db.String(50))

    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

    def __repr__(self):
        return "<Artista: {}>".format(self.nome)
   
class Albuns(db.Model):
    __tablename__ = 'albuns'
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50))
    ano_lancamento = db.Column(db.Integer)
    artista_id = db.Column(db.Integer, db.ForeignKey('artistas.id'))

    artista = db.relationship('Artistas', foreign_keys=artista_id)

    def __init__(self, titulo, ano_lancamento, artista_id):
        self.titulo = titulo
        self.artista_id = artista_id
        self.ano_lancamento = ano_lancamento

    def __repr__(self):
        return "<Álbum: {} - {} - {}>".format(self.titulo, self.ano_lancamento, self.artista.nome)
        