from flask import render_template

from . import app

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/status')
def status():
    return render_template('estado.html')

@app.route('/movimiento')
def movimiento():
    return 'movimiento'





































