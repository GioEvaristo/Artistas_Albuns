from flask import Blueprint, render_template, request, redirect, flash
from models import Artistas
from database import db

bp_artista = Blueprint('artistas', __name__, template_folder="templates")

@bp_artista.route('/')
def index():
    dados = Artistas.query.all()
    return render_template('artista.html', artistas = dados)

@bp_artista.route('/add')
def add():
    a = Artistas.query.all()
    return render_template('artista_add.html', artistas = a)

@bp_artista.route('/save', methods = ['POST'])
def save():
    artista_id = request.form.get('artista_id')
    nome = request.form.get('nome')
    genero = request.form.get('genero')

    if artista_id and nome and genero:
        bp_artista = Artistas(artista_id, nome, genero)
        db.session.add(bp_artista)
        db.session.commit()
        flash('Artista salvo com sucesso! :D')
        return redirect('/artistas')
    else:
        flash('Preencha todos os campos! >:/')
        return redirect('/artistas/add')
    

@bp_artista.route("/artista/remove/<int:artista_id>")
def artista_remove(artista_id):
    artista = Artistas.query.get(artista_id)
    if artista:
        db.session.delete(artista)
        db.session.commit()
        flash('Artista removido com sucesso!')
        return redirect("/artistas")
    else:
        flash("Caminho incorreto!")
        return redirect("/artistas")


@bp_artista.route("/artista/edita/<int:artista_id>")
def artista_edita(artista_id):
    artista = Artistas.query.get(artista_id)
    return render_template("artista_edita.html", dados=artista)


@bp_artista.route("/artista/editasave", methods=['POST'])
def artista_editasave():
    artista_id = request.form.get('artista_id')
    nome = request.form.get('nome')
    genero = request.form.get('genero')
    if artista_id and nome and genero:
        album = Artistas.query.get(artista_id)
        album.nome = nome
        album.genero = genero
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/artistas')
    else:
        flash('Dados incompletos.')
        return redirect("/artistas")