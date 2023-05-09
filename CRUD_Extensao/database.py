from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_cidade = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)

    def __init__(self, codigo_cidade, nome, estado):
        self.codigo_cidade = codigo_cidade
        self.nome = nome
        self.estado = estado