from app import app, db
from app.models.cliente import Cliente, ClienteSchema
from flask import jsonify

@app.route('/api/clientes/')
def clientes():
    cliente = Cliente.query.first()
    cliente_schema = ClienteSchema()
    cliente_output = cliente_schema.dump(cliente)
    return jsonify({'cliente': cliente_output.data})
