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
    a = Albuns.query.all()
    return render_template('album_add.html', albuns=a)

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
    

@bp_album.route("/album/remove/<int:id>")
def album_remove(id):
    album = Albuns.query.get(id)
    if album:
        db.session.delete(album)
        db.session.commit()
        flash('Álbum removido com sucesso!')
        return redirect("/albuns")
    else:
        flash("Caminho incorreto!")
        return redirect("/albuns")


@bp_album.route("/album/edita/<int:id>")
def album_edita(id):
    album = Albuns.query.get(id)
    return render_template("album_edita.html", dados=album)


@bp_album.route("/album/editasave", methods=['POST'])
def album_editasave():
    album_id = request.form.get('id')
    titulo = request.form.get('titulo')
    ano_lancamento = request.form.get('ano_lancamento')
    artista_id = request.form.get('id')
    if album_id and titulo and ano_lancamento and artista_id:
        album = Albuns.query.get(album_id)
        album.titulo = titulo
        album.ano_lancamento = ano_lancamento
        album = Albuns.query.get(artista_id)
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/albuns')
    else:
        flash('Dados incompletos.')
        return redirect("/albuns")