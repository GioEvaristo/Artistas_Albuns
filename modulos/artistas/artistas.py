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
    return render_template('artista_add.html')

@bp_artista.route('/save', methods = ['POST'])
def save():
    nome = request.form.get('nome')
    genero = request.form.get('genero')

    if nome and genero:
        bp_artista = Artistas(nome, genero)
        db.session.add(bp_artista)
        db.session.commit()
        flash('Artista salvo com sucesso! :D')
        return redirect('/artistas')
    else:
        flash('Preencha todos os campos! >:/')
        return redirect('/artistas/add')
    

@bp_artista.route("/remove/<int:id>")
def remove(id):
    dados = Artistas.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Artista removido com sucesso!')
        return redirect("/artistas")
    else:
        flash("Caminho incorreto!")
        return redirect("/artistas")

@bp_artista.route("/edita/<int:id>")
def edita(id):
    artista = Artistas.query.get(id)
    return render_template("artista_edita.html", dados = artista)

@bp_artista.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    genero = request.form.get('genero')
    if id and nome and genero:
        artista = Artistas.query.get(id)
        artista.nome = nome
        artista.genero = genero
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/artistas')
    else:
        flash('Dados incompletos.')
        return redirect("/artistas")