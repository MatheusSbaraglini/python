from app import app, db
from app.models.cliente import Cliente, ClienteSchema
from flask import jsonify

@app.route('/api/clientes/')
def clientes():
    first_clientes = Cliente.query.first()
    return first_clientes.nome
    '''cliente_schema = ClienteSchema(many=True)
    cliente_output = cliente_schema.dump(first_clientes).data
    return jsonify({'cliente': cliente_output})'''
