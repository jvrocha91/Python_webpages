from flask import Flask, render_template, request, redirect, url_for
from database import db, Cidade


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cidades.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    cidades = Cidade.query.all()
    return render_template('index.html', cidades=cidades)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        cidade = Cidade(
            codigo_cidade=request.form['codigo_cidade'],
            nome=request.form['nome'],
            estado=request.form['estado']
        )
        db.session.add(cidade)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/edit/<int:cidade_id>', methods=['GET', 'POST'])
def edit(cidade_id):
    cidade = Cidade.query.get_or_404(cidade_id)
    if request.method == 'POST':
        cidade.codigo_cidade = request.form['codigo_cidade']
        cidade.nome = request.form['nome']
        cidade.estado = request.form['estado']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', cidade=cidade)


@app.route('/delete/<int:cidade_id>', methods=['POST'])
def delete(cidade_id):
    cidade = Cidade.query.get_or_404(cidade_id)
    db.session.delete(cidade)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)