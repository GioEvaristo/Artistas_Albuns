from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHASEcreTA'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/GioBP"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database import db
from flask_migrate import Migrate
from models import Artistas, Albuns
db.init_app(app)
migrate = Migrate(app, db)

from modulos.artistas.artistas import bp_artista
app.register_blueprint(bp_artista, url_prefix = '/artistas')

from modulos.albuns.albuns import bp_album
app.register_blueprint(bp_album, url_prefix = '/albuns')

@app.route('/')
def index():
    return render_template("home.html")