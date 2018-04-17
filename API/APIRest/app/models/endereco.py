from app import db, ma


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(50))

class EnderecoSchema(ma.ModelSchema):
    class Meta:
        model = Endereco


db.create_all()
# manager.create_api(Endereco, methods=['POST', 'GET', 'PUT', 'DELETE'])
'''endereco = Endereco(logradouro='rua x', numero=123, bairro='bairro x')
db.session.add(endereco)
db.session.commit()
'''