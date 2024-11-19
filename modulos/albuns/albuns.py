from flask import Blueprint, render_template, request, redirect, flash
from models import Albuns, Artistas
from database import db

bp_album = Blueprint('albuns', __name__, template_folder="templates")

@bp_album.route('/')
def index():
    dados = Albuns.query.all()
    return render_template('album.html', albuns = dados)

@bp_album.route('/add')
def add():
    a = Artistas.query.all()
    return render_template('album_add.html', artistas = a)

@bp_album.route('/save', methods = ['POST'])
def save():
    titulo = request.form.get('titulo')
    ano_lancamento = request.form.get('ano_lancamento')
    artista_id = request.form.get('artista_id')

    if titulo and ano_lancamento and artista_id:
        bp_album = Albuns(titulo, ano_lancamento, artista_id)
        db.session.add(bp_album)
        db.session.commit()
        flash('Álbum salvo com sucesso! :D')
        return redirect('/albuns')
    else:
        flash('Preencha todos os campos! >:/')
        return redirect('/albuns/add')
    
@bp_album.route("/remove/<int:id>")
def remove(id):
    dados = Albuns.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Álbum removido com sucesso!')
        return redirect("/albuns")
    else:
        flash("Caminho incorreto!")
        return redirect("/albuns")

@bp_album.route("/edita/<int:id>")
def edita(id):
    album = Albuns.query.get(id)
    artista = Artistas.query.all()
    return render_template("album_edita.html", dados=album, artista=artista)

@bp_album.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    titulo = request.form.get('titulo')
    ano_lancamento = request.form.get('ano_lancamento')
    artista_id = request.form.get('artista_id')
    if id and titulo and ano_lancamento and artista_id:
        album = Albuns.query.get(id)
        album.titulo = titulo
        album.ano_lancamento = ano_lancamento
        album.artista_id = artista_id
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/albuns')
    else:
        flash('Dados incompletos.')
        return redirect("/albuns")