from app import db, ma


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(50))

class EnderecoSchema(ma.Schema):
    class Meta:
        model = Endereco


db.create_all()
# manager.create_api(Endereco, methods=['POST', 'GET', 'PUT', 'DELETE'])
